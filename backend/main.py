from fastapi import FastAPI, UploadFile, File
import mindsdb_sdk
import os
import uuid

app = FastAPI()

# Connect to MindsDB Cloud
mdb = mindsdb_sdk.connect("https://cloud.mindsdb.com", login="YOUR_MINDSDB_USERNAME", password="YOUR_MINDSDB_PASSWORD")

def train_ai_model(file_path: str, model_name: str):
    project = mdb.create_project("ai_models")
    project.learn(name=model_name, from_data=file_path, predict="target_column")
    return model_name

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"temp/{uuid.uuid4()}_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    model_name = f"model_{uuid.uuid4().hex[:8]}"
    trained_model = train_ai_model(file_location, model_name)
    return {"message": "Model trained!", "model_name": trained_model}

@app.get("/predict/{model_name}")
def predict(model_name: str, input_data: str):
    project = mdb.get_project("ai_models")
    model = project.get_model(model_name)
    result = model.predict({"input": input_data})
    return {"prediction": result}

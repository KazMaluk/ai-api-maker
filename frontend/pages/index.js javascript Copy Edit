import { useState } from "react";
import { motion } from "framer-motion";

export default function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [modelName, setModelName] = useState("");

  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setModelName(data.model_name);
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-10">
      <motion.h1 
        className="text-4xl font-bold mb-6" 
        initial={{ opacity: 0, y: -20 }} 
        animate={{ opacity: 1, y: 0 }}
      >
        🔮 AI API Maker – Deploy AI in One Click
      </motion.h1>

      <input type="file" onChange={handleFileUpload} className="p-2 border border-gray-300 rounded-md" />
      <button 
        onClick={handleSubmit} 
        className="mt-4 px-6 py-2 bg-blue-500 text-white rounded-lg shadow-lg hover:bg-blue-600"
      >
        {loading ? "Training..." : "🔥 Train & Deploy"}
      </button>
      
      {modelName && (
        <motion.div className="mt-6 p-4 bg-white shadow-lg rounded-md" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
          ✅ Model Trained! 
          <p className="text-gray-700">🔗 API Endpoint: <span className="font-mono bg-gray-200 p-1 rounded">http://localhost:8000/predict/{modelName}</span></p>
        </motion.div>
      )}
    </div>
  );
}

🌟 Bhagwat Geeta Chatbot 🌟
A Spiritual Companion Built with AI

Unlock the wisdom of the Bhagwat Geeta, one of the most revered texts in Indian philosophy. This chatbot is designed to provide meaningful answers, context-based spiritual guidance, and insights from the scripture using advanced machine learning techniques. Whether you’re looking for philosophical clarity, life advice, or exploring ancient texts, this bot has you covered!

🌼 Key Features
📖 Interactive Q&A
Ask & Learn: Pose any question, and the bot responds with teachings from the Bhagwat Geeta.
Relevant Answers: AI-powered contextual understanding ensures accurate responses.

💬 Custom Prompt Integration
Easily configure how the bot interacts using flexible prompt templates.
🧠 Advanced NLP Engine
Powered by Hugging Face Transformers for enhanced conversational capabilities.
🚀 Fast and Scalable
Integrated with Pinecone for efficient indexing and retrieval of textual data.

🎯 Objectives
Promote Ancient Wisdom: Bridge the gap between traditional knowledge and modern technology.
Enhance Accessibility: Make the profound teachings of the Geeta available to a global audience.
Encourage Spiritual Growth: Provide personalized, meaningful guidance in everyday life.

💻 Installation
Step 1: Clone the Repository
git clone https://github.com/your-username/bhagwat-geeta-chatbot.git
cd bhagwat-geeta-chatbot

Step 2: Set Up a Virtual Environment
conda create --name geetachatbot python=3.10.14
conda activate geetachatbot

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Configure API Keys
Create a .env file with the following content:

HUGGINGFACEHUB_API_TOKEN=our_huggingface_api_token  
PINECONE_API=our_pinecone_api_key  
CUSTOM_PROMPT_TEMPLATE="Answer the user's question using the provided information. If you're unsure, refrain from guessing. Context: {context} Question: {question}"

Step 5: Run the Chatbot
python chatbot.py


🛠️ It Works
Input our Question: Ask questions related to Bhagwat Geeta's teachings.
AI-Driven Response: The chatbot analyzes our query and retrieves a relevant verse or explanation.
Personalized Interaction: Answers are tailored based on the context of our query.


📊 Technologies Used
Python
Hugging Face Transformers: For building the chatbot's conversational model.
Pinecone: For efficient data retrieval and indexing.
Pretrained Language Models: Fine-tuned on Bhagwat Geeta translations and commentaries.

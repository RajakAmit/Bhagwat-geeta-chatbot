import os
import warnings

import streamlit as st
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.huggingface import HuggingFaceInferenceAPI

from utils.get_index import *
from utils.prompt_func import *

# Load environment variables
load_dotenv()
token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Setup model
Settings.llm = HuggingFaceInferenceAPI(
    model_name="mistralai/Mistral-7B-Instruct-v0.3",
    token=token,
    context_window=3900,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    device_map="auto",
)

# Ignore deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Create the index (could take time)
@st.cache_resource
def load_index():
    return create_index()

index = load_index()

# Define the function to get the final result
def final_result(query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response, query

# Format the output for display
def format_output(answer, query):
    result = f"**Question:** {query} 🤔\n\n"
    result += f"**Answer:** 💡 {answer.response} 🙏\n\n"

    if answer.source_nodes:
        result += "You can read more of it at: \n"
        for node in answer.source_nodes:
            metadata = node.node.metadata
            page = metadata.get('page_label', 'N/A')
            source = metadata.get('file_name', 'N/A')
            result += f"- Page {page} from {source}\n"
        result += "\n"

    result += "What would you like to know more?"
    return result

# Streamlit UI
def main():
    st.title("QA Bot powered by Hugging Face and Llama Index")

    # Input from the user
    user_input = st.text_input("Ask a question:", "")
    
    if st.button('Submit') and user_input:
        # Run the query
        with st.spinner('Fetching answer...'):
            response, query = final_result(user_input)
            formatted_output = format_output(response, query)
        
        # Display the response
        st.markdown(formatted_output)

if __name__ == '__main__':
    main()

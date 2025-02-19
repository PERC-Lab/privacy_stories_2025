import os
import sys
import json
import datetime
from getpass import getpass

# Local imports
import utils.text_processing as tp
from model_routes import model_routing

########################################
# 1) Create/Load Human Annotation Data
########################################
prompts_data_json_file = 'data/annotations/prompts_data.json'
if not os.path.exists(prompts_data_json_file):
    prompt_templates_dict = tp.create_prompts_data_json(
        annotations_dir='data/annotations',
        ontology_path='privacy_ontology.json',
        output_json=prompts_data_json_file
    )
else:
    print(f"Using existing prompts data JSON: {prompts_data_json_file}")
    with open(prompts_data_json_file, 'r', encoding='utf-8') as f:
        prompt_templates_dict = json.load(f)

########################################
# 2) Prompt for API Keys
########################################
os.environ['OPENAI_API_KEY'] = getpass('Enter your OPENAI API key: ')
os.environ['GROQ_API_KEY']   = getpass('Enter your Groq API key: ')

########################################
# 3) Define Models and Loop
########################################
models = [
    'groq:qwen-2.5-32b',
    # 'openai:gpt-4o-latest',
    # 'groq:deepseek-r1-distill-qwen-32b',
    # 'groq:llama-3.3-70b-versatile',
]

# Create a short 6-character timestamp (HHMMSS)
time_str = datetime.datetime.now().strftime('%H%M%S')

########################################
# 4) Run Annotations per Model
########################################
for model in models:
    # Make the model name file-safe by replacing special characters
    model_filename = model.replace(':', '_').replace('.', '_')
    
    # Build a unique output CSV name
    output_csv = f"data/responses/LLMAnnotation_{model_filename}_{time_str}.csv"
    
    print(f"\nRunning annotation for model: {model}")
    print(f"Saving results to: {output_csv}")
    
    # Run the multi-file annotation process
    model_routing.run_multi_file_annotations(
        prompt_templates_dict,
        output_csv,
        models=[model],
        num_runs=1
    )

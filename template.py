import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s')


list_of_files = [
    "src/__init__.py",
    "src/helpers.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "templates/index.html",
    "static/style.css",
    "static/jquery.min.js",
    "store_index.py"
]



for filepath in list_of_files:
    file_path = Path(filepath)
    
    filedir , filename= os.path.split(file_path)


    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filename}")
            
            
    else:
        logging.info(f"File already exists: {filename}")
    


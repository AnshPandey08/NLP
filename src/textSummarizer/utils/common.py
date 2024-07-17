import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

def read_yaml_file(path_to_yaml: str) -> ConfigBox:
    """
    Read a YAML file and return its contents.

    Args:
        path_to_yaml (str): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If there is an issue reading the file.

    Returns:
        ConfigBox: The contents of the YAML file wrapped in a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The YAML file is empty.")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose: True):
    """create list of dictionries
    Args:
    path_to_directories (list): list of path of Directories
    ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at:  {path}")
            
            

@ensure_annotations
def get_size(path: os.path) -> str:
    """get size in KB 
    
    Args:
       path (path): path of the file
       
    Returns:
       str: size in KB
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


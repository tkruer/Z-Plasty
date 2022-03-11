import os
from typing import Union
import json
from colorama import Fore
import datetime

def read_file(filename: str) -> Union[str, dict, None]:
    """Reads from a file
    Args:
        filename: Name of the file
    Returns:
        dict: if the file is json
        str:  if the file is txt
        None: on error
    """
    try:
        file_type = filename.split(".")[-1]
        if file_type == "json":
            if os.stat(filename).st_size == 0:
                return {}
            with open(filename, "r") as f:
                j = json.load(f)
            return j

        elif file_type == "txt":
            with open(filename, "r") as f:
                return f.read()
        else:
            return None
    except Exception as e:
        raise e

def get_time() -> str:
    """
    Simple function that returns a string containing info about current time and location.
    Returns:
        now {str}   - String in the format of '[time]'
    """
    now = str(datetime.datetime.now().time())
    # now = now[:-3] #[14:49:05.525]
    now = now[:-7]  # only want 3 decimal places
    return f"[{now}]"

def log_message(status: str, message: str, location: str = None, ) -> None:
    """
    A function to handle logging
    Args:
        status {str}    - Level of the logger - how problematic the message is, see Notes for special meanings
        message {str}   - Log message
    Returns:
        None
    Notes:
        Statuses with special meaning:
            - debug
            - info
            - warning
            - error
            - critical
    """
    if location:
        status = f"[{status.upper()}] ({location.upper()})"
    else:
        status = f"[{status.upper()}]"
    if status.lower().strip() == 'success':
        print(Fore.GREEN + f"{get_time()} {status} -> {message}")
    elif status.lower().strip() == 'error':
        print(Fore.RED + f"{get_time()} {status} -> {message}")
    else:
        print(f"{get_time()} {status} -> {message}")
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
LOG_FILE_PATH = os.makedirs(logs_path,exist_ok=True)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
                    level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging is working fine")
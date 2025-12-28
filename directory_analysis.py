import os
import pprint
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_size(size_bytes):
    return f"{size_bytes / (1024 * 1024):.2f} MB"

def convert_time(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime("%Y-%m-%d %H:%M:%S")

def analyze_directory(path):
    logger.info(f"Analyzing directory: {path}")
    files = dict()
    no_of_files = 0
    no_of_dirs = 0
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                file = dict()
                file["entry_name"] = entry.name
                file["entry_path"] = entry.path
                file["entry_size"] = convert_size(entry.stat().st_size)
                file["entry_size_in_bytes"] = entry.stat().st_size
                file["entry_modified_time"] = convert_time(entry.stat().st_mtime)
                file["entry_accessed_time"] = convert_time(entry.stat().st_atime)
                if entry.is_file():
                    no_of_files += 1
                    file["entry_type"] = "File"
                else:
                    no_of_dirs += 1
                    file["entry_type"] = "Directory"
                files[entry.name] = file
        
        # pprint.pprint(files)                                                        # Pretty print the collected file information / Uncomment to see detailed file info
        logger.info("Summary of Directory Analysis:")
        logger.info(f"Total files: {no_of_files}")
        logger.info(f"Total directories: {no_of_dirs}")
        
        # To find distinct file sizes
        distinct_sizes = set()
        for file_info in files.values():
            if file_info.get("entry_type") == "File":                                              
                distinct_sizes.add(file_info.get("entry_size_in_bytes"))
        logger.info(f"No. of distinct file sizes: {len(distinct_sizes)}")
        
        # To find duplicate files based on size
        size_to_files = dict()
        for file_info in files.values():
            size = file_info.get("entry_size_in_bytes")
            if size not in size_to_files:
                size_to_files[size] = []
            size_to_files[size].append(file_info.get("entry_name"))

        # Files with duplicate sizes
        for size, file_list in size_to_files.items():
            if len(file_list) > 1:
                logger.info(f"Size: {size} bytes - Files: {file_list}")

    except FileNotFoundError:
        logger.error(f"The directory {path} does not exist...")


if __name__ == "__main__":
    directory_path = input("Enter the directory path to analyze: ")
    analyze_directory(directory_path)
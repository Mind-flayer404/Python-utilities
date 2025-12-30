import json
import logging
import math

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def split_json_file(input_file, output_prefix, file_count=5):
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    logger.info(f"Total records in input file: {len(data)}")
    chunk_size = math.ceil(len(data) / file_count)      # Calculate the size of each chunk
    logger.info(f"Splitting into {file_count} files of size: {chunk_size}")

    for i in range(file_count):
        # Use list slicing to get the appropriate chunk
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        chunk = data[start_index:end_index]

        # Writing each chunk to a new JSON file
        output_filename = f"{output_prefix}_{i+1}.json"
        with open(output_filename, "w", encoding="utf-8") as outfile:
            json.dump(chunk, outfile, indent=4)
        logger.info(f"Created {output_filename} with {len(chunk)} records...")


if __name__ == "__main__":
    input_file = "large_data.json"                  # Replace with your input JSON file
    output_prefix = "chunked_data"                  # Prefix for output file path
    file_count = int(input("Enter the number of files to split into: "))
    split_json_file(input_file, output_prefix, file_count)
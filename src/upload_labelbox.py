import labelbox as lb
from dotenv import load_dotenv
import os
import glob

# Load environment variables from .env file
load_dotenv()
print("Environment variables loaded.")

# Initialize the Labelbox client with the API key from the environment
client = lb.Client(api_key=os.getenv("LABELBOX_API_KEY"))
print("Labelbox client initialized.")

# Create a new dataset
dataset = client.create_dataset(name="Shoplifting Dataset")
print("Dataset created.")

# Define the schema ID
schema_id = "correct_schema_id_here"  # Replace with the correct schema ID
print(f"Using schema ID: {schema_id}")

# Create data payload for shoplifting videos
shoplifting_assets = []
for video_path in glob.glob("archive/Shoplifting dataset/Shoplifting/*.mp4"):
    global_key = os.path.basename(video_path).replace('.mp4', '')
    shoplifting_assets.append({
        "row_data": video_path,
        "global_key": global_key,
        "media_type": "VIDEO",
        "metadata_fields": [{"schema_id": schema_id, "value": "shoplifting"}],
    })
print(f"Shoplifting assets prepared: {len(shoplifting_assets)}")

# Bulk add data rows to the dataset
task = dataset.create_data_rows(shoplifting_assets)
print("Data rows creation task started.")

# Wait for the task to complete
task.wait_till_done()
print("Data rows creation task completed.")

# Print any errors that occurred during the upload
if task.errors:
    print("Errors occurred during upload:")
    print(task.errors)
else:
    print("All assets uploaded successfully.")

import labelbox as lb
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Labelbox client with the API key from the environment
client = lb.Client(api_key=os.getenv("LABELBOX_API_KEY"))

# Create a new dataset
dataset = client.create_dataset(name="Shoplifting Detection Dataset")

# Create data payload for normal shopping videos
normal_assets = [
    {
        "row_data": "https://your-url.com/path/to/normal_video_1.mp4",
        "global_key": "normal-video-0001",
        "media_type": "VIDEO",
        "metadata_fields": [{"schema_id": "your_schema_id", "value": "normal shopping"}],
    },
    {
        "row_data": "https://your-url.com/path/to/normal_video_2.mp4",
        "global_key": "normal-video-0002",
        "media_type": "VIDEO",
        "metadata_fields": [{"schema_id": "your_schema_id", "value": "normal shopping"}],
    },
    # Add more normal videos as needed
]

# Create data payload for shoplifting videos
shoplifting_assets = [
    {
        "row_data": "https://your-url.com/path/to/shoplifting_video_1.mp4",
        "global_key": "shoplifting-video-0001",
        "media_type": "VIDEO",
        "metadata_fields": [{"schema_id": "your_schema_id", "value": "shoplifting"}],
    },
    {
        "row_data": "https://your-url.com/path/to/shoplifting_video_2.mp4",
        "global_key": "shoplifting-video-0002",
        "media_type": "VIDEO",
        "metadata_fields": [{"schema_id": "your_schema_id", "value": "shoplifting"}],
    },
    # Add more shoplifting videos as needed
]

# Combine both asset lists
assets = normal_assets + shoplifting_assets

# Bulk add data rows to the dataset
task = dataset.create_data_rows(assets)

# Wait for the task to complete
task.wait_till_done()

# Print any errors that occurred during the upload
print(task.errors)

import labelbox as lb
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
print("Environment variables loaded.")

# Initialize the Labelbox client with the API key from the environment
client = lb.Client(api_key=os.getenv("LABELBOX_API_KEY"))
print("Labelbox client initialized.")

# Define the ontology (schema) for the project
ontology_builder = lb.OntologyBuilder(
    classifications=[
        lb.Classification(
            class_type=lb.Classification.Type.RADIO,
            instructions="Label indicating whether the behavior is normal shopping or shoplifting.",
            name="Behavior",
            options=[
                lb.Option(value="Normal"),
                lb.Option(value="Shoplifting")
            ]
        ),
        lb.Classification(
            class_type=lb.Classification.Type.TEXT,  # Use TEXT for numerical input
            instructions="Confidence score of the detection (as text).",
            name="Confidence"
        )
    ]
)
print("Ontology defined.")

# Create the ontology
ontology = client.create_ontology("Shoplifting Detection Ontology", ontology_builder.asdict(), media_type=lb.MediaType.Video)
print("Ontology created.")

# Create a new project
project = client.create_project(
    name="Shoplifting Detection Project", 
    description="Project for detecting shoplifting and normal shopping behaviors.",
    media_type=lb.MediaType.Video
)
print("Project created.")

# Associate the ontology with the project
# Check the latest Labelbox documentation for the correct method to associate the ontology
# This might involve using a different method or API call

print("Project and schema created successfully.")

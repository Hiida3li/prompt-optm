import re
from typing import List
from pydantic import BaseModel, Field, create_model
import json

def create_topic_schema(topic_list: List[str]) -> str:
    schema_dict = []
    for topic in topic_list:
        # Create model name: lowercase with no special chars or spaces
        model_name = re.sub(r'[^a-zA-Z0-9]', '', topic).lower()
        
        # Create a dynamic Pydantic model
        TopicModel = create_model(
            model_name,
            description=(str, Field(description=topic)),
            __base__=BaseModel
        )
        schema_dict.append(TopicModel.model_json_schema())
        # Return the schema as a formatted JSON string
    return schema_dict
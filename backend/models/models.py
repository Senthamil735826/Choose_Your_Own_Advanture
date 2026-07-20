from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class StoryOptionalLLM(BaseModel):
    text:str = Field(..., description="The text of the option shown to the user")
    nextNode: Optional[Dict[str, Any]] = Field(None, description="The next node that this option leads to")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="The main content of the story node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinningEnding: bool = Field(description="whether this node is a winning ending node")
    options: Optional[List[StoryOptionalLLM]] = Field(None, description="The options available at this node")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")
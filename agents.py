from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langgraph.graph import MessagesState

class WeatherResponse(BaseModel):
    '''Respond to the user with this'''
    temperature: float = Field(description="Temperature in fahrenheit")
    wind_direction: str = Field(description="The direction os the wind in abbreviated form")
    wind_speed: float = Field(description="The speed of the wind in km/h")

# Inherit 'message' key from MessagesState, which is a list of messages
class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: WeatherResponse

@tool
def get_weather(city: Literal["ahm", "surat"]):
    '''Use this to get weather information.'''
    
    return WeatherResponse()
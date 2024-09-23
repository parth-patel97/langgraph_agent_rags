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
    """Use this to get weather information."""
    if city == "nyc":
        return "It is cloudy in NYC, with 5 mph winds in the North-East direction and a temperature of 70 degrees"
    elif city == "sf":
        return "It is 75 degrees and sunny in SF, with 3 mph winds in the South-East direction"
    else:
        raise AssertionError("Unknown city")
    
tools = [get_weather]
    
model = ChatAnthropic(model="claude-3-opus-20240229")
    
model_with_tools = model.bind_tools(tools)
model_with_structured_output = model.with_structured_output(WeatherResponse)
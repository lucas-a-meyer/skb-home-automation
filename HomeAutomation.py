import semantic_kernel as sk
from typing import Annotated
from semantic_kernel.functions.kernel_function_decorator import kernel_function

class HomeAutomation:
    def __init__(self):
        pass

    @kernel_function(
        description="Opens or closes the windows of the living room or bedroom.",
        name="OperateWindow",
    )      
    def OperateWindow(self, 
    location: Annotated[str, "The location where the windows are to be opened or closed. Must be either 'living room' or 'bedroom'"],
    action: Annotated[str, "Whether to open or close the windows"]) -> Annotated[str, "The output is a string describing whether the windows were opened or closed" ]:
        if location in ["living room", "bedroom"]:
            result = f"Changed status of the {location} windows to {action}."            
            return result
        else:
            error = f"Invalid location {location} specified."
            return error

    @kernel_function(
        description="Turns the lights of the living room, kitchen, bedroom or garage on or off.",
        name="OperateLight",
    )
    def OperateLight(self, 
    location: Annotated[str, "The location where the lights are to be turned on or off. Must be either 'living room', 'kitchen', 'bedroom' or 'garage'"],
    action: Annotated[str, "Whether to turn the lights on or off"]) -> Annotated[str,  "The output is a string describing whether the lights were turned on or off" ]:
        if location in ["kitchen", "living room", "bedroom", "garage"]:
            result = f"Changed status of the {location} lights to {action}."
            
            return result
        else:
            error = f"Invalid location {location} specified."
            return error

    @kernel_function(
        description="Opens or closes the garage door.",
        name="OperateGarageDoor",
    )
    def OperateGarageDoor(self, 
            action:  Annotated[str, "Whether to open or close the garage door"]) -> Annotated[str, "The output is a string describing whether the garage door was opened or closed" ]:
        result = f"Changed the status of the garage door to {action}."       
        return result

# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_new_project import __semver__

# TODO - should inherit from some TaskParameters base class rather than BaseSchema
class UclOpenNewProjectTaskParameters(BaseSchema):
    ...


class UclOpenNewProjectTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenNewProject"] = Field(default="UclOpenNewProject", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenNewProjectTaskParameters = Field(description="Parameters of the task logic")
    ...
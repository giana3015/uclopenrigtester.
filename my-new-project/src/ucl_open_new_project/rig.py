from typing import Literal, Dict
from pydantic import Field

from ucl_open.rigs.base import BaseSchema
import ucl_open.rigs.device as Device

from ucl_open_new_project import __semver__


class UclOpenNewProjectRig(BaseSchema):
    version: Literal[__semver__] = __semver__
    ...
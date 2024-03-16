# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.assistant_object_tools_inner import AssistantObjectToolsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateRunRequest(BaseModel):
    """
    CreateRunRequest
    """ # noqa: E501
    assistant_id: StrictStr = Field(description="The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.")
    model: Optional[StrictStr] = Field(default=None, description="The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.")
    instructions: Optional[StrictStr] = Field(default=None, description="Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.")
    additional_instructions: Optional[StrictStr] = Field(default=None, description="Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.")
    tools: Optional[Annotated[List[AssistantObjectToolsInner], Field(max_length=20)]] = Field(default=None, description="Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="metadata_description")
    __properties: ClassVar[List[str]] = ["assistant_id", "model", "instructions", "additional_instructions", "tools", "metadata"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CreateRunRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if instructions (nullable) is None
        # and model_fields_set contains the field
        if self.instructions is None and "instructions" in self.model_fields_set:
            _dict['instructions'] = None

        # set to None if additional_instructions (nullable) is None
        # and model_fields_set contains the field
        if self.additional_instructions is None and "additional_instructions" in self.model_fields_set:
            _dict['additional_instructions'] = None

        # set to None if tools (nullable) is None
        # and model_fields_set contains the field
        if self.tools is None and "tools" in self.model_fields_set:
            _dict['tools'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assistant_id": obj.get("assistant_id"),
            "model": obj.get("model"),
            "instructions": obj.get("instructions"),
            "additional_instructions": obj.get("additional_instructions"),
            "tools": [AssistantObjectToolsInner.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj



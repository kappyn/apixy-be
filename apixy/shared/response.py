import enum
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


# this could be more complex in the future - i.e. to differentiate between error types
class ResponseStatus(enum.Enum):
    """Marks whether the action succeeded"""

    SUCCESS = enum.auto()
    ERROR = enum.auto()


@dataclass
class Response(Generic[T]):
    """The base response class."""

    status: ResponseStatus
    errors: Optional[list[str]]
    content: T

    @classmethod
    def success(cls, content: T) -> "Response[T]":
        """Factory function for creating a success-response."""
        return cls(status=ResponseStatus.SUCCESS, errors=None, content=content)

    @classmethod
    def error(cls, errors: list[str], content: T) -> "Response[T]":
        """Factory function for creating a response with errors."""
        return cls(status=ResponseStatus.ERROR, errors=errors, content=content)

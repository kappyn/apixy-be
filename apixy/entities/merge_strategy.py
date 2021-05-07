from abc import abstractmethod
from collections.abc import Collection
from typing import Any, Final, Iterable, Mapping

from apixy.entities.shared import ForbidExtraModel


class MergeStrategy(ForbidExtraModel):
    """
    Base class for merge strategies to have same interface.
    Merge strategy is a definition of how datasource outputs should be processed.

    :param __root__: name of the merge strategy
    """

    __root__: str

    @staticmethod
    @abstractmethod
    def apply(data: Iterable[Any]) -> Collection[Any]:
        ...


class ConcatenationMergeStrategy(MergeStrategy):
    """
    Simple merge strategy which concatenates results of Collection enumerating them.
    """

    __root__: str = "concatenation"

    @staticmethod
    def apply(data: Iterable[Any]) -> Collection[Any]:
        return {str(index): each for index, each in enumerate(data)}


MERGE_STRATEGY_MAPPING: Final[Mapping[str, MergeStrategy]] = {
    "concatenation": ConcatenationMergeStrategy(),
}

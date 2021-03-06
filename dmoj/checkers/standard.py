from typing import Callable

from dmoj.result import CheckerResult
from ._checker import standard
from ..utils.unicode import utf8bytes


def check(
    process_output: bytes, judge_output: bytes, point_value: float, _checker: Callable[[bytes, bytes], tuple] = standard, **kwargs
) -> CheckerResult:
    passed, feedback = _checker(utf8bytes(judge_output), utf8bytes(process_output))
    return CheckerResult(passed, point_value, extended_feedback=feedback.decode("utf-8"))


del standard

from typing import Union

from dmoj.result import CheckerResult
from dmoj.checkers.floats import check as floats_check


def check(process_output: bytes, judge_output: bytes, **kwargs) -> Union[CheckerResult, bool]:
    return floats_check(process_output, judge_output, error_mode='absolute', **kwargs)

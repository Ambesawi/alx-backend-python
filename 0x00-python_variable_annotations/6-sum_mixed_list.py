#!/usr/bin/env python3

""" mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  returns sum as a float. """
    return float(sum(mxd_lst))

#!/usr/bin/env python3
'''Complex types - mixed list.
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Returns sum of mxd_lst list of floats and ints
    '''
    return float(sum(mxd_lst))

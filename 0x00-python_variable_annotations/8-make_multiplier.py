#!/usr/bin/env python3
''' Description: Accepts a float multiplier as arg and returns a function
                 that multiplies a float by the multiplier
    Params: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputs function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier

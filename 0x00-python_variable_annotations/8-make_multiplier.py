#!/usr/bin/env python3
''' Description: Accept a float multiplier as argument and returns a function 
                that multiplies a float by multiplier.
    Params: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputs function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier

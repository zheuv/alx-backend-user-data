#!/usr/bin/env python3
""" Doc for the script """

import re
from typing import List


def filter_datum(f: List[str], r: str, m: str, s: str) -> str:
    """ Doc for function """
    return re.sub(f"({'|'.join(f)})=[^{s}]*",
                  lambda m: m.group(0).split('=')[0] + f"={r}",
                  m)

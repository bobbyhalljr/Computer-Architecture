#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
sys.path.append('./examples')

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()
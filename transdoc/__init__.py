"""
# 🏳️‍⚧️ Transdoc 🏳️‍⚧️

A simple tool for transforming Python docstrings by embedding results from
Python function calls.
"""
__all__ = [
    '__version__',
    'main',
    'TransdocHandler',
    'Rule',
]

from .__consts import VERSION as __version__
from .handlers import TransdocHandler
from .__rule import Rule
from .__processor import main

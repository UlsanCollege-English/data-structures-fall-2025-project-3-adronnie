"""Pytest configuration helpers.

Ensure the project root is added to sys.path during test collection so tests
can import the top-level `flight_planner` module no matter how pytest sets
the working directory.
"""
import os
import sys

# Insert the repository root (parent of tests/) at the start of sys.path so
# imports like `import flight_planner` succeed when pytest changes the CWD.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

"""Top-level shim for tests — re-export from `src.flight_planner`.

Tests import `flight_planner` at the project root. The real implementation lives
in `src/flight_planner.py` so this small shim re-exports its public API.
"""

from src.flight_planner import *  # re-export public names for tests

__all__ = [name for name in globals().keys() if not name.startswith("_")]

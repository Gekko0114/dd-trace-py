"""
This integration provides context management for tracing the execution flow
of concurrent execution of ``asyncio.Task``.
"""
from ddtrace.internal.utils.importlib import require_modules


required_modules = ["asyncio"]

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from ddtrace._trace.provider import DefaultContextProvider

        context_provider = DefaultContextProvider()

        # Required to allow users to import from `ddtrace.contrib.asyncio.patch` directly
        # Expose public methods
        import warnings as _w

        with _w.catch_warnings():
            _w.simplefilter("ignore", DeprecationWarning)
            from . import patch as _  # noqa: F401, I001
        from ddtrace.contrib.internal.asyncio.helpers import ensure_future
        from ddtrace.contrib.internal.asyncio.helpers import run_in_executor
        from ddtrace.contrib.internal.asyncio.helpers import set_call_context
        from ddtrace.contrib.internal.asyncio.patch import get_version
        from ddtrace.contrib.internal.asyncio.patch import patch
        from ddtrace.contrib.internal.asyncio.patch import unpatch  # noqa: F401

        __all__ = ["context_provider", "set_call_context", "ensure_future", "run_in_executor", "patch", "get_version"]

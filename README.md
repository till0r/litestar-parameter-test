uv run litestar run --debug
Using Litestar app from app:app
Starting server process ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
┌──────────────────────────────┬──────────────────────┐
│ Litestar version             │ 2.14.0               │
│ Debug mode                   │ Enabled              │
│ Python Debugger on exception │ Disabled             │
│ CORS                         │ Disabled             │
│ CSRF                         │ Disabled             │
│ OpenAPI                      │ Enabled path=/schema │
│ Compression                  │ Disabled             │
└──────────────────────────────┴──────────────────────┘
INFO:     Started server process [13520]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:58376 - "GET /params?some_bool= HTTP/1.1" 400 Bad Request
ERROR - 2025-01-23 14:55:34,577 - litestar - config - Uncaught exception (connection_type=http, path=/params):
Traceback (most recent call last):
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/_signature/model.py", line 205, in parse_values_from_connection_kwargs
    return convert(kwargs, cls, strict=False, dec_hook=deserializer, str_keys=True).to_dict()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
msgspec.ValidationError: Expected `bool | null`, got `str` - at `$.some_bool`

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/middleware/_internal/exceptions/middleware.py", line 159, in __call__
    await self.app(scope, receive, capture_response_started)
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/_asgi/asgi_router.py", line 100, in __call__
    await asgi_app(scope, receive, send)
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/routes/http.py", line 81, in handle
    response = await self._get_response_for_request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/routes/http.py", line 133, in _get_response_for_request
    return await self._call_handler_function(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/routes/http.py", line 153, in _call_handler_function
    response_data, cleanup_group = await self._get_response_data(
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/routes/http.py", line 184, in _get_response_data
    parsed_kwargs = route_handler.signature_model.parse_values_from_connection_kwargs(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/till/Repositories/litestar-parameter-test/.venv/lib/python3.11/site-packages/litestar/_signature/model.py", line 218, in parse_values_from_connection_kwargs
    raise cls._create_exception(messages=messages, connection=connection) from e
litestar.exceptions.http_exceptions.ValidationException: 400: Validation failed for GET /params?some_bool=

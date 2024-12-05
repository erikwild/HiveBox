# pylint: disable=C0114
# pylint: disable=C0116
# pylint: disable=C0305
"""
This module defines a simple FastAPI application.

It provides a root endpoint (`/`) that returns a JSON message.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello World"}

@app.get("/version")
async def version():
    """
    Version endpoint that returns the current version.
    """
    return {"message": "version"}

@app.get("/temperature")
async def temperature():
    """
    Temperature endpoint that returns the current temperature.
    """
    return {"message": "Temperature"}



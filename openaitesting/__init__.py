import azure.functions as func
import logging
import openai
import json
import os 
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="openaitesting")
def openaitesting(req: func.HttpRequest) -> func.HttpResponse:
     logging.info(f"Received request data: {data}")
     api_key = os.getenv("OPENAI_API_KEY")
    endpoint = os.getenv("OPENAI_ENDPOINT")

    if not api_key or not endpoint:
        return func.HttpResponse("Environment variables are missing.", status_code=500)

    return func.HttpResponse(f"API Key: {api_key}, Endpoint: {endpoint}", status_code=200)


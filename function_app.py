import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="openaitesting")
def openaitest(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')

    try:
        # Parse the incoming request
        data = req.get_json()
        script = data.get("script")
        if not script:
            return func.HttpResponse("No script provided.", status_code=400)

        # Analyze and fix the script
        prompt = (
            f"The following Azure Automation script has an error. "
            f"Analyze the script, fix the issue, and explain the changes:\n\n{script}"
        )

        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=800,
            temperature=0.5
        )

        # Extract and return the result
        fixed_script = response["choices"][0]["text"].strip()
        explanation = (
            f"The script was analyzed, and the following changes were made to fix the errors:\n\n"
            f"{fixed_script}"
        )

        return func.HttpResponse(
            json.dumps({"fixed_script": fixed_script, "explanation": explanation}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse("Error analyzing or fixing the script.", status_code=500)

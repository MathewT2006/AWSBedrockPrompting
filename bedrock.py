# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Set up the prompt and temperature.
prompt = "make a list of the best cloud service providers ranked"
temperature = 0.9
bedrock = boto3.client("bedrock-runtime")

request = {
    "messages": [{"role": "user", "content": [{"text": prompt}]}],
    "inferenceConfig": {"temperature": temperature},
}

response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
)

response_body = json.loads(response.get("body").read())
reply = response_body["output"]["message"]["content"][0]["text"]
print(reply)

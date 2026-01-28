# AWSBedrockPrompting
Accessing AWS Bedrock using an IDE through the AWS SDK

<img width="541" height="158" alt="image" src="https://github.com/user-attachments/assets/42489b5d-7cb7-40b0-92e6-07c24ba8a72e" />


This script acts as a command-line interface (CLI) client for **Amazon Bedrock**. It allows users to send natural language prompts to the **Amazon Nova Lite v1** model and receive text-based responses directly in the terminal.

## Features

* **Interactive Input:** Accepts user prompts via standard console input.
* **Model Integration:** Specifically configured for `amazon.nova-lite-v1:0`, optimized for speed and cost-effectiveness.
* **Inference Configuration:** Uses a temperature setting of `0.9` for creative and varied responses.
* **JSON Handling:** Automatically constructs the request payload and parses the JSON response body.


## Usage

1. Save the code to a file, for example, `nova_chat.py`.
2. Run the script from your terminal:

```bash
python nova_chat.py

```

3. When prompted, type your request and press **Enter**:

```text
Please enter your prompt: Write a haiku about coding.

```

4. The script will print the model's response:

```text
Logic flows like streams,
Bugs hide in the shadows deep,
Code brings life to dreams.

```

---

import os

def handler(event, context):
    user = event.get("user", "Developer")
    env = os.environ.get("APP_ENV", "unknown")
    return {
        "statusCode": 200,
        "message": f"Hello {user}! Running live from my own Git repo in [{env}] mode."
    }

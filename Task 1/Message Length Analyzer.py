# List of messages
messages = ["Hi", "Welcome to the platform", "OK"]

# Analyze each message
for msg in messages:
    length = len(msg)
    print(f"Message: '{msg}' | Length: {length}", end="")
    
    # Flag messages longer than 10 characters
    if length > 10:
        print(" | Flag: Too long")
    else:
        print(" | Flag: OK")

from specklepy.api.client import SpeckleClient

# Create client
client = SpeckleClient(host="app.speckle.systems")

# Authenticate with token
token = "62e7eae2f934c9ebd98451282e5029ef29b8d5e8bf"  # Replace with your token
client.authenticate_with_token(token)

print(f"✓ Authenticated as {client.account.userInfo.name}")


#a1cd06bae2 workspace idfrom specklepy.api.client import SpeckleClient

def get_client():
    client = SpeckleClient(host="app.speckle.systems")
    token = "62e7eae2f934c9ebd98451282e5029ef29b8d5e8bf"  # Replace with your token
    client.authenticate_with_token(token)
    return client

# Puedes dejar este bloque para pruebas manuales
if __name__ == "__main__":
    client = get_client()
    print(f"✓ Authenticated as {client.account.userInfo.name}")

#a1cd06bae2 workspace idfrom specklepy.api.client import SpeckleClient

def get_client():
    client = SpeckleClient(host="app.speckle.systems")
    token = "62e7eae2f934c9ebd98451282e5029ef29b8d5e8bf"  # Replace with your token
    client.authenticate_with_token(token)
    return client

if __name__ == "__main__":
    client = get_client()
    print(f"✓ Authenticated as {client.account.userInfo.name}")

#a1cd06bae2 workspace id


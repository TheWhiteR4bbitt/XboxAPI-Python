from xboxapi import Client

client = Client(api_key='0007f9a92f608c0e55c03b8712a552edf06db78a')
gamer = client.gamer('voidpirate')

profile = gamer.get('profile')

print(client)
print(gamer)
print(profile)
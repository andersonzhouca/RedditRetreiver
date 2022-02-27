import discord

def get_token():
    with open("token.txt","r") as f:
        line = f.readlines()
        return line[0].strip()
print(get_token())
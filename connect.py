import discord
import os
import json


# Output file
def write_file(args):
        f = open('output.txt', 'a')
        f.write(args)
        f.close()


# Read Config
def config_json_read():
    with open(os.path.join("config", "config.json"), "r") as config_file:
        data = json.load(config_file)
    return data


# Discord Client called
client = discord.Client()


# Discord on message function that reads data, especially the URL
@client.event
async def on_message(message):
    messages = message.content
    data = config_json_read()
    guild_id = data['guild_id']
    channel_id = data['channel_id']
    valid_user_id = data['valid_user_id']
    id = client.get_guild(guild_id)
    channel = [channel_id]
    valid_user = [valid_user_id]

    if message.author == client.user:
        return

#    if message.content.find("https") != -1:
    if "https" in message.content and str(message.channel) in channel:
        await message.channel.send(messages)

        # For debugging message output
        print(messages)

        # write to output.txt
        write_file(messages + "\n")
    return messages


def main():
    data = config_json_read()
    token = data['token']
    client.run(token)


if __name__ == '__main__':
    main()



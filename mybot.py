import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            msg = "Hello (0 author.mention".format(message)
            await message.channel.send("Hi, " + message.author.mention) #right part pings whoever typed !hello
        if message.content.startswith('!reply'):
            await message.reply('Hello!', mention_author=True)

client = MyClient()
client.run("ODMxOTIxMDMyNTAzMDk5NTAz.YHcQ1g.YaX8TBi9FjhCdip_FF5HkxXwMyU")
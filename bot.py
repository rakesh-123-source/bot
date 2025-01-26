import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
keep_alive()

BOT_TOKEN = os.environ['discord_bot_token']  # 
YOUR_USER_ID = os.environ['user_id'] 
CHANNEL_NAME = "〔💬〕main-chat" 

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online and ready to send scheduled messages!")
    bot.loop.create_task(send_daily_messages())

@bot.event
async def on_message(message):
    # Don't let the bot respond to its own messages
    if message.author == bot.user:
        return

    # Check if @DRAXITY (your user ID) is mentioned in the message
    if any(mention.id == int(YOUR_USER_ID) for mention in message.mentions):
        # Find the user in the server by user ID
        user = discord.utils.get(message.guild.members, id=int(YOUR_USER_ID))

        if user and user.status == discord.Status.offline:
            await message.channel.send(f"{message.author.mention}, DRAXITY is offline now!")

    # Ensure the bot processes commands
    await bot.process_commands(message)

async def send_daily_messages():
    await bot.wait_until_ready()
    while True:
        now = datetime.now() + timedelta(hours=5, minutes=30)
        today = datetime.now()
        good_morning_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=7)
        if now > good_morning_time:
            good_morning_time += timedelta(days=1)

        promotion_time_12pm = datetime.combine(today, datetime.min.time()) + timedelta(hours=12)
        if now > promotion_time_12pm:
            promotion_time_12pm += timedelta(days=1)

        promotion_time_3pm = datetime.combine(today, datetime.min.time()) + timedelta(hours=15)
        if now > promotion_time_3pm:
            promotion_time_3pm += timedelta(days=1)

        promotion_time_7pm = datetime.combine(today, datetime.min.time()) + timedelta(hours=19)
        if now > promotion_time_7pm:
            promotion_time_7pm += timedelta(days=1)

        good_night_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=22)
        if now > good_night_time:
            good_night_time += timedelta(days=1)

        next_message_time = min(good_morning_time, promotion_time_12pm, promotion_time_3pm, promotion_time_7pm, good_night_time)
        time_to_sleep = (next_message_time - now).total_seconds()

        print(f"Sleeping until: {next_message_time.strftime('%Y-%m-%d %H:%M:%S')} ({time_to_sleep} seconds)")
        await asyncio.sleep(time_to_sleep)

        # Send the message in the channel
        for guild in bot.guilds:
            channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
            if channel:
                if next_message_time == good_morning_time:
                    await channel.send("@everyone Good morning, everyone! Have a great day ahead! 🌅")
                elif next_message_time == promotion_time_12pm:
                    embed = discord.Embed(
                        title="What's about DRAXITY?",
                        description=(
                            "💥Step into the ultimate gaming experience with DRAXITY, where the grind never stops! "
                            "From intense battles to epic victories, we've got everything for true gamers like YOU. 💥\n\n"
                            "✨ **What We Offer:**\n"
                            "🎮 Gaming Highlights\n"
                            "🔥 Exciting Content\n"
                            "🌀 Stay Connected with Our Community\n\n"
                            "💡 **Ready to join the fun?** Click below and become a part of the DRAXITY squad now! 👇\n\n"
                            "[**Join DRAXITY**](https://www.youtube.com/@DRAXITY_official)"
                        ),
                        color=0xFF0A01
                    )
                    embed.set_thumbnail(
                        url="https://yt3.ggpht.com/DucAft3ewcWkcpILirmBDUSzvPaEo76jq2fQaUJiSayOKHJajN9-4i-IRPKj_Ivr3UGTGkS3pyQ=s108-c-k-c0x00ffffff-no-rj"
                    )
                    embed.set_image(
                        url="https://yt3.googleusercontent.com/T8mYPeK07QbEKjq6pvG6_5CrFgnmAoI9K59lKqqZZai4pfuAYqlNqoDIVZ-0CJ17ATZugcvAaw=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj"
                    )
                    embed.set_footer(
                        text="YouTube",
                        icon_url="https://www.gstatic.com/youtube/img/branding/favicon/favicon_144x144_v2.png"
                    )
                    await channel.send(embed=embed)
                elif next_message_time == promotion_time_3pm:
                    embed = discord.Embed(
                        title="Don't Miss Out on DRAXITY!",
                        description=(
                            "🚨 It's time for some epic gaming with DRAXITY! We've got all the highlights, action, "
                            "and exciting content just for you! 🚨\n\n"
                            "✨ **What We Offer:**\n"
                            "🎮 Gaming Highlights\n"
                            "🔥 Exciting Content\n"
                            "🌀 Stay Connected with Our Community\n\n"
                            "💡 **Want to join the squad?** Click below and get ready to play! 👇\n\n"
                            "[**Join DRAXITY**](https://www.youtube.com/@DRAXITY_official)"
                        ),
                        color=0xFF0A01
                    )
                    embed.set_thumbnail(
                        url="https://yt3.ggpht.com/DucAft3ewcWkcpILirmBDUSzvPaEo76jq2fQaUJiSayOKHJajN9-4i-IRPKj_Ivr3UGTGkS3pyQ=s108-c-k-c0x00ffffff-no-rj"
                    )
                    embed.set_image(
                        url="https://yt3.googleusercontent.com/T8mYPeK07QbEKjq6pvG6_5CrFgnmAoI9K59lKqqZZai4pfuAYqlNqoDIVZ-0CJ17ATZugcvAaw=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj"
                    )
                    embed.set_footer(
                        text="YouTube",
                        icon_url="https://www.gstatic.com/youtube/img/branding/favicon/favicon_144x144_v2.png"
                    )
                    await channel.send(embed=embed)
                elif next_message_time == promotion_time_7pm:
                    embed = discord.Embed(
                        title="Don't Miss Out on DRAXITY!",
                        description=(
                            "🚨 It's time for some epic gaming with DRAXITY! We've got all the highlights, action, "
                            "and exciting content just for you! 🚨\n\n"
                            "✨ **What We Offer:**\n"
                            "🎮 Gaming Highlights\n"
                            "🔥 Exciting Content\n"
                            "🌀 Stay Connected with Our Community\n\n"
                            "💡 **Want to join the squad?** Click below and get ready to play! 👇\n\n"
                            "[**Join DRAXITY**](https://www.youtube.com/@DRAXITY_official)"
                        ),
                        color=0xFF0A01
                    )
                    embed.set_thumbnail(
                        url="https://yt3.ggpht.com/DucAft3ewcWkcpILirmBDUSzvPaEo76jq2fQaUJiSayOKHJajN9-4i-IRPKj_Ivr3UGTGkS3pyQ=s108-c-k-c0x00ffffff-no-rj"
                    )
                    embed.set_image(
                        url="https://yt3.googleusercontent.com/T8mYPeK07QbEKjq6pvG6_5CrFgnmAoI9K59lKqqZZai4pfuAYqlNqoDIVZ-0CJ17ATZugcvAaw=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj"
                    )
                    embed.set_footer(
                        text="YouTube",
                        icon_url="https://www.gstatic.com/youtube/img/branding/favicon/favicon_144x144_v2.png"
                    )
                    await channel.send(embed=embed)
                elif next_message_time == good_night_time:
                    await channel.send("😴 Good night, everyone! Sleep well and recharge for tomorrow!")
                break
            else:
                print(f"Channel named '{CHANNEL_NAME}' not found in {guild.name}.")

bot.run(BOT_TOKEN)

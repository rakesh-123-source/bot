import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import pytz
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
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} is now online and ready to send scheduled messages!")
    bot.loop.create_task(send_daily_messages())
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if any(mention.id == int(YOUR_USER_ID) for mention in message.mentions):
        user = discord.utils.get(message.guild.members, id=int(YOUR_USER_ID))
        if user and user.status == discord.Status.offline:
            await message.channel.send(f"{message.author.mention}, DRAXITY is offline now! but @DRAXITY will reply whenever he comes online ")
    await bot.process_commands(message)
async def send_daily_messages():
    await bot.wait_until_ready()
    while True:
        timezone = pytz.timezone('Asia/Kolkata')
        now = datetime.now(timezone)
        today = datetime.now(timezone)
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
        promotion_time_11pm = datetime.combine(today, datetime.min.time()) + timedelta(hours=23)
        if now > promotion_time_11pm:
            promotion_time_11pm += timedelta(days=1)
        promotion_time_2am = datetime.combine(today, datetime.min.time()) + timedelta(hours=2)
        if now > promotion_time_2am:
            promotion_time_2am += timedelta(days=1)
        promotion_time_5am = datetime.combine(today, datetime.min.time()) + timedelta(hours=4,minutes=29)
        if now > promotion_time_5am:
            promotion_time_5am += timedelta(days=1)
        good_night_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=23,minutes=30)
        if now > good_night_time:
            good_night_time += timedelta(days=1)
        next_message_time = min(good_morning_time, promotion_time_12pm, promotion_time_3pm, promotion_time_7pm, promotion_time_11pm, good_night_time, promotion_time_2am, promotion_time_5am)
        time_to_sleep = (next_message_time - now).total_seconds()
        print(f"Sleeping until: {next_message_time.strftime('%Y-%m-%d %H:%M:%S')} ({time_to_sleep} seconds)")
        await asyncio.sleep(time_to_sleep)
        for guild in bot.guilds:
            channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
            if channel:
                if next_message_time == good_morning_time:
                    embed = discord.Embed(
                        title="💥Good morning 🌅! ",
                        description=(
                            "What's about DRAXITY?"
                            "Chalore uthjao sab"
                            "🌀 Stay Connected with Our Community\n\n"
                            "[**Join DRAXITY on yt**](https://www.youtube.com/@DRAXITY_official)"
                        ),
                        color=0xFF0A01
                    )
                    embed.set_thumbnail(
                        url="https://cdn.shopify.com/s/files/1/0603/6412/8462/files/Latest-Good-Morning-Images-with-message-wish-for-2023-viraasi_23_600x600.jpg?v=1672140737"
                    )
                    embed.set_image(
                        url="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Z29vZCUyMG1vcm5pbmd8ZW58MHx8MHx8fDA%3D"
                    )
                    embed.set_footer(
                        text="Good Morning",
                        icon_url="https://png.pngtree.com/png-vector/20230414/ourmid/pngtree-sun-orange-three-dimensional-illustration-png-image_6694186.png"
                    )
                    await channel.send(embed=embed)
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
                elif next_message_time == promotion_time_11pm:
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
                elif next_message_time == promotion_time_2am:
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
                elif next_message_time == promotion_time_5am:
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
                    embed = discord.Embed(
                        title="Good Night !",
                        description=(
                            "😴 Good night, @everyone! Sleep well and recharge for tomorrow!"
                            "🌀 Stay Connected with Our Community\n\n"
                            "💡 **Want to join the squad?** 👇\n\n"
                            "[**Join DRAXITY on yt**](https://www.youtube.com/@DRAXITY_official)"
                        ),
                        color=0xFF0A01
                    )
                    embed.set_thumbnail(
                        url="https://goodwishes.com/wp-content/uploads/2024/01/night11.jpg"
                    )
                    embed.set_image(
                        url="https://cdn.pixabay.com/photo/2017/09/22/23/58/roof-windows-2777582_960_720.jpg"
                    )
                    embed.set_footer(
                        text="YouTube",
                        icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEKD_Z4_eu3H284-j27jDXLeeJWVXnddk3RA&s"
                    )
                    await channel.send(embed=embed)
                    break
            else:
                print(f"Channel named '{CHANNEL_NAME}' not found in {guild.name}.")
bot.run(BOT_TOKEN)

import os
import discord
from discord.ext import commands

from PIL import Image, ImageDraw, ImageFont, ImageColor

intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a simple command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

@bot.command()
async def ts(ctx):
  with open('ts.png', "rb") as fh:
    f = discord.File(fh, filename='ts.png')
  await ctx.send(file=f)

@bot.command()
async def make(ctx, *args):
  current = ""
  response = []
  count = 1
  for input in (args):
    if (input == f"text{count}"):
      response.append(current)
      current = ""
      count += 1
    else:
      current += f" {input}"
  if len(current) > 0:
    response.append(current)
  
  formImage(response[0].strip(), response[1:], [[100, 100], [500, 500]], ctx.author)
  with open(f'./memes/{ctx.author}.png', "rb") as fh:
    f = discord.File(fh, filename=f'./memes/{ctx.author}.png')
  await ctx.send(file=f)

def formImage(memename, texts, coordinates, author):
    font = ImageFont.truetype("./CALIBRI.TTF", size=72)
    
    image = Image.open(f"./{memename}.png")

    # creating a draw object
    draw = ImageDraw.Draw(image)

    # adding text to image
    for i in range(0, min(len(coordinates), len(texts))):
        text = texts[i].strip()
        text = texts[i].title()
        draw.text((coordinates[i][0], coordinates[i][1]), text, font=font, fill=(255, 255, 255))


    # image.show()
    image.save(f'./memes/{author}.png')


# Run the bot with your token
bot.run(os.environ['TOKEN'])

# IDK library or something
import os
import discord
import google.generativeai as genai

# Set API keys into variables
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

# Set up the GenAI API client
genai.configure(api_key=GOOGLE_API_KEY)

# List each model that supports generateContent (not necessary actually)
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Set up the Discord client and AI model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# Enable the necessary intents
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
# this is for building context later on
pretext = "You're name is newtella, and you are on a discord server and here are the messages you can see on the server (You do not need to mention about being newtella as this is for your context only, you also do not need to repeat any of the messages or say that you see them as this also for your context): \n"

# if the bot sees it's name is called it will respond
@bot.event
async def on_message(message):
  print(str(message.content))
  if 'newtella' in message.content.lower() and message.author != bot.user:
    # Retrieve the last 15 messages for context
    messages = await message.channel.history(limit=15).flatten()
    # start making context for AI to unda-stand
    context = pretext
    for msg in reversed(messages):    # reverse to maintain chronological order
      context += f'{msg.author.name}: {msg.content}\n'
    # Add the current message to the context
    context += f'{message.author.name}: {message.content}\n'
    print(context)
    response = model.generate_content(context)
    print(response)
    # send the what the AI thinks about you to the channel (probably cringe)
    await message.channel.send(response.text)

# Apparently this shit is required for the bot to work
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# token ni... uhhh... yes
bot.run(DISCORD_TOKEN)

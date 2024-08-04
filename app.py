from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.core import ConversationState, MemoryStorage
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.core import ConversationState, MemoryStorage
from botbuilder.core import TurnContext
from botbuilder.schema import Activity
from bot import AgenteBot
import os

APP_ID = os.getenv("MicrosoftAppId", "")
APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)
memory = MemoryStorage()
conversation_state = ConversationState(memory)
bot = AgenteBot(conversation_state)

async def on_turn(turn_context: TurnContext):
    await bot.on_turn(turn_context)

async def main():
    app = web.Application()
    app.router.add_post("/api/messages", on_turn)
    return app

if __name__ == "__main__":
    web.run_app(main())

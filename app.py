from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext

# Tạo cài đặt cho bot
adapter_settings = BotFrameworkAdapterSettings("", "")
adapter = BotFrameworkAdapter(adapter_settings)

# Logic xử lý của bot
async def echo_activity(turn_context: TurnContext):
    await turn_context.send_activity(f"You said: {turn_context.activity.text}")

# Tạo một HTTP server để lắng nghe các yêu cầu
async def messages(req):
    body = await req.json()
    activity = TurnContext.apply_conversation_reference(
        req.json(), TurnContext.get_conversation_reference(req.json())
    )
    await adapter.process_activity(activity, "", echo_activity)
    return web.Response(status=202)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, port=3978)

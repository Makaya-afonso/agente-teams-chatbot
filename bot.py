from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from conversation_memory import ConversationMemory

class AgenteBot(ActivityHandler):
    def __init__(self, conversation_state):
        self.conversation_state = conversation_state
        self.memory = ConversationMemory()
    
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text.strip()
        user_id = turn_context.activity.from_property.id
        
        # Store the conversation in memory
        self.memory.add_message(user_id, user_message)

        # Provide a response based on the user's message
        response = self.memory.generate_response(user_id, user_message)
        await turn_context.send_activity(MessageFactory.text(response))

    async def on_conversation_update_activity(self, turn_context: TurnContext):
        if turn_context.activity.members_added:
            for member in turn_context.activity.members_added:
                if member.id != turn_context.activity.recipient.id:
                    await turn_context.send_activity(MessageFactory.text("Olá! Eu sou o Agente. Como posso ajudar você hoje?"))

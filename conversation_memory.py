class ConversationMemory:
    def __init__(self):
        self.user_conversations = {}

    def add_message(self, user_id, message):
        if user_id not in self.user_conversations:
            self.user_conversations[user_id] = []
        self.user_conversations[user_id].append(message)

    def generate_response(self, user_id, message):
        if user_id not in self.user_conversations:
            return "Não tenho informações sobre isso ainda."
        
        # Implement a basic keyword matching or other logic to generate responses
        conversation = self.user_conversations[user_id]
        if "como você está" in message.lower():
            return "Estou bem, obrigado por perguntar!"
        
        return "Desculpe, não entendi sua pergunta."

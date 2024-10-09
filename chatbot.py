import random 
class chatbott:
    def __init__(self):
        self.responses = ""
        self.user_input = ""
    # Predefined responses
    responses = {
        "hello": ["Hello!", "Hi there!", "Greetings!"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
        "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
        "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
    }

    # Function to get a response based on user input
    def get_respon(self,user_input):
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        return random.choice(self.responses["default"])
    # Chatbot function
    def chatbot(self):
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            user_input = input("User: ").lower()
            response = chatbott.get_respon(self.user_input)
            
            print("Chatbot:", response)
            
            if user_input == "goodbye":
                break
chatbott()



# import random
# class pas:
#     def __init__(self,lenght):
#         self.lenght =lenght
#         self.char= "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890!@#$%^&*"

#     def gen(self):
#         num_of_char = len(self.char)
#         self.password=""

#         for i in range(self.lenght):
#             rand_index= random.randrange(0,num_of_char)
#             self.password += self.char[rand_index]
#         return  self.password
    
# if __name__ == "__main__":
#     pass_lenght= 8
#     random_pass= pas(pass_lenght) 
#     print(random_pass.gen())


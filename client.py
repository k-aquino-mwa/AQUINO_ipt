import socket #imports the socket module

class GuessingGameClient: #defines a new class
    def __init__(self, host="10.125.9.13", port=7777): #specifies the server address and port
        self.host = host
        self.port = port

    def play(self): #contains the main logic
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            print("Connected to the server. Start guessing!")
            while True: #starts an infinite loop
                guess = input("Enter your guess (1-100): ") #asks the users to guess num from1-100
                client_socket.sendall(guess.encode()) #sends the users guess to the server
                response = client_socket.recv(1024).decode() #waits for the response from the server
                print(response)
                if response == "Correct! You win!":
                    break #breaks the infinite loop if response is "correct..." and ends the game

def main(): #this is for the entry point for the program
    client = GuessingGameClient()
    try:
        client.play() #call the play method on the "client" to start the guessing
    except KeyboardInterrupt: #catches a "KeyboardInterrupt" exception
        print("stopping client")
    finally: #this block ia executed after the try
        pass

if __name__ == "__main__":
    main()

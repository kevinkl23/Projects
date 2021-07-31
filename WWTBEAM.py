# WHO WANTS TO BE A MILLIONAIRE #

class Menu:
    def __init__(self, userName):
        self.userName = userName

    def __repr__(self):
        return self.userName

    def greetings(self):
        print("Welcome To The Game " + self.userName + "!")

class Game:
    user_point = 0
    preview = {}
    def __init__(self):
        return None
    def __repr__(self):
        return "Who Wants To Be A Millionaire"
    def question(self):
        answers = ["The Blue Whale", "France", "1869", "Netherlands", "Mercury"]
        guesses = []
        questions = ["What's the biggest animal in the world?", "Which country is brie cheese originally from?", "What year was Heinz established?", "Who came second in the FIFA Women's World Cup in 2019?", "Which planet is closest to the sun?"]
        
        print("You'll be given 5 random questions.\nFor each correct answer,100 points will be aquired.\nReach for a minimum of 300 points to win the game!\n")
        for question in questions:
            print(question)
            guesses.append(str(input("Enter Answer: ").title()))
        for i in range(0, len(answers), 1):
            if guesses[i] == answers[i]:
                self.user_point += 100
                self.preview[questions[i]] = guesses[i]
            else:
                self.preview[questions[i]] = guesses[i] + " , Answer : " + answers[i]

    def giveresult(self):
        print("Score : " + str(self.user_point))
        if self.user_point >= 300:
            print("Congratulation! You Win!")
        else:
            print("You Lose!")
        print("Preview: " + str(self.preview))

name = input("Enter User Name:")

User = Menu(name)
User.greetings()
User1 = Game()
User1.question()
User1.giveresult()
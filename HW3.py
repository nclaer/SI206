# Your name: Nicole Claerhout
# Your student id: 73974682
# Your email: nclaer@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random

# Create the class Magic_8_Ball
class Magic_8_Ball:
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    def __init__(self, answerlst):
        # it sets this object's answer_list (instance variable) to the passed list of possible answers
        self.answer_list = answerlst
        # it sets this object's question_list (instance variable) to an empty list
        self.question_list = []
        # it sets this object's answer_history_list (instance variable) to an empty list
        self.answer_history_list = []


    # create the __str__ method
    def __str__(self):
        # It should return a string with all the answers in answer_list separated by commas
        # For example : "Yes, No, Not clear"
        string = ""
        for item in self.answer_list:
            if item != self.answer_list[-1]:
                string += item + ", "
            else:
                string += item
        return string


    # create the shake_8_ball method
    def shake_8_ball(self):
        # it randomly picks an answer from the answer_list
        answer = random.choice(self.answer_list)
        # it adds that index to the end of the answer_history_list
        self.answer_history_list.append(self.answer_list.index(answer))
        # it returns the answer at the picked index
        return answer

    # create the check_question method that takes a question
    def check_question(self, question):
        # it checks if the question is in the question_list and if so returns
        #         "I've already answered that question”
        if question in self.question_list:
            return "I've already answered that question"
        # Otherwise it adds the question to the question_list and
        self.question_list.append(question)
        # returns the answer from shake_8_ball
        return self.shake_8_ball()

    # create the print_question_history method
    def print_question_history(self):
        # prints "[answer index] question - answer" for each of the indices in the answer_history_list
        # from the first to the last with each on a separate line.  If there are no items in the
        # answer_history_list it prints "None yet"
        if self.answer_history_list == []:
            print("None yet")
        placeholder = 0
        for item in self.answer_history_list:
            print("[" + str(placeholder) + "]" + " " + self.question_list[placeholder] + " - " + self.answer_list[placeholder])
            placeholder += 1
        # it does not return anything!

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #   a number, n. Ex: 200
    def most_frequent(self, num):
        # it generates a random response n times by calling shake_8_ball
        for i in range(num):
            self.shake_8_ball()
        # It prints the counts for each answer and
        # prints the most frequently occurring answer (Do not use a dictionary in this solution):
        results = []
        counts = []
        for item in self.answer_history_list:
            if item not in results:
                results.append(item)
        for item in results:
            count = self.answer_history_list.count(item)
            counts.append((self.answer_list[item], count))
            print(self.answer_list[item] + ": " + str(count))
        mostfreq = sorted(counts, key = lambda tup: tup[1], reverse = True)[0][0]
        print("The most frequent after " + str(num) + " was " + str(mostfreq))


    #   Yes: 36
    #   No: 36
    #   Ask again: 48
    #   Maybe: 38
    #   Not clear: 47
    #   The most frequent answer after 200 was Not clear

def main():

    # You are welcome to replace the answer_list with your desired answers
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8_Ball(answer_list)

    # get the first question or quit
    inp = input("Ask a question or type quit: ")

    # loop while question is not "quit"
    while inp != "quit":

        # get an answer from check_question
        answer = bot.check_question(inp)

        # print question - answer
        print(inp + " - " + answer)

        # get the next question or quit 
        inp = input("Ask a question or type quit: ")

def test():

    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8_Ball(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_question_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.check_question("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.check_question("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.check_question("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.check_question("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_question_history()
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    print("Testing most_frequent method with 200 responses")
    bot2.most_frequent(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
from time import sleep, time

def welcome():
    print("                         Welcome to...")
    sleep(2)
    print("                       The Guess Game!!!")
    sleep(1)
    print("                                         ")
    print("                                         ")
    print("                       Rules of the game:")
    sleep(2)
    print("                       - Answer the riddles")
    sleep(2)
    print("                       - Try not to make some mistakes")
    sleep(2)
    print("                       - Try to answer the riddles quickly (before 1min)")
    sleep(2)
    ready = input("                   Are you ready???? (yes/no) ")
    if ready.lower() == 'yes':
        print("                           3")
        sleep(2)
        print("                           2")
        sleep(2)
        print("                           1")
        sleep(2)
        print("                           GO")
    elif ready.lower() == 'no':
        print("                       C'mon!")
        return False
    else:
        print("                Sorry but I only understand yes/no")
        return False
    return True

def riddles():
    answers = []
    answers.append(input("Riddle 1: What is always in front of you but can’t be seen? "))
    answers.append(input("Riddle 2: What can you break, even if you never pick it up or touch it? "))
    answers.append(input("Riddle 3: What goes up but never comes down? "))
    answers.append(input("Riddle 4: A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why? "))
    answers.append(input("Riddle 5: I shave every day, but my beard stays the same. What am I? "))
    answers.append(input("Riddle 6: What can’t talk but will reply when spoken to? "))
    answers.append(input("Riddle 7: The more of this there is, the less you see. What is it? "))
    return answers

def chronometer(start_time):
    return time() - start_time

def main():
    if welcome():
        start_time = time()  # Start the timer
        answers = riddles()
        elapsed_time = chronometer(start_time)

        if elapsed_time <= 60:
            print(f"\nYou completed the riddles in {elapsed_time:.2f} seconds!")
        else:
            print("You are too slow!!! It's been more than 1 min")

        correct_answers = [
            "the future", "a promise", "an age", 
            "he was bald", "a barber", "an echo", "darkness"
        ]

        for i, answer in enumerate(answers):
            if answer.lower() == correct_answers[i]:
                print(f"Riddle {i + 1} is correct!")
            else:
                print(f"Riddle {i + 1} is incorrect :c")
                print(f"Your answer: {answer} , The correct answer: {correct_answers[i]}")
            print("                                         ")
            sleep(2)

if __name__ == "__main__":
    main()
import random
import prompt
from brain_games.cli import welcome_user


def start():
    print('Welcome to the Brain Games!')
    user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_response(user)


def is_even(value):
    return (value % 2 == 0)


def check_response(name):
    reference = 3
    counter = 0
    while counter < reference:
        random_count = random.randrange(1000)
        print('Question: ' + str(random_count))
        answer = prompt.string('Your answer: ')
        if (is_even(random_count) and answer == 'yes') or ((is_even(random_count) is False) and answer == 'no'):
            print('Correct!')
            counter += 1
        else:
            print("Let's try again, " + name + '!')
            counter = 0
    print('Congratulations, ' + name + '!')


def main():
    start()


if __name__ == '__main__':
    main()

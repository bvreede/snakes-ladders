import random


def ningago():
    rps = ['rock','paper','sissors']
    choose = random.randint(0,2)
    return rps[choose]

print(ningago())
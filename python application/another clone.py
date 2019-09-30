import random 

inputer = input()

def randomnum(a):
    this = random.randint(1,a,a-1)
    arry = []
    if this > 0:
        arry.append(this)
    elif this == 0:
        while this > 0:
            return inputer

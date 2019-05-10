'''
    Author:  Ethan Pellittiere
    Date:    1/24/19
    Course:  CS310
    Project: HW1
    Purpose: Python Programming Recap
'''


def main():
    """Reads user input, calls appropriate function"""
    user_in = input("Select problem to run (1-4), 0 to exit ")
    if user_in == "1":
        req1()
    elif user_in == "2":
        num = []
        while 1:
            x = input("Enter numbers, no input to finish: ")
            if x == "":
                break
            num.append(int(x))
        print(req2(num))
    elif user_in == "3":
        num = []
        while 1:
            x = input("Enter numbers, no input to finish: ")
            if x == "":
                break
            num.append(int(x))
        print(req3(num))
    elif user_in == "4":
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))
        print("Hamming distance: " + str(req4(x, y)))
    else:
        input("Invalid Input")


def req1():
    """Reads user input, prints output in reverse order, ends when EOF is read"""
    data = []
    print("Enter Values, use CTRL-D or CTRL-Z to indicate EOF")
    try:
        while 1:
            data.append(input())
    except EOFError:
        pass
    for x in range(len(data)-1, -1, -1):
        print(data[x])


def req2(num):
    """Inputs a sequence of integer values, returns True if there exists a pair of numbers
    that when multiplied are odd"""
    for x in range(0, len(num)):
        for y in range(x+1, len(num)):
            if num[x] * num[y] % 2 == 1:
                return True
    return False


def req3(num):
    """Inputs a collection of integers, returns a collection of all possible permutations
    calls perm(num, x) recursively"""
    tmp = num
    listOut = []
    for x in range(0, len(tmp)):
        tmp = num
        t = tmp[0]
        tmp[0] = tmp[x]
        tmp[x] = t
        listOut.append(perm(tmp, 1))
    return listOut


def perm(num, x):
    """Recursive helper function to req3, input is a collection of values and an int
    returns collection after being arranged into a possible permutation"""
    if x == len(num)-1:
        return num
    for y in range(x, len(num)):
        t = num[x]
        num[x] = num[y]
        num[y] = t
        perm(num, x+1)


def req4(x, y):
    """Returns Hamming Distance of two integers. Converts them to a binary string and compared for
    different bits"""
    binX=""
    binY=""
    out=0
    while x > 0 or y > 0:
        if x > 0:
            binX= str(x%2) + binX
            x = int(x/2)
        else:
            binX = "0" + binX
        if y > 0:
            binY = str(y%2) + binY
            y = int(y/2)
        else:
            binY = "0" + binY
    for x in range(0, len(binX)):
        if binX[x] != binY[x]:
            out += 1
    return out


main()

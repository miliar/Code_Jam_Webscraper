def write(case, number):
    f = open("output.txt", "a")
    line = "Case #" + str(number) + ": " + str(case) + "\n"
    f.write(line)
    f.close()

def load():
    f = open("B-small-attempt0.in", "r")
    cases = f.readline()

    for i in range(int(cases)):
        case = f.readline().rstrip('\n').split(" ")
        cookie(float(case[0]), float(case[1]), float(case[2]), 2, 0, i + 1)
    f.close()

def cookie(C, F, X, production, case):
    seconds = 0
    run = True
    while run:
        if (X-C)/production < X/(production + F):
            seconds += X/production
            seconds = round(seconds, 7)
            print(seconds)
            run = False
        else:
            seconds += C/production
            production = production + F

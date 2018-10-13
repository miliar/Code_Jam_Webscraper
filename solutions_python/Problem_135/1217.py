import sys

T = int(sys.stdin.readline())
for testcase in range(T):
    answer1 = int(sys.stdin.readline())
    for i in range(4):
        a = sys.stdin.readline()
        if i == answer1 - 1:
            card = map(int, a.split())
    answer2 = int(sys.stdin.readline())
    for i in range(4):
        b = sys.stdin.readline()
        if i == answer2 - 1:
            card2 = map(int, b.split())
    choices = set(card).intersection(set(card2))
    if len(choices) == 1:
        result = str(list(choices)[0])
    elif len(choices) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad Magician!"
    print "Case #" + str(testcase + 1) + ": " + result



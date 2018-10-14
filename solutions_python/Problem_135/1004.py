import fileinput

inp = fileinput.input()

T = int(inp.readline())

for t in range(1,T+1):
    first_answer = int(inp.readline())
    possibles = set()
    for i in range(1,5):
        line = inp.readline()
        if i == first_answer:
            possibles = set(int(x) for x in line.split())
    second_answer = int(inp.readline())
    for i in range(1,5):
        line = inp.readline()
        if i == second_answer:
            possibles &= set(int(x) for x in line.split())

    if len(possibles) == 0:
        print("Case #{}: Volunteer cheated!".format(t))
    elif len(possibles) > 1:
        print("Case #{}: Bad magician!".format(t))
    else:
        print("Case #{}: {}".format(t, possibles.pop()))
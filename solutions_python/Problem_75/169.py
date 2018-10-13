from sys import stdin
input = stdin.read().split()
inputs = 0

def next():
    global input, inputs
    ans = input[inputs]
    inputs += 1
    return ans

T = int(next())
for t in range(1,T+1):
    C = int(next())
    good = []
    for c in range(C): good.append(next())
    D = int(next())
    bad = []
    for d in range(D): bad.append(next())
    N = int(next())
    data = next()

    evolve = {}
    for item in good:
        evolve[ (item[0],item[1]) ] = item[2]
        evolve[ (item[1],item[0]) ] = item[2]

    erase = {}
    for item in bad:
        erase[ (item[0],item[1]) ] = 1
        erase[ (item[1],item[0]) ] = 1

    answer = []
    for x in data:
        if len(answer)==0:
            answer.append(x)
        else:
            answer.append(x)
            while (len(answer)>1) and ((answer[-1],answer[-2]) in evolve):
                y = evolve[ (answer[-1],answer[-2]) ]
                answer.pop()
                answer.pop()
                answer.append(y)
            for i in range(len(answer)-1):
                if (answer[i],answer[-1]) in erase:
                    answer = []
                    break

    print ( "Case #%d:" % t ), repr(answer).replace("'","")

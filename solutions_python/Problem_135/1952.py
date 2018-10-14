for t in range(1, int(raw_input()) + 1):
    x = int(raw_input())
    S1 = set([[int(z) for z in raw_input().split()] for y in range(4)][x-1])
    x = int(raw_input())
    S2 = set([[int(z) for z in raw_input().split()] for y in range(4)][x-1])
    S = S1 & S2
    if len(S) == 0:
        message = "Volunteer cheated!"
    elif len(S) == 1:
        message = S.pop()
    else:
        message = "Bad magician!"
    print "Case #{}: {}".format(t, message)

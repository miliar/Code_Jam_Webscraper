T = int(input())
for i in range(T):
    out = {k for k in range(1, 17)}
    for l in range(2):
        a = int(input()) - 1
        for j in range(4):
            line = {int(w) for w in input().split(' ')}
            if j == a:
                out &= line
    message = ""
    if len(out) == 0:
        message = "Volunteer cheated!"
    elif len(out) > 1:
        message = "Bad magician!"
    else:
        message = str(next(iter(out)))
    print("Case #{}: {}".format(i+1, message))


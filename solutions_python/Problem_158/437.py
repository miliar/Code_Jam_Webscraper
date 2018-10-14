#Written by Raynger


def s1(r, c):
    return True

def s2(r, c):
    return (r*c) % 2 == 0

def s3(r, c):
    if (r * c) % 3 != 0 or (r * c) == 3:
        return False
    else:
        return True

def s4(r, c):
    return (r == 4 and c == 4) or (r * c) == 12

cases = int(input())
for c in range(cases):
    line = input().split()
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])
    flag = False
    if X == 1:
        flag = s1(R, C)
    elif X == 2:
        flag = s2(R, C)
    elif X == 3:
        flag = s3(R, C)
    else:
        flag = s4(R, C)
    if flag:
        output = "GABRIEL"
    else:
        output = "RICHARD"
    #print(X, R, C)
    print("Case #{}: {}".format(c+1, output))
    #print()
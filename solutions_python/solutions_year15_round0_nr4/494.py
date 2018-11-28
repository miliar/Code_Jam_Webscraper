import sys

def log(*args, sep=" ", end="\n", file= sys.stderr, flush= False):
    file.write(sep.join(str(a) for a in args) + end)
    if flush:
        file.flush()

def getWinner(x, r, c):
    if x == 1:
        return "GABRIEL"
    elif (c * r) % x != 0:
        return "RICHARD"
    elif x == 2:
        return "GABRIEL"
    elif r == 1 or c == 1:
        return "RICHARD"
    elif x == 3:
        return "GABRIEL"
    elif c == 2 or r == 2:
        return "RICHARD"
    else:
        return "GABRIEL"
    

if __name__ == "__main__":
    nCases= int(input())
    for iCase in range(1, nCases + 1):
        x, r, c= map(int, input().split())
        
        winner= getWinner(x, r, c)

        print("Case #{:d}: {:s}".format(iCase, winner))
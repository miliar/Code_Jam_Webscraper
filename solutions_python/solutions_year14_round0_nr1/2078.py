from sys import stdin, stdout

def compute():
    ans = None
    possibilities = set()

    rowChoice = int(stdin.readline())
    for r in range(1,4+1):
        if r == rowChoice:
            for num in map(int, stdin.readline().split(" ")):
                possibilities.add(num)
        else:
            stdin.readline()

    rowChoice = int(stdin.readline())
    for r in range(1,4+1):
        if r == rowChoice:
            for num in map(int, stdin.readline().split(" ")):
                if num in possibilities:
                    if not ans:
                        ans = str(num)
                    else:
                        ans = "Bad magician!"
        else:
            stdin.readline()

    if ans:
        return ans
    else:
        return "Volunteer cheated!"


T = int(stdin.readline())
for t in range(T):
    ans = compute()

    stdout.write("Case #%d: %s\n"%(t+1, ans))



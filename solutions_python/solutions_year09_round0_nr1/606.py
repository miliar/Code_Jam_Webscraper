
from __future__ import print_function

word = set()
case = []

if __name__ == "__main__":
    
    inf = open("A-large.in", "r")
    outf = open("A-large.out", "w")

    # Read info
    L, D, N = inf.readline().split()
    L, D, N = int(L), int(D), int(N)

    # Read words
    for d in range(D):
        word.add(inf.readline().strip())

    # Read cases
    for c in range(N):
        text = inf.readline().strip()
        part = []
        group = ""
        inGroup = False
        for char in text:
            if char == "(":
                group = ""
                inGroup = True
            elif char == ")":
                part.append(group)
                inGroup = False
            elif inGroup:
                group += char
            else:
                part.append(char)
        case.append(part)

    print(word)
    print(case)
    
    for n, c in enumerate(case):
        count = 0
        for w in word:
            for i in range(L):
                if w[i] not in c[i]:
                    break
            else:
                count += 1
        print("Case #", n + 1, ": ", count, sep="")
        print("Case #", n + 1, ": ", count, sep="", file=outf)

    inf.close()
    outf.close()

import fileinput


def solve(s):
    tidy = 0
    s = list(s)
    if s[len(s)-1] is '\n':
        s.pop()
    while not tidy:
        tidy = 1
        for i in range(0, len(s)-1):
            if int(s[i]) > int(s[i+1]):
                tidy = 0
                s[i] = str(int(s[i])-1)
                for j in range(i+1, len(s)):
                    s[j] = str(9)
                break


# remove start zeros
    while '0' in s[0]:
        del s[0]
    return "".join(s)

reader = fileinput.input()
t = int(reader.readline())
for i in range(1, t+1):
    s = reader.readline()
    print("Case #{}: {}".format(i, solve(s)))



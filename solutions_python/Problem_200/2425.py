
def last_tidy(t):
    s = str(t)
    l = len(s)
    m = list(map(int, s))

    for i in range(l - 2, -1, -1):
        if m[i] > m[i + 1]:
            m[i] -= 1
            for j in range(i + 1, l):
                m[j] = 9

    return ''.join(str(x) for x in filter((0).__ne__, m))

# run the program
test_cases = int(input())
cases = []
for i in range(test_cases):
    cases.append(int(input()))

for i in range(test_cases):
    print("Case #" + str(i + 1) + ": " + last_tidy(cases[i]))

import pdb

def flip(p, k):
    d = []
    length = len(p)
    sum = 0

    for c in p:
        if c == '+':
            d.append(True)
        else:
            d.append(False)

    for i in range(length - k + 1):
        if d[i] == False:
            sum += 1
            for j in range(i, i + k):
                    d[j] = not d[j]

#    print(d)
    for i in d:
        if i == False:
            return 'IMPOSSIBLE'

    return str(sum)

# run the program
test_cases = int(input())
cases = []
for i in range(test_cases):
    cases.append(list(input().split()))

for i in range(test_cases):
    pancake = cases[i][0]
    k = cases[i][1]
    print("Case #" + str(i + 1) + ": " + flip(pancake, int(k)))


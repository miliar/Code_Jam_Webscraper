#import random
f = open("A-large.in.txt", "r")

t = 0
cases = []
ks = []

for line in f:
    if t == 0:
        t = int(line)
    else:
        data = line.split()

        case = [(0 if i == "-" else 1) for i in data[0]]
        ks.append(int(data[1]))
        cases.append(case)


f.close()

'''
cases.append([0,0,0,1,1])
ks.append(3)

# Test randoms
for _ in range(100):
    new = [random.randint(0,1) for i in range(10)]
    cases.append(new)
    ks.append(random.randint(2,10))
'''

out = open("flip.txt", "w")

for c in range(len(ks)):

    case = cases[c]
    orig = [i for i in case]
    k = ks[c]
    ans = 0
    for i in range(0, len(case) - k + 1):

        if case[i] == 0:
            
            # Flip k
            ans += 1
            for j in range(i, i+k):
                case[j] = (case[j] + 1) % 2

    for i in range(0,k):
        if case[len(case)-i-1] == 0:
            ans = "IMPOSSIBLE"
            break

    #print(orig, k, ans)
    out.write("Case #" + str(c+1) + ": " + str(ans) + "\n")


out.close()

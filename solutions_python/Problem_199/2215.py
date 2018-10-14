def flip(x):
    if x == '+':
        return '-'
    if x == '-':
        return '+'


t = input()
t = int(t)
for i in range(0, t):
    entry = input()
    entry = entry.split()
    p = entry[0]
    p = list(p)
    k = int(entry[1])
    x = 0
    counter = 0
    imp = 0
    while x < len(p):
        if p[x] == '-' and x + k <= len(p):
            for flip_n in range(0, k):
                p[x + flip_n] = flip(p[x + flip_n])
            counter += 1
        if '-' in p and x + k > len(p):
            print("Case #" + str(i + 1) + ": IMPOSSIBLE")
            imp = 1
            break
        x += 1

    if imp == 0:
        print("Case #" + str(i + 1) + ": " + str(counter))

test = int(input())
# test = 1
z = 0
for i in range(test):
    z += 1
    ip1, ip2 = input().split(" ")
    ip2 = int(ip2)
    # ip1 = "+-+-+-+-+"
    # ip2 = 3
    pcakes = list(str(ip1))
    lcakes = len(pcakes)
    flips = ip2
    plus = 0
    minus = 0
    aplus = 0
    aminus = 0
    result = 0
    start = 0
    counter = 0
    string = str()
    for i in pcakes:
        if i == '+':
            plus += 1
        else:
            minus += 1

    for i in range(start, lcakes):
        if pcakes[i] == '-' and (i + flips) <= lcakes:
            result += 1
            pcakes[i] = '+'
            for j in range(i + 1, i + flips):
                if pcakes[j] == '+':
                    pcakes[j] = '-'
                else:
                    pcakes[j] = '+'
            start = i + 1
            continue
    for i in range(lcakes):
        if pcakes[i] == "-":
            result = "IMPOSSIBLE"
    print("Case #" + str(z) + ':', result)

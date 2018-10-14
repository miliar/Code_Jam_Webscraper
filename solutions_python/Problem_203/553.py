t = int(raw_input())

currCase = 1;
while currCase <= t:
    r, c = [int(s) for s in raw_input().split(" ")]

    print "Case #{}:".format(currCase)

    cake = [[str(i) for i in str(raw_input())] for y in range(r)]

    for j in range(r):
        for k in range(c):
            if cake[j][k] != '?':
                p = k + 1
                while p < c:
                    if cake[j][p] == '?':
                        cake[j][p] = cake[j][k]
                    else:
                        break;
                    p+=1

                q = k - 1;
                while q >= 0:
                    if cake[j][q] == '?':
                        cake[j][q] = cake[j][k]
                    else:
                        break;
                    q-=1

    for j in range(r - 1):
        for k in range(c):
            if cake[j][k] != '?' and cake[j+1][k] == '?':
                cake[j+1][k] = cake[j][k]


    for j in range(r - 1, 0, -1):
        for k in range(c):
            if cake[j][k] != '?' and cake[j-1][k] == '?':
                cake[j-1][k] = cake[j][k]

    for j in range(r):
        print "".join(cake[j])

    currCase+=1;

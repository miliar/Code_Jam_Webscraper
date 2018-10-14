import re

def calc(h, w, a):
    l = [[i + j * W for i in range(W)] for j in range(H)]
    r = [['-' for i in range(W)] for j in range(H)]

    Loop = True
    while Loop:
        Loop = False
        for j in range(H):
            for i in range(W):
                e = [10001 for k in range(4)]
                if               j > 0:     e[0] = a[j - 1][i    ]
                if i > 0                  : e[1] = a[j    ][i - 1]
                if i < W - 1              : e[2] = a[j    ][i + 1]
                if               j < H - 1: e[3] = a[j + 1][i    ]

                min = a[j][i]
                dir = -1
                for k in range(4):
                    if min > e[k]:
                        dir = k
                        min = e[k]

                if dir == 0 and e[dir] < 1001:
                    if l[j][i] < l[j - 1][i    ]:
                        Loop = True
                        l[j - 1][i    ] = l[j][i]
                    elif l[j][i] > l[j - 1][i    ]:
                        Loop = True
                        l[j][i] = l[j - 1][i    ]
                elif dir == 1 and e[dir] < 1001:
                    if l[j][i] < l[j    ][i - 1]:
                        Loop = True
                        l[j    ][i - 1] = l[j][i]
                    elif l[j][i] > l[j    ][i - 1]:
                        Loop = True
                        l[j][i] = l[j    ][i - 1]
                elif dir == 2 and e[dir] < 1001:
                    if l[j][i] < l[j    ][i + 1]:
                        Loop = True
                        l[j    ][i + 1] = l[j][i]
                    elif l[j][i] > l[j    ][i + 1]:
                        Loop = True
                        l[j][i] = l[j    ][i + 1]
                elif dir == 3 and e[dir] < 1001:
                    if l[j][i] < l[j + 1][i    ]:
                        Loop = True
                        l[j + 1][i    ] = l[j][i]
                    elif l[j][i] > l[j + 1][i    ]:
                        Loop = True
                        l[j][i] = l[j + 1][i    ]

    al = 0

    for j in range(H):
        for i in range(W):
            if r[j][i] == '-':
                for j2 in range(H):
                    for i2 in range(W):
                        if l[j][i] == l[j2][i2]:
                            r[j2][i2] = chr(al + 97)
                al += 1
    return r



state = 0
Case = 0
for line in open('B-small-attempt2.in', 'r'):
#for line in open('B-test', 'r'):
    while True:
        if state == 0:
            N = int(line[:-1])
            state = 1
            break
        elif state == 1:
            if N == 0: break
            N -= 1

            r = re.compile("^([0-9]+) ([0-9]+)$")
            m = r.search(line[:-1])
            H = int(m.group(1))
            W = int(m.group(2))

            state = 2
            Atr = []
            r = re.compile("^([0-9]+)"+ " ([0-9]+)" * (W - 1) + "$")
            h = 0
            break
        elif state == 2:
            if len(Atr) == H:
                state = 3
                continue
            m = r.search(line[:-1])
            Atr.append([int(m.group(i + 1)) for i in range(W)])
            break
        elif state == 3:
            r = calc(H, W, Atr)
            Case += 1
            print "Case #"+str(Case)+":"
            for j in range(H):
                ln = r[j][0]
                for i in range(1, W):
                    ln += " "+r[j][i]
                print ln
            del Atr
            state = 1
            continue
            break

r = calc(H, W, Atr)
Case += 1
print "Case #"+str(Case)+":"
for j in range(H):
    ln = r[j][0]
    for i in range(1, W):
        ln += " "+r[j][i]
    print ln


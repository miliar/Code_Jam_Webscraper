#!/usr/bin/env python3

T = int(input())

for case in range(1, T + 1):
    rc = input().strip().split(" ")
    r = int(rc[0])
    c = int(rc[1])
    lines = []
    for _ in range(r):
        line = list(input())
        lines.append(line)
    expanded = set()
    for i in range(r):
        for j in range(c):
            if lines[i][j] not in expanded:
                expanding = True
                ip1 = i
                ip2 = i + 1
                jp1 = j
                jp2 = j + 1
                while expanding:
                    expanding = False
                    if ip1 > 0 and \
                            all(lines[ip1 - 1][x] == "?" for x in range(jp1, jp2)):
                        expanding = True
                        ip1 -= 1
                    if ip2 < r and \
                            all(lines[ip2][x] == "?" for x in range(jp1, jp2)):
                        expanding = True
                        ip2 += 1

                    if jp1 > 0 and \
                            all(lines[x][jp1 - 1] == "?" for x in range(ip1, ip2)):
                        expanding = True
                        jp1 -= 1
                    if jp2 < c and \
                            all(lines[x][jp2] == "?" for x in range(ip1, ip2)):
                        expanding = True
                        jp2 += 1
                for x in range(ip1, ip2):
                    for y in range(jp1, jp2):
                        lines[x][y] = lines[i][j]
                expanded.add(lines[i][j])
    print("Case #{}:".format(case))
    for line in lines:
        print("".join(line))

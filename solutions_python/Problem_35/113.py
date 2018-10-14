#!/usr/bin/env python

def solve(input):
    h = len(input)
    w = len(input[0])

    graph = [[[] for _ in range(w)] for _ in range(h)]
    result = [['' for _ in range(w)] for _ in range(h)]

    for row in input:
        row.append(1000000)
    input.append([1000000 for _ in range(len(input[0]))])

    nwse = ((0, -1), (-1, 0), (1, 0), (0, 1))
    for y in range(h):
        for x in range(w):
            p = min(input[y+dy][x+dx] for dx, dy in nwse)
            if p < input[y][x]:
                for dx, dy in nwse:
                    if input[y+dy][x+dx] == p:
                        graph[y][x].append((y+dy,x+dx))
                        graph[y+dy][x+dx].append((y,x))
                        break

    num = 97
    for y in range(h):
        for x in range(w):
            if result[y][x] == '':
                letter = chr(num)
                stack = [(y,x)]
                while stack:
                    p, q = stack.pop()
                    result[p][q] = letter
                    stack.extend((a,b) for a,b in graph[p][q] if result[a][b] == '')
                num += 1

    return '\n'.join(' '.join(row) for row in result)

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        H, W = map(int, raw_input().split())
        print "Case #%d:" % (i+1)
        print solve([map(int, raw_input().split()) for _ in range(H)])

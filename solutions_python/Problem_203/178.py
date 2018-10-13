import sys

def solve():
    R, C = map(int, sys.stdin.readline().rstrip().split())

    cake_map = {}

    cake = []
    for row_num in range(R):
        row = list(sys.stdin.readline().rstrip())
        cake.append(row)

        for col_num, char in enumerate(row):
            if char == '?':
                continue

            if char not in cake_map:
                cake_map[char] = (col_num, col_num, row_num, row_num)

            cake_char = cake_map.get(char)
            best_left = min(col_num, cake_char[0])
            best_right = max(col_num, cake_char[1])
            best_down = max(row_num, cake_char[3])

            cake_map[char] = (best_left, best_right, cake_char[2], best_down)

    for char in cake_map:
        vals = cake_map[char]
        for row_num in range(vals[2], vals[3]+1):
            for col_num in range(vals[0], vals[1]+1):
                cake[row_num][col_num] = char

    #for row in cake:
    #    print ''.join(row)

    #print cake_map
    while True:
        # Floodfill in all directions and hope for the best

        did_fill = False
        for char in cake_map:
            # Can we FF up?
            l, r, u, d = cake_map[char]
            if u > 0:
                for col in range(l, r+1):
                    if cake[u-1][col] != '?':
                        break
                else:
                    for col in range(l, r+1):
                        cake[u-1][col] = char
                    did_fill = True
                    cake_map[char] = (l, r, u-1, d)
                    l, r, u, d = cake_map[char]

            # Can we FF down?
            if d < R-1:
                for col in range(l, r+1):
                    if cake[d+1][col] != '?':
                        break
                else:
                    for col in range(l, r+1):
                        cake[d+1][col] = char
                    did_fill = True
                    cake_map[char] = (l, r, u, d+1)
                    l, r, u, d = cake_map[char]

            # Can we FF left?
            if l > 0:
                for row in range(u, d+1):
                    if cake[row][l-1] != '?':
                        break
                else:
                    for row in range(u, d+1):
                        cake[row][l-1] = char
                    did_fill = True
                    cake_map[char] = (l-1, r, u, d)
                    l, r, u, d = cake_map[char]

            # Can we FF right?
            if r < C-1:
                for row in range(u, d+1):
                    if cake[row][r+1] != '?':
                        break
                else:
                    for row in range(u, d+1):
                        cake[row][r+1] = char
                    did_fill = True
                    cake_map[char] = (l, r+1, u, d)
                    l, r, u, d = cake_map[char]

        if not did_fill:
            break

    #print cake_map

    for row in cake:
        print ''.join(row)



def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        print 'Case #{}:'.format(t)
        answer = solve()

if __name__ == "__main__":
    main()

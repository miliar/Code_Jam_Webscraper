def calc(in_file):
    R,C = map(int, in_file.readline().split())
    grid = []
    for _ in range(R):
        tmp = in_file.readline()
        grid.append(tmp)

    total_move_row = [0]*R
    total_move_col = [0]*C
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '.':
                total_move_row[r] += 1
                total_move_col[c] += 1
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.': continue

            is_safe = False
            if grid[r][c] =='^':
                is_safe = False
                for i in range(r-1, -1, -1):
                    if grid[i][c] != '.':
                        is_safe = True
                        break

            elif grid[r][c] =='>':
                is_safe = False
                for i in range(c+1, C):
                    if grid[r][i] != '.':
                        is_safe = True
                        break

            elif grid[r][c] =='<':
                for i in range(c-1, -1, -1):
                    if grid[r][i] != '.':
                        is_safe = True
                        break

            else:
                for i in range(r+1, R):
                    if grid[i][c] != '.':
                        is_safe = True
                        break
            if is_safe: continue
            if total_move_row[r] > 1 or total_move_col[c] > 1:
                ans += 1
            else: return "IMPOSSIBLE"
    return ans

if __name__ == '__main__':
    in_file = open("input.txt")
    ou_file = open("output.txt", 'w')
    T = int(in_file.readline())
    for t in range(T):
        ans = calc(in_file)
        ou_file.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    ou_file.close()
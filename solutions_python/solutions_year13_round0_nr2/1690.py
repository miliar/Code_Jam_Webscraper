def main():
    def mowe_row(x,n):
        for i in range(M):
            if poss_grid[x][i] > n:
                poss_grid[x][i] = n
    def mowe_col(y,n):
        for i in range(len(grid)):
            if poss_grid[i][y] > n:
                poss_grid[i][y] = n
    no_test_cases = int(input())
    for test_case in range(1,no_test_cases+1):
        N, M = input().split()
        N, M = int(N), int(M)
        grid = []
        poss_grid = []
        grid_str = ''
        highest = 0
        highest_loc = (0,0)
        do_able = False
        for row in range(N):
            cur_int = []
            str_in = input()
            grid_str += str_in
            cur = str_in.split()
            for i in range(M):
                val = int(cur[i])
                if val > highest:
                    highest = val
                    highest_loc = (row,i)
                cur_int.append(val)
            grid.append(cur_int)
        # Initialising possible grid
        poss_grid = [[highest for col in range(M)] for row in range(N)]
        # Real Checks..
        if grid_str.count(grid_str[0]) == len(grid_str):
            do_able = True
        else:
            # Construct own grid
            for k in range(N):
                mowe_row(k, grid[k][highest_loc[1]])
            for l in range(M):
                mowe_col(l, grid[highest_loc[0]][l])
            if grid == poss_grid:
                do_able = True
        if do_able:
            yes = 'YES'
        else:
            yes = 'NO'
        print('Case #'+str(test_case)+': '+yes+chr(10))
 
if __name__ == '__main__':
    main()
def main():
    def mowe_row(x,n):
        for i in range(M):
            if poss_grid[x][i] > n:
                poss_grid[x][i] = n
    def mowe_col(y,n):
        for i in range(len(grid)):
            if poss_grid[i][y] > n:
                poss_grid[i][y] = n
    f = open('G:/Study/Programming/Code Jam/2013/B-large.in', 'r')
    #f = open('G:/Study/Programming/Code Jam/trial.txt', 'r')
    g = open('G:/Study/Programming/Code Jam/2013/output2_large.txt', 'w')
    #g = open('G:/Study/Programming/Code Jam/output_trial.txt', 'w')
    no_test_cases = int(f.readline())
    for test_case in range(1,no_test_cases+1):
        N, M = f.readline().split()
        N, M = int(N), int(M)
        grid = []
        poss_grid = []
        grid_str = ''
        highest = 0
        highest_loc = (0,0)
        do_able = False
        for row in range(N):
            cur_int = []
            str_in = f.readline()
            grid_str += str_in
            cur = str_in.split()
            for i in range(M):
                fuck = int(cur[i])
                if fuck > highest:
                    highest = fuck
                    highest_loc = (row,i)
                cur_int.append(fuck)
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
        g.writelines('Case #'+str(test_case)+': '+yes+chr(10))

if __name__ == '__main__':
    main()

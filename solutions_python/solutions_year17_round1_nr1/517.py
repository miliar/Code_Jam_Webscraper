
import sys


def read_grid( rfile, R, C ):
    grid=[]
    for i in range(R):
        line = rfile.readline()
        if line[-1]== '\n':
            grid.append(list(line[:-1]))
        else:
            grid.append(list(line))
    return grid

def fill_left( grid , r, c, curr_intial):
    r_i, c_i = r, c
    while c_i >= 0 and grid[r_i][c_i] == '?':
        grid[r_i][c_i] = curr_intial
        c_i -= 1

def fill_right( grid , r, c, curr_intial):
    r_i, c_i = r, c
    while c_i < len(grid[0]) and grid[r_i][c_i] == '?':
        grid[r_i][c_i] = curr_intial
        c_i +=1
    return c_i

def  replicate_row_below( grid,r ):
    if r > 0 and grid[r - 1][0] == '?' and grid[r][0] != '?':
        for c in range( len(grid[0]) ):
            grid[r-1][c] = grid[r][c]
        replicate_row_below(grid, r - 1)

def  replicate_row_above( grid,r ):
    if r > 0 and grid[r][0] == '?' and grid[r-1][0] != '?':
        for c in range( len(grid[0]) ):
            grid[r][c] = grid[r-1][c]
        replicate_row_below(grid, r - 1)

def to_str( grid):

    my_str =''
    for r in range(len(grid)):
        my_str.join(grid[r])
    return my_str
def main( file_name ):
    rfile = open(file_name,"r")
    wfile =  open(file_name.split('.')[0]+"-out.txt","w+")

    T = int (rfile.readline()[:-1])
    for test_no in range(T):
        line = rfile.readline()
        R,C= int(line[:-1].split(' ')[0]), int(line[:-1].split(' ')[1])
        grid = read_grid(rfile, R, C)
        for r in range(R):
            c=0
            while c < C:
                curr_intial = grid[r][c]
                if curr_intial != '?':
                    fill_left(grid, r, c-1, curr_intial)
                    c=fill_right(grid, r, c+1, curr_intial)
                else:
                    c +=1
            replicate_row_above(grid, r)
            replicate_row_below(grid,r)

            r +=1
        assignment = '\n'.join( ''.join(mylist) for mylist in grid)
        print 'case '+str(test_no)+"\n"+assignment
        wfile.write("Case #%d:\n"%(test_no+1))
        if( test_no < T-1):
            wfile.write(assignment+"\n")
        else:
            wfile.write(assignment)
    rfile.close()
    wfile.close()



if __name__ == "__main__":
    main(sys.argv[1])
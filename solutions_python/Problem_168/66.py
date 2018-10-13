input_file = "sample_input.txt"
input_file = "A-small-attempt0.in"
##input_file = "B-small-attempt2.in"
input_file = "A-large.in"

from multiprocessing import Pool
from itertools import izip

def line(f,_type=str):
    s = [_type(i) for i in f.readline().strip().split()]
    return s

def f_star(args):
    return f(*args)

# solution function
def f(grid):
    r = len(grid)
    c = len(grid[0])
    answer = 0
    for i,row in enumerate(grid):
        for j, arrow in enumerate(row):
            if arrow == '.':
                continue
            else:
                up = False
                down = False
                left = False
                right = False
                for k in xrange(0,i):
                    if grid[k][j] != '.':
                        up = True
                for k in xrange(i+1,r):
                    if grid[k][j] != '.':
                        down = True
                for k in xrange(0,j):
                    if grid[i][k] != '.':
                        left = True
                for k in xrange(j+1,c):
                    if grid[i][k] != '.':
                        right = True
                if not up and not down and not left and not right:
                    return 'IMPOSSIBLE'
                else:
                    if arrow == '^':
                        answer += int(not up)
                    if arrow == 'v':
                        answer += int(not down)
                    if arrow == '<':
                        answer += int(not left)
                    if arrow == '>':
                        answer += int(not right)
    return str(answer)
            
        
            
                
    

if __name__ == "__main__":
    # read inputs
    with open(input_file) as fin:
        T = line(fin,int)[0]

        args = []
        for case in range(1,T+1):
            r,c = line(fin,int)
            grid = []
            for i in xrange(r):
                grid.append(list(line(fin)[0]))
            args.append(grid)

    # calculate answers
    answers = map(f,args)

    # print answers
    with open('output_mp.txt','w') as fout:
        for i in range(len(answers)):
            case = i + 1
            answer = answers[i]
            s = "Case #%d: %s\n" % (case, answer)   # change answer format if necessary
            print s,
            fout.write(s)

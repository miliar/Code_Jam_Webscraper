import sys

grid = []
ans = []

def buildGrid(R,C):
    global grid, ans
    ans = grid[:]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.':
                if ans[r][c] in ('/','\\'):
                    ans = 'Impossible'
                    return
                else:
                    ans[r][c] = '.'
            
            if grid[r][c] == '#':
                if ans[r][c] in ('/','\\'):
                    pass
                elif ans[r][c] == '#':
                    ans[r][c] = '/'
                    try:
                        ans[r][c] = '/'
                        ans[r+1][c] = '\\'
                        ans[r][c+1] = '\\'
                        ans[r+1][c+1] = '/'
                    except:
                        ans = 'Impossible'
                        return
        

def main():
    global grid, ans
    infile = open('A-small.in', 'r');
    cases = int(infile.readline());
    f = open('A-small.out', 'w')
    for case in range(1, cases+1):
        ans = []
        line = infile.readline().strip().split();
        
        R, C = int(line[0]), int(line[1])
        grid = []
        
        gotAns = False
        
        for r in range(0,R):
            line = infile.readline().strip();
            grid.append([c for c in line])
            if line.count('#') % 2 == 1:
                gotAns = True
                
        if gotAns:
            ans = 'Impossible'
            s = "Case #%d:\n" % (case)
            s += str(ans) + '\n'
            print s,
            f.write(s)
            continue
        else:
            ans = '1'
            buildGrid(R,C)
        
        
        s = "Case #%d:\n" % (case)
        if ans == 'Impossible':
            s += str(ans) + '\n'
        else:
            for a in ans:
                s += ''.join(a) + '\n'
        print s,
        f.write(s)
    
    f.close()
main();
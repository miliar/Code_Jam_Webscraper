import sys
'''
Only one x or o per row/column
Only one + or o per diagonal
Set x/o for row column
Populate + and or upgrade x to o systematically; choice has same value
Best answer will usually be N + 2N-2 for N x's and (2N-2) +'s or x/o conversions
'''

def print_model(model):
    n = len(model)
    for i in range(n):
        for j in range(n):
            sys.stdout.write(model[i][j])
        sys.stdout.write('\n')
    sys.stdout.write('\n')



if __name__  == '__main__':
    xx = sys.stdin.readline()
    num = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        num += 1
        (n, m) = line.strip().split()
        n = int(n)
        m = int(m)
        score = 0
        model = []
        row_taken = {}
        col_taken = {}
        diag_pos_taken = {}
        diag_neg_taken = {}
        for i in range(0,2*n-1):
            diag_pos_taken[i] = 0
        for i in range(-n+1,n):
            diag_neg_taken[i] = 0
        model_changed = []
        for i in range(n):
            model.append([])
            for j in range(n):
                model[i].append('.')
        for i in range(m):
            line = sys.stdin.readline()
            (mod, ri, ci) = line.strip().split()
            ri = int(ri)-1 # switch to zero-based, add one on output
            ci = int(ci)-1
            model[ri][ci] = mod
            if mod == 'x' or mod == 'o':
                row_taken[ri] = 1
                col_taken[ci] = 1
                score += 1
            if mod == '+' or mod == 'o':
                diag_pos_taken[ri+ci] += 1
                diag_neg_taken[ri-ci] += 1
                score += 1

        #print 'Input:',score,n
        #print_model(model)

        # first populate x/o's. just use x unless already an o
        for i in range(n): # for each row, if not populated, add at first column available
            if i in row_taken: continue
            for j in range(n):
                if j in col_taken: continue
                if model[i][j] != '.': continue
                model[i][j] = 'x'
                row_taken[i] = 1
                col_taken[j] = 1
                model_changed.append( (i,j,'x') )
                score += 1
                #diag_pos_taken[i+j] = 1
                #diag_neg_taken[i-j] = 1
                break
        #print_model(model)
        #print model_changed

        # scan through all possible positions for options to add '+' or upgrade 'x' - may be fast enough
        for i in [0,n-1]+range(1,n-1): 
            for j in range(n):
                #print 'diag',diag_pos_taken,diag_neg_taken
                if diag_pos_taken[i+j]: continue
                if diag_neg_taken[i-j]: continue
                # this position should be good for ugrade, either . to + or x to o
                if model[i][j] == '.':
                    model[i][j] = '+'
                    diag_pos_taken[i+j] += 1
                    diag_neg_taken[i-j] += 1
                    model_changed.append( (i,j,'+') )
                    score += 1
                elif model[i][j] == 'x':
                    model[i][j] = 'o'
                    diag_pos_taken[i+j] += 1
                    diag_neg_taken[i-j] += 1
                    if (i,j,'x') in model_changed:
                        model_changed.remove( (i,j,'x') )
                    model_changed.append( (i,j,'o') )
                    score += 1
                else:
                    sys.stderr.write('problem\n')

        #print_model(model)

        # finally, scan through all possible '+' positions for possible upgrade, only if it is the only +/o on the diagonal
        for i in range(n): 
            for j in range(n):
                if model[i][j] != '+': continue
                if diag_pos_taken[i+j] !=1: continue
                if diag_neg_taken[i-j] !=1: continue
                if i in row_taken: continue
                if j in col_taken: continue
                # upgrade to 'o'
                model[i][j] = 'o'
                if (i,j,'+') in model_changed:
                    model_changed.remove( (i,j,'+') )
                model_changed.append( (i,j,'o') )
                score += 1
            
        #print 'Output:'
        #print_model(model)


        print 'Case #'+str(num)+': '+ str(score) + ' ' + str(len(model_changed))
        for (a,b,c) in model_changed:
            print c, a+1, b+1

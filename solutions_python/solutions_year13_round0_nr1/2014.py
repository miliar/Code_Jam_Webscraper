def state(A, i):
    def check(L):
        # print L
        flag = 1
        no_of_dots = 0
        for l in L:
            x = dic.get(l, 0)
            if '.' in l:
                no_of_dots += 1
            elif x == 1:
                print 'Case #' + str(i) + ': X won'
                flag = 0
                break
            elif x == 2:
                print 'Case #' + str(i) + ': O won'
                flag = 0
                break
        if flag == 1:
            if no_of_dots > 0:
                print 'Case #' + str(i) + ': Game has not completed'
            else:
                print 'Case #' + str(i) + ': Draw'
    dic = {'XXXX': 1,'TXXX':1,'XTXX':1,'XXTX':1,'XXXT':1,'OOOO':2,'OTOO':2,'TOOO':2,'OOTO':2,'OOOT':2}
    check([A[0], A[1], A[2], A[3], A[0][0] + A[1][0] + A[2][0]+ A[3][0], A[0][1] + A[1][1] + A[2][1]+ A[3][1], A[0][2] + A[1][2] + A[2][2]+ A[3][2], A[0][3] + A[1][3] + A[2][3]+ A[3][3], A[0][0] + A[1][1] + A[2][2]+ A[3][3], A[0][3] + A[1][2] + A[2][1]+ A[3][0]])

def readfile(filename):
    f = open(filename, "r")
    all = [ line.rstrip() for line in f.readlines()]
    n = int(all[0])
    lines = []
    for line in all[1:]:
        if len(line) == 0:
            continue
        lines.append(line)
    # print lines
    for j in range(len(lines)/4):
        i = 4*j
        A = [lines[i], lines[i+1], lines[i+2], lines[i+3]]
        # print A, j
        state(A, j + 1)
        
readfile('A-large.in')          
'''
n = int(raw_input())
i = 0
while i < n:
    A = []
    for j in range(4):
        A.append(raw_input())
    s = raw_input()
    state(A, i+1)
    i += 1
'''


    
    

def time(count, C, F, X):
    s = 0
    for i in range(count):
        if i == count - 1:
            s = s +(X/(2+F*(i)))
        else:
            s = s +(C/(2+F*(i)))
    return s
            





def run(C, F, X):
    count = 1
    minval = time(count, C, F, X)
    flag = 0
    while flag == 0 :
        count += 1
        nextval = time(count, C, F, X)
        if nextval > minval:
            flag = 1
        else:
            minval = nextval
    return minval


def runprog(FILE):
    infile = open(FILE,'r')
    outfile = open('cookies.out','w')
    line1 = infile.readline()
    T = int(line1.strip('\n'))
    for i in range(T):
        line2 = infile.readline()
        par = line2.strip('\n').split(' ')
        for j in range(3):
            par[j] = float(par[j])
        res = run(par[0], par[1], par[2])
        outfile.write('Case #' + str(i+1) + ': ' + str(format(res,'.7f')) + '\n')
    infile.close()
    outfile.close()
    
    
        

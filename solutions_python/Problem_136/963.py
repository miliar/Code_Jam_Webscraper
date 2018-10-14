def solve(case):
    C,F,X=case
    r = 2
    cost = 0
    while C/r+X/(r+F)<X/r:
        cost += C/r
        r+=F
    cost+=X/r
    return round(cost,7)
    
    

def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = a_in.readlines()
    N = int(results[0].replace('\n',''))
    a_out = open('B_output.txt','w',encoding = 'utf-8')
    for i in range(1,N+1):
        case = list(map(float,results[i].replace('\n','').split()))
        #print(case)
        rels = "Case #"+str(i)+": "+"{0:.7f}".format(solve(case))
        a_out.write(rels+'\n')

run('B-large.in')

#t=solve([30.50000,3.14159,1999.19990])
#t=solve([3,1,10000])

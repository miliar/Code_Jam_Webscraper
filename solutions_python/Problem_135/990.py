def solve(g1,g2,ar1,ar2):
    r1= set(ar1)
    r2= set(ar2)
    intsect = r1&r2    
    if len(intsect)==1:
        return list(intsect)[0]
    elif len(intsect)>1:
        return "Bad magician!"
    elif len(intsect)==0:
        return "Volunteer cheated!"
    
    

def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = a_in.readlines()
    N = int(results[0].replace('\n',''))
    a_out = open('A_output.txt','w',encoding = 'utf-8')
    for i in range(1,N+1):
        tmp = 10*(i-1)
        g1 = int(results[1+tmp].replace('\n',''))
        g2 =int(results[6+tmp].replace('\n',''))
        ar1=list(map(int, results[1+tmp+g1].replace('\n','').split()))
        ar2 = list(map(int, results[6+tmp+g2].replace('\n','').split()))
        rels = "Case #"+str(i)+": "+str(solve(g1,g2,ar1,ar2))
        a_out.write(rels+'\n')

run('A_t.txt')
run('A-small-attempt0.in')
        
    
    

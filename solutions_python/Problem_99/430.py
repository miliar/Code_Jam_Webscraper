def password(a, b, p):
    expectation = 2+b
    for k in range(a+1):
        p_k = 1
        p_l = p[1:(a-k+1)]
        for i in p_l:
            p_k = p_k*i
        expect = p_k*(2*k + b - a + 1) + (1-p_k)*(2*k +b-a+1+b+1)
        if expect < expectation:
            expectation = expect
    return(expectation)

infile = open('A-small-attempt2.in','r')
outfile = open('output1.txt','w')


x = int(infile.readline())
i=0
while i<x:
    [l1, l2] = infile.readline().strip().split()
    a,b = int(l1), int(l2)
    p = [1]
    p1 = infile.readline().strip().split()
    for m  in p1:
        if m == '1.000000':
            p.append(1)
        else:
            y = int(m[2:])/10**6
            p.append(y)
    
    k = password(a,b,p)
    j = str(i+1)
    outfile.write('Case #'+ j + ': ' + str(k)+'\n')
    i = i+1


outfile.close()
infile.close() 


import numpy
t=int(raw_input().strip())
for i in range(1,t+1):
    d,n=list(map(int,raw_input().strip().split()))
    tim=-1.0
    for j in range(1,n+1):
        di,si=list(map(int,raw_input().strip().split()))
        ti=numpy.longfloat(d-di)/numpy.longfloat(si)
        if tim < ti:
            tim=ti
    print("Case #"+str(i)+": "+str(numpy.longfloat(d)/tim))
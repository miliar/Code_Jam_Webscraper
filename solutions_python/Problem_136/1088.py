a=open('B-large.in')
b=open('file.out', 'w')

cases=int(a.readline());

for case in range(cases):

    numbers=map(float, a.readline().split())
    C=numbers[0]
    F=numbers[1]
    X=numbers[2]

    cPSec=2.0;

    minTime=X/cPSec;

    count=0;

    while True:
	count+=C/cPSec;
        cPSec+=F;
        timeToEnd=X/cPSec;

        if count+timeToEnd < minTime:
	    minTime=count + timeToEnd
	else:
	    break
    
    b.write('Case #'+str(case+1)+': '+str(minTime)+'\n')
b.close();

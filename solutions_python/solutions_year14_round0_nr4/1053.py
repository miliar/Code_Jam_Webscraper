a=open('D-large.in');
b=open('file.out','w');

cases=int(a.readline());

for case in range(cases):
    N=int(a.readline());
    me=map(float, a.readline().split());
    he=map(float,a.readline().split());
    #war: optimal of he
    me.sort()
    he.sort()
    meIndex=0;
    heIndex=0;
    pointsWar=0;
    while heIndex<N:
	if me[meIndex]<he[heIndex]:
	    heIndex+=1;
	    meIndex+=1;
	else:
	    heIndex+=1;
	    pointsWar+=1; 
    #d. war: always I can make optimal solution with method
    meIndex=0
    heIndex=0
    pointsDWar=0
    while meIndex < N:
	if he[heIndex]<me[meIndex]:
	    meIndex+=1;
	    heIndex+=1;
	    pointsDWar+=1;
        else:
	    meIndex+=1;
    b.write("Case #"+str(case+1)+": "+str(pointsDWar)+" "+str(pointsWar)+"\n");
b.close();
	

    
    

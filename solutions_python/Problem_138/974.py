#deceitful war
f = open('D-large.in', 'r')
read = f.readline() #of test cases
x = 0
while x<int(read):
   nind = 0
   kind = 0
   nw = []
   kw = []
   nw2 = []
   kw2 = []

   fpoints = 0 #points for fair play
   dpoints = 0	#points for deceitful play

   blocks = int(f.readline()) # num of blocks in the game
   nao_weights = f.readline().split()
   ken_weights =f.readline().split()

   nw = map(float,nao_weights)
   kw = map(float,ken_weights)
   nb = blocks

   nw2 = map(float,nao_weights)
   kw2 = map(float,ken_weights)
   nb2 = blocks

   #fair play
   while nb != 0:
    nao = max(nw) #naomi's choice
    nind = nw.index(nao) 

    #sure point for naomi
    ken = max(kw)

    if ken < nao: #if all of ken's weights are less than that of naomi's, ken will choose the least of his blocs
    	kind = kw.index(min(kw)) #get index of the min weight of ken's blocks
    	fpoints =  fpoints + 1

    else:
    	#find a bloc in ken's weights that could outweigh naomi's choice (least)
    	for i in kw:
    		if i > nao and i<=ken:
    			ken = i
    			kind = kw.index(i)

    #delete blocks used in play
    nw.pop(nind)
    kw.pop(kind)
    nb = nb-1

   #deceitful play
   nao_told = 0
   while nb2 != 0:
   	ken_max = max(kw2)
   	nao_max = max(nw2)

   	nao_told = nao_max - 0.1
   	ken = ken_max

   	if ken_max > nao_max:	#sure win for ken
   		nao = min(nw2)

   	else:
   		nao = max(nw2)

   	if ken<nao:
   		dpoints = dpoints + 1
   	nind = nw2.index(nao)
   	kind = kw2.index(ken)

   	nw2.pop(nind)
   	kw2.pop(kind)
   	nb2 = nb2 - 1


   #printing 
   
   print 'Case #{num}: {dpoints} {fpoints}'.format(num=x+1,dpoints=dpoints,fpoints=fpoints)
   x = x+1

f.close()
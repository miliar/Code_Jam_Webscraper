
f= open('A-small-attempt0.in-2.txt')
imput= f.read().splitlines()

fOut = open('solverMagicTrick.out', 'w')

ncases=int(imput[0])
del imput[0]

#prueba:

for a in range(1,ncases+1):
    aoption=int(imput[0])
    aArray=imput[aoption].split()
    del imput[:5]
    boption=int(imput[0])
    bArray=imput[boption].split()
    del imput[:5]
    result= list(set(aArray) & set(bArray) )
    if len(result)==1:
        msg= result[0]
    if len(result)>1:
        msg= "Bad magician!"
    
    if len(result)==0:
        msg= "Volunteer cheated!"
        
    fOut.write("Case #"+str(a)+": "+msg+"\n")
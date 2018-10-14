outresult= open ('D-small-attempt0.out', 'w')
inputterms = open('D-small-attempt0.in', 'r')
values = inputterms.readlines()
y= int(values[0])
values.pop(0)
sum=0
for line in values[0:y]:
    sum+=1
    param= line.split()
    x = int(param[0])
    r = int(param[1])
    c = int(param[2])
    if min(r,c)>= x-1:
        chance1 = 1
    else:
        chance1 = 0
    if x <= max(r,c):
        chance2 = 1
    else:
        chance2 = 0
    if (r*c)%x==0:
        chance3 = 1
    else:
        chance3 = 0
    chan= min(chance1,chance2,chance3)
    if chan==0:
        winner='RICHARD'
    else:
        winner='GABRIEL'
    outresult.write('Case #'+ str(sum) + ': ' + winner )
    outresult.write('\n') 
outresult.close()
    
        

                        
                        


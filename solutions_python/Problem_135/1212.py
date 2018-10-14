'''
Created on 12-Apr-2014

@author: savs95
'''
solution=[]
gamma=open("input.in","r")
hilde=open("output.txt","w")
case=int(gamma.readline())
itern=0
while(itern<case):
    alpha=int(gamma.readline())
    card=[]
    z=0
    while(z<4):
        beta=gamma.readline()
        card+=[beta[:-1].split()]
        z+=1
    c=int(gamma.readline())
    z=0
    while(z<4):
        z+=1
        beta=gamma.readline()
        card+=[beta[:-1].split()]
    count=0
    for i in range(0,4):
        for j in range(0,4):
            if card[alpha-1][i]==card[3+c][j]:
                if(count==0):
                    card_no=card[alpha-1][i]
                count+=1
    if(count==0):
        string="Case #"+str(itern+1)+": "+"Volunteer cheated!"+"\n"
    elif(count>1):
        string="Case #"+str(itern+1)+": "+"Bad magician!"+"\n"
    else:
        solution+=[card_no]
        string="Case #"+str(itern+1)+": "+card_no+"\n"
    itern+=1
    hilde.write(string)

    
gamma.close()
hilde.close()
from sys import stdin

dictionary = {'XXXX':1, 'TXXX':1, 'XTXX':1, 'XXTX':1, 'XXXT':1, 'OOOO':-1, 'TOOO':-1, 'OTOO':-1, 'OOTO':-1, 'OOOT':-1}

T = int(input())
data = stdin.readlines()
d=0
t=1
while(t<=T):
    i=0
    flag = 0
    li=[]
    dotpresent = 0
    while(i<4):
        data[d]=data[d].rstrip("\n")
        if '.' in data[d]:
            dotpresent=1
        li.append(data[d])
        d+=1
        i+=1
    d+=1
    
    for ii in range(4):
        s = ''
        for jj in range(4):
            s+=li[jj][ii]
        li.append(s)
    
    li.append(li[0][0]+li[1][1]+li[2][2]+li[3][3])
    li.append(li[0][-1]+li[1][-2]+li[2][-3]+li[3][-4])
    print(li)
    for ii in li:
        if ii in dictionary:
            if dictionary[ii]==1:
                print("Case #"+str(t)+": X won")
                flag = 1
                break
            else:
                print("Case #"+str(t)+": O won")
                flag = 1
                break
    if(flag == 0):
        if dotpresent == 1:
            print("Case #"+str(t)+": Game has not completed")
            break
        else:
            print("Case #"+str(t)+": Draw")
            break
    t+=1
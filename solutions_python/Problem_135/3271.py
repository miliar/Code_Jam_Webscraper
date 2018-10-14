__author__ = 'Ana'


import sys

def main():
    file=sys.stdin
    t=int(file.readline())
    v1=[0]*4
    v2=[0]*4
    for i in range(t):
        r1=int(file.readline())
        for j in range(4):
            line=file.readline()
            if j+1==r1:
                values=line.split(' ')
                v1[0],v1[1],v1[2],v1[3]=int(values[0]),int(values[1]),int(values[2]),int(values[3])
        r2=int(file.readline())
        for j in range(4):
            line=file.readline()
            if j+1==r2:
                values=line.split(' ')
                v2[0],v2[1],v2[2],v2[3]=int(values[0]),int(values[1]),int(values[2]),int(values[3])

        ans=[]
        for c in v1:
            if v2.__contains__(c):
                ans.append(c)

        if len(ans)==0:
             print 'Case #'+str(i+1)+': Volunteer cheated!'

        elif len(ans)>1:
            print 'Case #'+str(i+1)+': Bad magician!'

        else:
            print 'Case #'+str(i+1)+': '+str(ans[0])


main()

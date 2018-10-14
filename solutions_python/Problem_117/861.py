
def answer(m,n,data):
    colmax=[max([data[i][j] for j in range(n)]) for i in range(m)]
    rowmax=[max([data[i][j] for i in range(m)]) for j in range(n)]
    
    ok=all([(data[i][j]>=colmax[i] or
             data[i][j]>=rowmax[j])
            for i in range(m)
            for j in range(n)])
                
    return 'YES' if ok else 'NO'


data="""3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1"""

data=open("B-large.in").read()

data=data.split('\n')

# output answer
f=open("B-large.out","w")
row=0
T=int(data[0])
for i in range(T):
    row+=1
    m,n=map(int,data[row].split())
    question=[map(int,d.split(' ')) for d in data[row+1:row+m+1]]
    row+=m
    f.write("Case #%d: "%(i+1)+answer(m,n,question)+'\n')
f.close()    

    

#Cruise Control






with open ('in.txt') as ifile:
    inp = ifile.readlines()

wfile=open('out.txt', 'w')

t=int(inp[0])
ctr=1
for x in range(t):
    ans=float(-1)
    res='Case #'+str(x+1)+': '
    dist, N=list(map(float, inp[ctr].split()))
    N=int(N)
    ctr+=1
    for y in range(N):
        temp=list(map(float, inp[ctr].split()))
        ctr+=1
        if (dist-temp[0])/temp[1]>dist/ans or ans==-1:
            ans=dist/((dist-temp[0])/temp[1])
            
        
    answer='%0.6f' %ans
    wfile.write(res+answer+'\n')
          
wfile.close()
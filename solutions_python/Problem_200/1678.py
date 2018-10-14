# Tidy numbers
# CodeJam 2017
# Istvan Szabo



#f=open("B-small-attempt0.in")
#f=open("B-test.in")
f=open("B-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')

for i in range(T):
    print(i)
    N=list(input_lines2[i+1][0])
    for j in range(len(N)-1):
        y=len(N)-j-2
        print('y='+str(y) + 'length N= '+str(len(N)))
        if int(N[y])>int(N[y+1]):
            N[y]=str(int(N[y])-1)
            for k in range(y+1,len(N)):
                N[k]='9'
    g.write('Case #'+str(i+1)+': '+str(int( ''.join(N) ))+'\n')
g.close()

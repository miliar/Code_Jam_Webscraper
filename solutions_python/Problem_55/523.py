def roller_coaster_ride(rounds,capacity,groups):
    cost=0
    for i in range(0,rounds):
        n=0
        coaster=[]
        while n<=capacity:
            if (n+groups[0])<=capacity:
                coaster.append(groups[0])
                n=n+groups[0]
                groups.pop(0)
            else:
                break
            if groups==[]:
                break
        cost=cost+n
        #print "c=",coaster,",g=",groups
        groups=groups+coaster
        #print "g=",groups
    return cost

infile=open("A-small.in","r")
outfile=open("A-small.out","w")

number_of_cases=infile.readline()

case=1

# R = rounds
# k = capacity
# N = number of groups


while infile:
    s=infile.readline()
    if s=='':
        break
    l=s.split()
    R=int(l[0])
    k=int(l[1])
    N=int(l[2])
    s=infile.readline()
    if s=='':
        break
    l=s.split()
    g=[]
    for i in l:
        g.append(int(i))

    c=roller_coaster_ride(R,k,g)
    outfile.write("Case #"+str(case)+": "+str(c)+"\n")
    case = case+1

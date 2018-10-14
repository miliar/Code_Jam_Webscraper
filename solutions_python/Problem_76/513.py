from functools import reduce

inFile = open("C-large.in.in", 'r')
outFile = open("candySplitting.out",'w')
N = int(inFile.readline())

for i in range(1,N+1):
    M = int(inFile.readline())
    l = [int(x) for x in inFile.readline().split()]
    r = reduce(lambda x,y:x^y, l)
    if r == 0: #possible
        best = sum(l)-min(l)
        outFile.write("Case #"+str(i)+": "+str(best)+"\n")
        print("Case #"+str(i)+": "+str(best))
    else:
        outFile.write("Case #"+str(i)+": NO\n")
        print("Case #"+str(i)+": NO")

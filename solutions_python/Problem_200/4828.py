import time
trials = 100000000

infilename ='B-small-attempt0.in'


timestart = time.time()
iterations = 0
problem = []



def solve(i):
    num = int(i)
    # for x in xrange(num,0,-1):
    #
    #     # print str(x), "".join(sorted(str(x)))
    #     if  str(x) == "".join(sorted(str(x))):
    #         return x
    # return 0
    while num > 0:
        if  str(num) == "".join(sorted(str(num))):
            return num
        num -= 1


f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    # print i
    problem.append( f.readline().strip() )
fw = open('out.txt', 'w')
num = 1
for i in problem:
    answer=str(solve(i))
    print "Case #"+str(num)+": "+str(answer)
    fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num += 1
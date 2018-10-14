import Queue

level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    [s,k] = input_file.readline().split()
    k = int(k)
    s = [x == '+' for x in s]
    n = len(s)
    q = Queue.Queue(k)
    t = 0
    for i in xrange(n):
        if(not q.empty() and q.queue[0] + k <= i):
            q.get()
        s[i] ^= (q.qsize() & 1)
        if(s[i] == 0):
            if(i > n-k):
                return "IMPOSSIBLE"
            else:
                q.put(i)
                t+=1    
    return t

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()

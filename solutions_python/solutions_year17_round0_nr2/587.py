import math
import bisect
data = []

# def make():

#     offset2 = 0
#     for i in xrange(2, 19):
#         offset1 = math.factorial(i - 2 + 8) / (math.factorial(i-2) * math.factorial(8))
#         offset2 += math.factorial(i - 1 + 8) / (math.factorial(i-1) * math.factorial(8))
#         print offset1, offset2, i
#         if i == 2:
#             offset1 = 0
            
#         start = offset1
#         for j in xrange(1, 10):
#             for k in xrange(start, offset2):
#                 temp = str(j) + data[k]
#                 data.append(temp)
#                 # print k, temp, offset1, offset2
            
#             start = offset1*(i-1) + j
#             print offset1
#             print data      

#         if i == 4:
#             break


def recurse(start, out, n):

    if n == 0:
        data.append(int(out))
        return 

    for i in xrange(start, 10):
        temp = out + str(i)
        recurse(i, temp, n - 1)

def start():

    for i in xrange(1, 19):
        recurse(1, "", i)

start()
# print data[:200]

# inp = open("B-small-attempt0.in", "r")
# out = open("B-small-output", "w")
inp = open("B-large.in", "r")
out = open("B-large-output", "w")
tt = int(inp.readline())
for i in xrange(tt):
    n = inp.readline()
    a = list(n)
    n = int(n)
    if n in data:
        ans = n

    else:        
        idx = bisect.bisect_left(data, n)
        ans = data[idx-1]
        # print idx, data[idx-1]

    out.write("Case #%d: %s \n" % (i+1, ans))

inp.close()
out.close()
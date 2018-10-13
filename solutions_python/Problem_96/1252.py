__author__ = 'Daria'
#import time
#start = time.time()
#reading
input = open ('/Users/Daria/PycharmProjects/CodeJam/input.txt','r')
N = int(input.readline())
print N
res = []

def surprised(total,p):
    if total == 0:
        return False
    if p == 1 and total > 1:
        return True
    if total == 3*p - 3 or total == 3*p - 4:
        return True
    return False

def is_better(total,p):
    if total == 0 and p == 0:
        return True
    elif total == 1 and p == 1:
        return True
    elif total == 2 and p == 1:
        return True
    elif total >= 3*p - 2:
        return True
    return False

i = 0
while i <N:
    count = 0
    l = map(int, input.readline().split())
    print l
    n = l[0]
    S = l[1]
    p = l[2]
    for total in l[3:]:
        if total >= 3*p -4:
            if is_better(total,p):
                count += 1
            elif surprised(total,p) and S > 0:
                count += 1
                S -= 1
    res.append(count)
    i += 1

input.close()
output = open ('/Users/Daria/PycharmProjects/CodeJam/out.txt','w')

k = 0
for c in res:
    k += 1
    output.write("Case #%i: %i\n"%(k,c))
    print ('Case #%i: %i'%(k,c))
  #  output.write("\n")
output.close()
#print time.time()-start
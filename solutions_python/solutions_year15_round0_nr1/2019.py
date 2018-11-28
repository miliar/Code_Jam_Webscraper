import math

f = 'A-large'
f_in = f + ".in"
f_out = f + "-out.txt"

with open(f_in ,'r') as f:
 	read_data = f.read().split('\n')

fo = open(f_out, 'w')

T = int(read_data[0])
data = []
for i in xrange(1,T+1):
	data.append(read_data[i].split(' '))

print T, data
ans = [0 for i in range(T)]

for i in xrange(0,T):
    v = [int(j) for j in data[i][1]]
    ans[i] = 0
    sum = 0
    for j in xrange(0,int(data[i][0])+1):
        delta = j - (sum + ans[i])
        if delta > 0:
            ans[i] = ans[i] + delta
        sum = sum + v[j]
        #print j, sum, ans[i], delta, v[j]
    # print v

for i in xrange(0,T):
    print(ans[i])
    fo.write('Case #' + str(i+1) +": " + str(ans[i]) + '\n')
fo.close()

rr = file("input.txt").readlines()
count = int(rr[0])
line = 1
s = ''
for i in xrange(count):
    sum = 0
    temp = rr[line].split()
    people = map(int,rr[line+1].split())
    line += 2
    r,k,n = map(int,temp)
    for j in xrange(r):
        queue = 0
        length = n
        while (queue+people[0] <= k):
               if length <= 0:
                    break
               length -= 1
               tem = people.pop(0)
               queue += tem
               people.append(tem)
        sum+= queue
    s += 'Case #'+str(i+1)+': '+str(sum)+'\n'
w = open('output.txt','w')
w.write(s)
w.close()


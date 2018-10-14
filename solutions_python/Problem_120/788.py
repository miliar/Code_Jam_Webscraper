
f = open("input")
f_out = open('output', 'w')

count = int(f.readline())
for i in range(count):
    r, t = f.readline().split(' ')
    r = int(r)
    t = int(t)
    
    j = (r + 1) * 2 - 1
    sum = j
    cnt = 0
    while sum <= t:
        j = j + 4
        sum = sum + j
        cnt = cnt + 1  
    
    f_out.write("Case #%i: %d\n" % (i + 1, cnt))



f.close()
f_out.close()
print "done"
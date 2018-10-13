input_file = open('C:\Users\Inspiron\Downloads\A-large.in')
output_file = open('abcdef.out', 'w')
t = int(input_file.readline())
for i in xrange(1, t+1):
    a, b = input_file.readline().split()
    a = int(a)
    b = list(b)
    b = map(int, b)
    c = 0
    if b[0] == 0:
        c+=1
        b[0] = 1
    for j in xrange(1, a):
        if b[j] == 0:
            if sum(b[:j]) == j:
                b[j] = 1
                c+=1
    output_file.write("Case #"+str(i)+": "+str(c)+'\n')
input_file.close()
output_file.close()


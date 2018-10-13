# Google Code Jam
# Recycled Numbers
# vishen

f = open('google_dump.txt', 'r')
T = f.readline()
gs = open('google_solutions.txt', 'w')
for count in range(int(T)):
    line_split = f.readline().split()
    a = int(line_split[0])
    b = int(line_split[1])
    print a, b

    recycled_numbers = 0

    for x in range(a, b+1):
        for y in range(a, b+1):
            if x < y: continue
            if x == y: continue

            tmp_a = str(x)
            tmp_b = str(y)
            #print 'WTFWTFWTFW: %s %s' % (tmp_a, tmp_b)
            for z in range(len(tmp_a)):
                tmp_a = tmp_a[1:] + tmp_a[0]
                #print tmp_a, tmp_b
                if tmp_a == tmp_b:
                    #print 'found 1'
                    #print tmp_a, tmp_b
                    recycled_numbers += 1
                    break
        
    print 'Case #%d: %s\n' % (count+1, recycled_numbers)
    gs.write('Case #%d: %s\n' % (count+1, recycled_numbers))

f.close()
gs.close()


import math
row_num = raw_input()

for i in range(int(row_num)):
    line = raw_input()
    a, b = line.split()
    #print a
    #print b
    keta = int(math.log10(int(a)) + 1)
    #print keta
    count = 0
    for j in range(int(a), int(b)+1):
        base = str(j)
        base_array = [j]
        for k in range(keta):
            c = int( base[k:] + base[0:k] )
            #print c
            if c >= int(a) and c <= int(b):
                if not c in base_array:
                    base_array.append(c)
        #print base_array
        for elm in base_array:
            if elm > j:
                count = count + 1

    print "Case #" + str(i+1) + ": " + str(count)


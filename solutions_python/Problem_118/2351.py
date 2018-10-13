from math import sqrt

file_in = open('C-small-attempt0.in', 'r')
file_out = open('pal.out', 'w')
N = int(file_in.readline())

for i in range(N):
    start, end = map(int, file_in.readline().split(" "))
    #print start, end

    cnt = 0
    for j in range(start, end+1):
        string = str(j)
        #check it is palindrom
        if string[0:] == string[::-1]:
            #check it is square of a palindrom
            sq_root = sqrt(j)
            if sq_root.is_integer():
                string2 = str(int(sq_root))
                if string2[0:] == string2[::-1]:
                    #print string2
                    #print i
                    cnt += 1
    result = "Case #%d: %d\n" % (i+1, cnt)
    file_out.write(result)

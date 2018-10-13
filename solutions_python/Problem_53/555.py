casenumber = 1
file = open("A-large.in")
wfile = open("2.txt", "w")
numberofcases = int(file.readline()) +1
#numberofcases = int(raw_input()) +1
while casenumber < numberofcases:
    line = file.readline()
    #line = raw_input()
    if not line:
        break
    numbers = line.split()
    N = int(numbers[0])
    K = int(numbers[1])
    x = (2**N)
    y = x-1
    
    if ((K-y)%x == 0):
        wfile.writelines("Case #" + str(casenumber) + ": ON\n")
        #print "Case #" + str(casenumber) + ": ON\n"
    else:
        wfile.writelines("Case #" + str(casenumber) + ": OFF\n")
        #print "Case #" + str(casenumber) + ": OFF\n"
    casenumber+=1
wfile.close()
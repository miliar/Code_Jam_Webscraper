import sys

filename = sys.argv[1]
f = open(filename)
output = open("result.txt","w")
times = int(f.readline())

for i in xrange(times):
    line = f.readline()
    N,K = [int(x) for x in line.split()]
    shiftedK = K-(2**N)+1
#    print "N: ",N," K: ",K," shifted: ",shiftedK
    if shiftedK%(2**N) == 0:
        output.write("Case #"+str(i+1)+": ON\n")
    else:
        output.write("Case #"+str(i+1)+": OFF\n")

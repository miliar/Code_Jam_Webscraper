import sys

fin = open(sys.argv[1],'rU')
fout = open(sys.argv[2],'w')
T = int(fin.readline().strip())

light = {True: "ON", False: "OFF"}

for case,line in enumerate(fin):
    N,K = map(int,line.split())
    state = (K-(2**N-1))%2**N == 0
    fout.write("Case #%i: %s\n" % (case+1, light[state]))

fin.close()
fout.close()

assert case+1 == T, "Wrong number for T"
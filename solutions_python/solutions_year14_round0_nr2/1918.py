infile = open('B-small-attempt0.in', 'r')
try:
    outfile = open('B-small.out', 'x')
except:
    outfile = open('B-small.out', 'w')
st = infile.readline()
st = st.rstrip()
n = int(st)
for p in range(1, n+1):
    st = infile.readline()
    st = st.rstrip()
    sp = st.split(' ')
    c = float(sp[0])
    f = float(sp[1])
    x = float(sp[2])
    k = 0
    previous = 0
    curr = 0
    while True:
        previous = curr
        time = 0.0
        rate = 2.0
        for i in range(0, k):
            time += (c / rate)
            rate += f
        time += (x / rate)
        curr = time
        if (previous != 0) and (curr > previous):
            outfile.write('Case #' + str(p) + ': ' + str(previous) + '\n')
            break
        k += 1
infile.close()
outfile.close()

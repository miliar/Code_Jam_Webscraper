fin = open("a.in", "r")
fout = open("a.sol", "r")

m = {}

fin.readline() #skip one line

m['z'] = 'q'
m['q'] = 'z'
try:
    while True:
        inp = fin.readline()
        out = fout.readline()
        out = out[len(out)-len(inp):]

        #print(inp, out)

        for i in range(len(inp)):
            m[inp[i]] = out[i]
#m[out[i]] = inp[i]
except:
   pass

#print(m)
#print(len(m))

fin.close()
fout.close()

n = int(raw_input(""))

for i in range(n):
    line = raw_input()
    line = "".join([m[x] for x in line])
    print("Case #" + str(i+1) + ": " + line)


f = open("./dataset", "rb")
ofp = open("./output", "wb")

cases = int(f.readline())

for N in range(0, cases, 1):

	n, m = [x for x in f.readline().split()]
        cl = 0
        inv = 0
        for i in range(0, len(m)-1, 1):
                cl += int(m[i])
                if(cl+inv < i+1):
                        inv+=i+1-cl-inv
	ofp.write("Case #"+str(N+1)+": "+str(inv)+"\n")
      
f.close()
ofp.close()

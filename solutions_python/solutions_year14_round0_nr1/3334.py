a = "inp.txt"
outp = "out.txt"

with open(a) as f:
    inp = f.read().splitlines()
    inp = inp[1:]
    for i in range(0,len(inp)):
        tmp = inp[i].split(" ")
        for j in range(0,len(tmp)):
            tmp[j] = int(tmp[j])
        inp[i] = tmp

out = []
for i in range(0,len(inp),10):
    a = inp[i][0]
    b = inp[i+5][0]
    list1 = inp[i+a]
    list2 = inp[i+b+5]
    b = False
    flip = True
    s = 0
    for j in list1:
        for k in list2:
            if j==k and not b:
                s = j
                b = True
            elif j==k:
                flip = False
                break
    if not flip:
        out.append("Bad magician!")
        continue
    if s == 0:
        out.append("Volunteer cheated!")
    else:
        out.append(str(s))
                

with open(outp,"w") as f:
    counter = 1
    for t in out: 
       f.write("Case #"+str(counter)+": "+t+"\n")
       counter += 1


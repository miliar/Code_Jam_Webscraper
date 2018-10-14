
f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\A-large.in")
lines = f.readlines()
numcases = int(lines[0])
i = 1
pos = 1
while i <= numcases:
    d,n = [int(x) for x in lines[pos].split()]
    hrs = []
    op =pos
    while pos < op+ n:
        pos +=1
        hrs.append([float(x) for x in lines[pos].split()])
    hrs = sorted(hrs,key=lambda x: x[0])[::-1]
    ind = 0
    arr = 0.0
    c_h = []
    while ind < len(hrs):
        h = hrs[ind]
        c_arr = (d-h[0])/h[1]
        #print(c_arr)
        if c_arr > arr:
            arr = c_arr
        ind +=1
    sp = d/arr
    res = "Case #" + str(i) + ": " + str(sp)
    print (res)
    i = i+ 1
    pos +=1
import io
import string

def toInt(val):
    ret = ""
    for a in val:
        ret += str(a)
    return int(ret)

def toArr(val):
    ret = []
    for i in val:
        ret.append(i)
    return ret

fin = io.open('in.txt', 'r')
fout = io.open('out.txt', 'w')
T = int(fin.readline())
for z in range(T):
    cur = fin.readline().replace("\n", "")

    arr = []
    for a in cur:
        arr.append(int(a))
    out = ""
    print arr

    comp = False
    while True:
        for i in range(len(arr)):
            if i < len(arr) - 1:
                if arr[i] > arr[i + 1]:
                    ival = toInt(arr)
                    ival -= 1
                    arr = toArr(str(ival))
                    break
            if i == len(arr) - 1:
                comp = True
        if comp:
            break
    
    for a in arr:
        out += str(a)


    print "Case #" + str(z + 1) + ": " + str(out)
    fout.write(unicode("Case #" + str(z + 1) + ": " + str(out) + "\n"))
    
fin.close()
fout.close()
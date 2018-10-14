f = open('in.txt','r')
fo = open('out.txt','w')
cases = int(f.readline())
curcase=1
while curcase<=cases:
    s = f.readline()
    n = [x for x in s]
    n = n[:-1]
    first = True
    i = 0
    while i<len(n)-1:
        if(n[i] <= n[i+1]):
            i += 1
            continue
        else:
            n[i] = chr(ord(n[i]) - 1)
            j = i+1
            while j<len(n):
                n[j] = '9'
                j += 1
            i = -1
        i += 1
    ans = 0
    i = 0
    while i<len(n):
        ans = (ans*10) + ord(n[i]) - ord('0')
        i += 1
    fo.write("Case #" + str(curcase) + ": " +str(ans) + "\r\n")
    print("Case #" + str(curcase) + ": "+ str(ans))
    curcase += 1

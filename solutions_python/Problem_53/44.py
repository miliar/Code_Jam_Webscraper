def process_case() :
    n, k = map(int, raw_input().split())
    kk = k
    
    arr = []
    while k > 0 :
        arr.append(k%2)
        k = k >> 1
    while len(arr) < 32 :
        arr.append(0)
        

    #print arr
    def debug_dmp() :
        print n, kk
        s = ""
        for i in range(31, -1, -1) :
            s += str(arr[i])
                #print int(s, 2)
        assert(kk==int(s,2))
        #print s
        #print arr
    #debug_dmp()

    for i in range(0, n) :
        if arr[i]==0 :
            return "OFF"
    return "ON"

case_num = int(raw_input())
for i in range(case_num) :
    result = process_case()
    print "Case #%d: %s" % (i+1, result)

import sys
'''
Convert to array... decrement right to left until increasing...
'''


if __name__  == '__main__':

    xx = sys.stdin.readline()
    num = 0
    for line in sys.stdin:
        num += 1
        input = line.strip()
        arr = []
        for c in input:
            arr.append(int(c))
        arr = arr[::-1]
        idx = -1
        #print arr
        row = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                idx = i
                row = True
            if row:
                if arr[i] == arr[i+1]:
                    idx = i
            else:
                row = False
                #break
        #print idx
        for i in range(idx+1):
            arr[i] = 0
        
        ret = ''.join([str(c) for c in arr[::-1]])
            
        if idx>=0:
            ret = str(int(ret)-1)
        else:
            ret = str(int(ret))

        print 'Case #'+str(num)+': '+ ret

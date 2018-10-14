def fill(arr, R, C):
    for r in range(R):
        for c in range(C):
            c_ = c+1
            while (c_ < C):
                if not arr[r][c_] == '?':
                    break
                else:
                    arr[r][c_] = arr[r][c]
                c_ += 1
    for r in range(R):
        for c in range(C):
            c_ = c-1
            while (c_ > -1):
                if not arr[r][c_] == '?':
                    break
                else:
                    arr[r][c_] = arr[r][c]
                c_ -= 1

def complete(arr, R, C):
    for r in range(1, R):
        if arr[r][0] == '?':
            arr[r] = arr[r-1]
    for r in range(R-2, -1,-1):
        if arr[r][0] == '?':
            arr[r] = arr[r+1]

arr = []
file_ = open('out.txt','w')
with open('A-large.in','r') as file:
    t = int(file.readline().strip())
    for i in range(t):
        R, C = file.readline().strip().split()
        R, C = int(R), int(C)
        arr = [0] * R
        chars = set([])
        for r in range(R):
            values = file.readline().strip()
            arr_ = []
            for c in range(C):
                arr_.append(values[c])
                chars.add(values[c])
            arr[r] = arr_
        chars.discard('?')
        fill(arr, R, C)
        complete(arr,R,C)
        file_.write("Case #"+str(i+1)+":\n")
        for r in range(R):
            for c in range(C):
                file_.write(str(arr[r][c]))
            file_.write("\n")
file_.close()
        

def flip(S,i,K):
    res = ""
    for ii in range(len(S)):
        if i<= ii < i+K:
            res += "+" if S[ii] == "-" else "-"
        else:
            res += S[ii]
    return res
def solve(S,K):
    def find_last(S):
        for i in range(len(S)-1,-1,-1):
            if S[i] == "-":
                return i
    def helper(S,K,count):
        if S == "+"*len(S):
            return count
        index = find_last(S)
        if index - K + 1 < 0:
            return None
        sub = S[index-K+1:index+1]
        f = flip(sub,0,K)
        if f[-1] == "+":
            return helper(flip(S,index-K+1,K),K,count+1)
        else:
            return None
        
    # available = set([i for i in range(len(S)-K+1)])
    h = callWithLargeStack(helper,S,K,0)
    return h if type(h) == int else "Impossible" 

def callWithLargeStack(f,*args):
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

# print(callWithLargeStack(rangeSum,1,123456)) # prints 7620753696
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
contentsRead = readFile("A-large.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    S = c.split(" ")[0]
    K = c.split(" ")[1]
    res = solve(S,int(K))
    contentsToWrite += "Case #%d: " % count
    contentsToWrite += "%d" % res if type(res) == int else res 
    contentsToWrite += "\n"
    count+=1

writeFile("out.txt",contentsToWrite)

"""
ref = readFile("out_ref.txt")
stu = readFile("out.txt")
for c in range(len((ref.split("\n")[1:-1]))):
    if ref.split("\n")[1:-1][c] != stu.split("\n")[1:-1][c]:
        print("OOPs!")
        print(ref.split("\n")[1:-1][c])
"""

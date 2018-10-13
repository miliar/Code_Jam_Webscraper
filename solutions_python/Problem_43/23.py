import psyco
psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]

def myAdd(Dict, item, key):
#    print "dict", Dict, "key", key
    if key not in Dict or Dict[key] > item:
        Dict[key] = item

def solve(st):
    #print st
    digits = {st[0]:1}
    c = 2
    first=True
    for d in st:
        if d not in digits:
            if first:
                digits[d] = 0
                first=False
            else:
                digits[d] = c
                c+=1
    
    val=0
    st=st[::-1]
    for i in range(len(st)):
        val+=digits[st[i]] * (c**i)
    #print digits, c, val
    return val

from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    data = open("d:/gcj/in", "r")
    Cases = int(data.readline())
    for case in range(1, Cases + 1):
        st = data.readline().rstrip('\n')
        s="Case #%d: %d" % (case, solve(st))
        print(s)
        output.write(s+"\n")
            
    print time()-start_time

    
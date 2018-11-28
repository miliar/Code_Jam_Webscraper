target = 'welcome to code jam'
n = int(raw_input().strip())

class memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def occurances(input, inputIndex, targetIndex):
    '''
    How many occurances are there of target[targetIndex:] in input[inputIndex:]
    '''
    global target
    retval = 0
    if targetIndex == len(target):
        return 1

    for i in range(inputIndex, len(input)):
        if input[i] == target[targetIndex]:
            retval += occurances(input, i + 1, targetIndex + 1)
    
    return retval

for i in range(n):
    print 'Case #%s: %04d' % (i + 1, occurances(raw_input().strip(), 0, 0)) 





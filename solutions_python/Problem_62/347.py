file = open("A-small.in")

o = {'left' : 0.0, 'right' : 0.1}

class Window:
    def __init__(self, side, height, other=None):
        self.side = side
        self.height = height
        self.other = other
        
    def __repr__(self):
        return "%s(%i)" % (self.side, self.height)
        
T = int(file.readline())
for t in xrange(T):
    N = int(file.readline())
    
    windows = []
    for n in xrange(N):
        heightLeft, heightRight = tuple(map(int, file.readline().rstrip("\n").split(" ")))
        
        windowLeft = Window('left', heightLeft)
        windowRight = Window('right', heightRight)
        
        windowLeft.other = windowRight
        windowRight.other = windowLeft
        
        windows.extend([windowLeft, windowRight])
        
    windows.sort(key=lambda window: window.height + o[window.side])

    i = 0
    
    Q = []
    for window in windows:
        if window.height > window.other.height:
            Q.remove(window.other)
            for q in Q:
                if q.height > window.other.height or q.other.height > window.other.height:
                    if q.side == window.side and q.height < window.height:
                        i += 1
                    elif q.other.side == window.side and q.other.height < window.height:
                        i += 1
        elif window.height == window.other.height and window.side == 'right':
            pass
        else:
            Q.append(window)
        
    print "Case #%i: %s" % (t+1, i)

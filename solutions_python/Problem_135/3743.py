
class Log():
    def __init__(self, debug=False):
        self.debug = debug

    def info(self, fmt, *args):
        if self.debug:
            print fmt % args
    
def get_int():
    return int(raw_input())
    
def get_array():
    return [ int(i) for i in raw_input().split(' ')]
    
def get_raw(raw):
    fraw = []
    for i in range(1,5):
        a = get_array()
        if i == raw:
            fraw = a
    return set(fraw)

def solve(case):
    first = get_int()
    fraw = get_raw(first)
    
    second = get_int()
    sraw = get_raw(second)
    
    common = fraw.intersection(sraw)
    size = len(common)
    
    if size == 1:
        print "Case #%d: %s" %(case, list(common)[0])
    elif size == 0:
        print "Case #%d: %s" %(case, "Volunteer cheated!")
    else:
        print "Case #%d: %s" %(case, "Bad magician!")
    


if __name__ == "__main__":
    T = get_int()
    for case in range(1, T+1):
        solve(case)
        
        
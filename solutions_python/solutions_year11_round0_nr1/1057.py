import sys

class BotTrust(object):
    def __init__(self, sequence):
        self.seq = sequence
        self.robots = {'O':1, 'B':1}
        self.chunks = []
        self.moves = 0
        self.discount = 0 
        
    def do_chunk(self, chunk):
        cost = 0
        robot = chunk[0][0]
        d = max(0, abs(chunk[0][1] - self.robots[robot]) - self.discount)
        cost += d + 1
        self.robots[robot] = chunk[0][1] 
        for m in chunk[1:]:
            d = abs(m[1] - self.robots[robot])
            cost += d + 1
            self.robots[robot] = m[1]
        return cost
        
    def calc_chunks(self):
        chunk = None
        robot = None
        for m in self.seq:
            if m[0] == robot:
                chunk.append(m)
            else:
                if chunk != None:
                    self.chunks.append(chunk)
                chunk = [m]
                robot = m[0]
        self.chunks.append(chunk)
        
    def solve(self):
        self.calc_chunks()
        for chunk in self.chunks:
            cost = self.do_chunk(chunk)
            self.moves += cost
            self.discount = cost  
    
    
def read_test_case(instream):
    items = instream.readline().split()
    N = int(items[0])
    result = []
    items = items[1:]
    for i in range(N):
        result.append((items[i * 2], int(items[i * 2 + 1])))
    return result



if __name__ == '__main__':
    instream = sys.stdin
#    instream = open('test.tiny.in')
    outstream = sys.stdout
    test_cases = int(instream.readline())
    for i in range(test_cases):
        case = read_test_case(instream)
        bt = BotTrust(case)
        bt.solve()
        outstream.write("Case #%d: %d\n" % (i + 1, bt.moves))
        

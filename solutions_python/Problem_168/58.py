UP = 1
LEFT = 0
DOWN = 3
RIGHT = 4
class Map:
        def __init__(self, R, C):
                self.Rs = [[] for r in xrange(R)]
                self.Cs = [[] for c in xrange(C)]
                self.locs = []
                self.dirs = {}
        def Add(self, R, C, D):
                self.Rs[R].append([R, C, D])
                self.Cs[C].append([R, C, D])
                self.locs.append((R,C))
                self.dirs[(R, C)] = D
        def Solve(self):
                status = {x:False for x in self.locs}
                changeCount = 0
                for l, s in status.iteritems():
                        if s:
                                pass
                        visited = [l]
                        last = self.dirs[l]
                        flag = False
                        l2 = l
                        lo = l
                        while True:
                                lo = l2
                                l2 = self.Next(l2)
                                if l2 == None:
                                        break
                                if last + self.dirs[l2] == 4:
                                        flag = True
                                        break
                                if status[l2]:
                                        flag = True
                                        break
                                if l2 in visited:
                                        flag = True
                                        break
                                last = self.dirs[l2]
                                visited.append(l2)
                        if not flag:
                                r, c = lo
                                d = self.dirs[lo]
                                i = self.Cs[c].index([r, c, d])
                                j = self.Rs[r].index([r, c, d])
                                if len(self.Rs[r]) == 1:
                                        if len(self.Cs[c]) == 1:
                                                return 'IMPOSSIBLE'
                                        else:
                                                if i == 0:
                                                        d = DOWN
                                                else:
                                                        d = UP
                                else:
                                        if j == 0:
                                                d = RIGHT
                                        else:
                                                d = LEFT
                                self.Cs[c][i][2] = d
                                self.Rs[r][j][2] = d
                                self.dirs[lo] = d
                                changeCount += 1
                        for x in visited:
                            status[x] = True
                return changeCount
                                                        
                                
                                
        def Next(self, x):
                d = self.dirs[x]
                if d%2 == 1:
                        i = self.Cs[x[1]].index([x[0], x[1], d])
                        if d == UP:
                                i -= 1
                        else:
                                i += 1
                        if i < 0 or i == len(self.Cs[x[1]]):
                                return None
                        t = self.Cs[x[1]][i]
                        return (t[0], t[1])
                else:
                        i = self.Rs[x[0]].index([x[0], x[1], d])
                        if d == LEFT:
                                i -= 1
                        else:
                                i += 1
                        if i < 0 or i == len(self.Rs[x[0]]):
                                return None
                        t = self.Rs[x[0]][i]
                        return (t[0], t[1])
                        

	
def solve():
        R, C = map(int, raw_input().split())
        m = Map(R, C)
        for i in xrange(R):
                line = raw_input()
                for j, c in enumerate(line):
                        if c == "^":
                                m.Add(i, j, UP)
                        elif c == ">":
                                m.Add(i, j, RIGHT)
                        elif c == "v":
                                m.Add(i, j, DOWN)
                        elif c == "<":
                                m.Add(i, j, LEFT)
        return m.Solve()
		
	
	

T = int(raw_input())
for i in xrange(T):
	print 'Case #%d: %s' % (i+1, solve())


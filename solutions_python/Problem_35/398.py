import os
def line(f):
    return f.readline().replace("\n","")
def items_line(f, split=" "):
    return line(f).split(split)
def items_line_limit(f, limit, split=" "):
    return line(f).split(split, limit)
def int_line(f):
    return int(line(f))
def ints_line(f, split=" ", limit=None):
    line = items_line_limit(f, limit, split=split) if limit else items_line(f, split=split)
    return map(int, line)

def d_xy(y, x, i):
    return [(y-1,x),(y,x+1),(y+1, x),(y, x-1)][i]

def get_targets(map, y, x, Y, X):
    t = map[y-1][x] if y > 0 else None
    r = map[y][x+1] if x < X-1 else None
    b = map[y+1][x] if y < Y-1 else None
    l = map[y][x-1] if x > 0 else None
    
    return (t,r,b,l)



def find_sinks(map, Y, X):
    sinks = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            ts = get_targets(map, y, x, Y, X)
            for t in ts:
                is_sink = True
                if t is not None and t < cell:
                    is_sink = False
                    break
            if is_sink:
                sinks.append((y, x))
    return sinks
            

def run(infile, outfile):
    f = open(infile)
    out = open(outfile,"w")
    ns = int_line(f)
    
    for n in range(ns):
        Y, X = ints_line(f)
        map = [[]]*Y
        for i in range(Y):
            map[i] = ints_line(f)
        sinks = find_sinks(map,Y,X)
        map = Map(map, sinks, Y, X)
        map.fill_cover_magrix()
        map.sign_them_all()
        out.write("Case #%d:\n%s\n" % (n+1, map))
        print n
        
    out.close()
    f.close()

class Cell(object):
    def __init__(self, map, y, x):
        self.map = map
        self.y = y
        self.x = x
        self.sign = None
        self.next = None #Cell object
        self.prevs = [] #List of Cell object
        self.map.cover_matrix[y][x] = self
        if (self.y, self.x) not in self.map.sinks:
            self.go_down()
        
    def go_down(self):
        nv, ny, nx = self.get_auto_target()
        if self.map.cover_matrix[ny][nx] is not None:
            self.map.cover_matrix[ny][nx].prevs.append(self)
            self.next = self.map.cover_matrix[ny][nx]
        else: 
            self.next = Cell(self.map, ny, nx)
            self.next.prevs.append(self)
    
    def get_sink(self):
        if self.next:
            return self.next.get_sink()
        else:
            return self
    
    def mark_sign_to_all(self, sign):
        sink = self.get_sink()
        sink.go_up_with_sign(sign)
    
    def go_up_with_sign(self, sign):
        self.sign = sign
        for prev in self.prevs:
            prev.go_up_with_sign(sign)
    
    def get_auto_target(self):
        t,r,b,l = get_targets(self.map.map, self.y, self.x, self.map.Y, self.map.X)
        if t is not None and (t <= r or r is None) and (t <= b or b is None) and (t <= l or l is None):
            return (t, self.y-1, self.x)
        elif l is not None and (l <= r or r is None) and (l <= t or t is None) and (l <= b or b is None):
            return (l, self.y, self.x-1)
        elif r is not None and (r <= t or t is None) and (r <= b or b is None) and (r <= l or l is None):
            return (r, self.y, self.x+1)
        elif b is not None:
            return (b, self.y+1, self.x)
        
    def __str__(self):
        str = "[%d, %d]%s" % (self.x, self.y, "(%s)" % self.sign if self.sign else "")
        if self.next:
            str += " => %s" % self.next
        else:
            str += "."
        return str
        
class Map(object):
    def __init__(self, map, sinks, Y, X):
        self.map = map
        self.sinks = sinks
        self.Y = Y
        self.X = X
        self.cover_matrix = [[]]*Y
        for y in range(self.Y):
            self.cover_matrix[y] = [None]*self.X
    
    def fill_cover_magrix(self):
        for y in range(self.Y):
            for x in range(self.X):
                if self.cover_matrix[y][x] is None:
                    cell = Cell(self, y, x)
        
    def sign_them_all(self):
        letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
        sign = 0 
        for y in range(self.Y):
            for x in range(self.X):
                if self.cover_matrix[y][x].sign is None:
                    self.cover_matrix[y][x].mark_sign_to_all(letters[sign])
                    sign+=1
                    
    def __str__(self):
        str = ""
        for y in range(self.Y):
            for x in range(self.X):
                str += self.cover_matrix[y][x].sign
                if x != self.X-1:
                    str+=" "
            if y != self.Y-1:
                str += "\n"
        return str

def check(outfile, answer):
    out = open(outfile)
    ans = open(answer)
    assert out.read() == ans.read()
    ans.close()
    out.close()
    print "ok"

if __name__=="__main__":
    name = os.path.splitext(os.path.basename(__file__))[0]
    run("inputs/%s.in" % name, "outputs/%s.out" % name)
    #check("outputs/%s.out" % name, "outputs/%s.ans" % name)

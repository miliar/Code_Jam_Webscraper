class cookie_game():
    
    def __init__(self, c, f, x):
        self.c = float(c)
        self.f = float(f)
        self.x = float(x)
        self.d = 2.0
        
    def next_score(self):
        s = self.c / self.d
        self.d += self.f
        return (round(s,7) , round((self.x / self.d) , 7))

_in = open("B-small-attempt0.in", "r")
_out = open("B-small-attempt0.out", "wb");
_num_test_cases = int(_in.readline().strip())

for t in range(0,_num_test_cases):
    c,f,x = _in.readline().strip().split(" ")
    
    g = cookie_game(c, f, x)
   
    i = round(float(x) / 2.0, 7)
    s = g.next_score()
    
    if i == min(i, s[0] + s[1]):
        b = i
    else:
        a = s[0]
        b = a + s[1]
        s = g.next_score()
        while b > (a + s[0] + s[1]):
            a += s[0]
            b = a + s[1]
            s = g.next_score()
        
    _out.write("Case #%s: %s\r\n" %(t + 1, b))
_out.close()
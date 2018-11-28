class bot:
    
    def __init__(self,name):
	self.name = name
	self.curr = 1

    def move(self,s):
       	self.curr = s

    def movetime(self,button, time):
        req = self.ttm(button)
        
        if req > time :
            if button > self.curr:
                self.move(self.curr + time)
            else:
                self.move(self.curr - time)
        else:
            self.move(button)


    def ttm(self,s):
	t = abs(s - self.curr)+1
	return t

if __name__ == "__main__":
    
    fi = open("input", "r")
    fo = open("output", "w")

    tests = int(fi.readline())
    
    for test in range(tests):

        o = bot("Orange")
        b = bot("Blue")

        line = fi.readline()
        steps = line.split()

        n = steps[0]
        seq = steps[1:]
    
        tim = 0
    
        order = [x for x in seq if x.isalpha()]
        steps = [int(x) for x in seq if x.isdigit()]

        bcount = order.count("B")
        ocount = order.count("O")

        for i,s in enumerate(order):
            if s == "O":
                try:
                    t = o.ttm(steps[i])
                    tim += t
                    o.move(steps[i])
                    ocount -= 1
                    if bcount > 0:
                        b.movetime(steps[order.index("B",i)],t)
                except:
                    pass
                
            elif s == "B":
                try:
                    t = b.ttm(steps[i])
                    tim += t
                    b.move(steps[i])
                    bcount -= 1
                    if ocount > 0:
                        o.movetime(steps[order.index("O",i)],t)

                except:
                    pass

        fo.write( "Case #" + str(test+1) + ": " + str(tim) + "\n")

    fo.close()
    fi.close()

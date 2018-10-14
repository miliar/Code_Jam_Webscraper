import sys

class Robot:
    def __init__(self):
        self.seq = []
        self.pos = 1
        self.goal = None

    def next_goal(self):
        self.goal = self.seq and self.seq.pop(0) or None
    
    def move(self, count=None):
        pos = self.pos
        target = self.goal[1]
        if count is not None:
            if abs(target - pos) <= count:
                self.pos = target
            else:
                if target > pos:
                    self.pos += count
                else:
                    self.pos -= count
            return
        
        count = abs(target - pos) + 1 # +1 for button push
        self.pos = target
        self.next_goal()
        return count


def compute(data):
    a, b = Robot(), Robot()
    for i in range(0, len(data), 2):
        robot, button = data[i], int(data[i+1])
        if robot == 'O':
            a.seq.append((i, button))
        else:
            b.seq.append((i, button))
    
    time = 0
    a.next_goal()
    b.next_goal()
    while a.goal and b.goal:
        if b.goal[0] < a.goal[0]:
            a, b = b, a
        # a precedes b
        c = a.move()
        b.move(c)
        time += c
    while a.goal:
        time += a.move()
    while b.goal:
        time += b.move()
        
    return time


def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in range(1, T+1):
        data = f.readline().split()
        data.pop(0) # ignoring N
        print "Case #%d: %d" % (t, compute(data))

if __name__ == "__main__":
    main()
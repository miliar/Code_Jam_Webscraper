import time
import sys

class Robot:
    def __init__(self, color):
        self.state = 'ready'
        self.pos = 1
        self.queue = []
        self.color = color

    def run(self, working, tick):
        if not self.queue:
            # print self.color, 'Stay at button', self.pos
            return 'empty'

        f = self.queue[0]
        if working == f[0]:
            if self.pos == f[1]:
                # print self.color, 'Push button', self.pos
                del self.queue[0]
                return 'push'
            elif self.pos < f[1]:
                self.pos += 1
                # print self.color, 'Move to button', self.pos
            else:
                self.pos -= 1
                # print self.color, 'Move to button', self.pos
        else:
            if self.pos == f[1]:
                # print self.color, 'Stay at button', self.pos
                pass
            elif self.pos < f[1]:
                self.pos += 1
                # print self.color, 'Move to button', self.pos
            else:
                self.pos -= 1
                # print self.color, 'Move to button', self.pos

        return 'working'

def run(ro, rb):
    tick = 0
    working = 0

    while True:
        tick += 1
        # print tick
        a = ro.run(working, tick)
        b = rb.run(working, tick)

        if a == 'empty' and b == 'empty':
            break
        elif a == 'push' or b == 'push':
            working += 1

    return tick - 1

def readLine():
    return sys.stdin.readline()

def readInt():
    line = readLine()
    return int(line)

def main():
    t = readInt()
    for i in range(t):
        s = readLine()
        a = s.split()
        n = int(a[0])
        del a[0]

        ro = Robot('Orange')
        rb = Robot('Blue')

        for j in range(n):
            if a[2 * j] == 'O':
                ro.queue.append((j, int(a[2 * j + 1])))
            else:
                rb.queue.append((j, int(a[2 * j + 1])))

        ans = run(ro, rb)
        print 'Case #%d: %d' % (i + 1, ans)

if __name__ == '__main__':
    main()


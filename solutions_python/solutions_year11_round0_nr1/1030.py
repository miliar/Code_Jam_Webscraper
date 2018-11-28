class Robot(object):
    def __init__(self):
        self.pos = 1

    def move(self, n, button):
        for i in range(n):
            if self.pos > button:
                self.pos -= 1
            if self.pos < button:
                self.pos += 1

f = open('A-large.in')
of = open('A-large.out', 'w')

T = int(f.readline())
for i in range(T):
    orange = Robot()
    blue = Robot()
    bot = ''
    elapsed = 0
    total = 0
    sync = 0
    line = f.readline().split(' ')
    N = int(line.pop(0))

    for j in range(N):
        oldbot = bot
        bot = line.pop(0)
        button = int(line.pop(0))
        if bot == 'O':
            if oldbot <> bot:
                orange.move(sync, button)
                sync = 0
            if orange.pos == button:
                elapsed = 1
            else:
                elapsed = abs(button-orange.pos) + 1
                orange.pos = button
        if bot == 'B':
            if oldbot <> bot:
                blue.move(sync, button)
                sync = 0
            if blue.pos == button:
                elapsed = 1
            else:
                elapsed = abs(button-blue.pos) + 1
                blue.pos = button
        total += elapsed
        sync += elapsed

    of.write("Case #{0}: {1}\n".format(i+1, total))

f.close()
of.close()
                
        

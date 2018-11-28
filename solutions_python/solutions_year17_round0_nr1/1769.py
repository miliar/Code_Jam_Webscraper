class Grill():
    def __init__(self):
        self.pancakes = ""
        self.flipper_size = 0
        self.count = 0
        self.index = 0

    def put(self, stack, flipper_size):
        self.pancakes = stack 
        self.flipper_size = int(flipper_size)

    def get_pancakes(self):
        return self.pancakes

    def get_count(self):
        return self.count

    def try_flipping(self):
        length = len(self.pancakes)
        while (self.index < length):
            if self.pancakes[self.index] == "-" and length - self.index >= self.flipper_size:
                self.flip()
                self.count += 1
            else:
                pass
            self.index += 1

    def flip(self):
        pancakes_flipped = ""

        pancakes_start = self.pancakes[:self.index]
        pancakes_target = self.pancakes[self.index:self.index + self.flipper_size]
        pancakes_last = self.pancakes[self.index + self.flipper_size:]
        
        #print 'start: ' + pancakes_start + ', middle :' + pancakes_target + ', last :' + pancakes_last

        for pancake in pancakes_target:
            if pancake == "-":
                pancakes_flipped += "+"
            else:
                pancakes_flipped += "-"

        #print 'start: ' + pancakes_start + ', middle :' + pancakes_flipped + ', last :' + pancakes_last

        self.pancakes = pancakes_start + pancakes_flipped + pancakes_last
        #print self.pancakes

    def test(self):
        for pancake in self.pancakes:
            if pancake == '-':
                return False
        return True

count = 0
t = 0

read_file = open('large.in', 'r')
write_file = open('result.txt', 'w')
"""
3
---+-++- 3
+++++ 4
-+-+- 4
"""
for line in read_file:
    if count == 0:
        t = int(line.strip())
    else:
        S, K = line.strip().split(' ')
        grill = Grill()
        grill.put(S, K)
        grill.try_flipping()
        if grill.test():
            if count != t:
                write_file.write("Case #" + str(count) + ': ' + str(grill.get_count()) + '\n')
            else:
                write_file.write("Case #" + str(count) + ': ' + str(grill.get_count()))
        else:
            if count != t:
                write_file.write("Case #" + str(count) + ': IMPOSSIBLE' + '\n')
            else:
                write_file.write("Case #" + str(count) + ': IMPOSSIBLE')
    count += 1
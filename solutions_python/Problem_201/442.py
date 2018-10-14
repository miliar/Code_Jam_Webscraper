class Levels:

    def __init__(self, level, parent, val, bro):

        self.parent = parent
        self.level = level
        self.me = val
        self.bro = bro

        if(self.level in [0, 1]):
            self.count = 1

        else:
            if(self.parent.bro == self.parent.me):
                self.count = 2*self.parent.count

            elif((self.parent.bro // 2) % 2 == 0):
                self.count = self.parent.count + (2*(2**(level-1) - self.parent.count))
            else:
                self.count = self.parent.count

        if(self.me % 2 == 0):
            self.left = self.me//2
            self.right = self.me//2 - 1
        else:
            self.left = self.me//2
            self.right = self.me//2

        if(self.left % 2 == 0):
            self.even = self.left
            self.odd = self.right
        else:
            self.even = self.right
            self.odd = self.left


t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):

    inp = raw_input().split()
    num = int(inp[0])
    k = int(inp[1])

    #k=i
    #num=1000

    level = 0
    parent = None
    bro = None
    val = num

    while(2**level <= k):
        parent = Levels(level, parent, val, bro)
        bro = parent.odd
        val = parent.even
        level += 1

    #print val, bro, level, '\n' 
    if(level == 1):
        out = [parent.odd, parent.even]
        print "Case #{}: {} {}".format(i, max(out), min(out))
        continue

    level -= 1

    k -= (2**level - 1)
    me = parent.me
    bro = parent.bro
    if(me == bro):
        print "Case #{}: {} {}".format(i, max(parent.even, parent.odd), min(parent.odd, parent.even))
        continue

    if(me < bro):
        first_count = (2**level - parent.count)
        # print "####>",me, bro, level, first_count, parent.count, k, '\n'
        if(k <= first_count):
            print "Case #{}: {} {}".format(i, bro//2, bro//2)
        else:
            if(me//2 != 0):
                print "Case #{}: {} {}".format(i, me//2, me/2 - 1)
            else:
                print "Case #{}: {} {}".format(i, me//2, me/2)
        continue

    first_count = parent.count
    # print "--->",me, bro, level, first_count, parent.count, k, '\n'
    child = Levels(level+1, parent, parent.even, parent.odd)
    child_even_count = child.count

    if(k > first_count):
        print "Case #{}: {} {}".format(i, bro//2, bro//2)
    else:
        if(me//2 != 0):
            print "Case #{}: {} {}".format(i, me//2, me/2 - 1)
        else:
            print "Case #{}: {} {}".format(i, me//2, me/2)

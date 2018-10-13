import math

class Space:

    def __init__(self,num):
        self.num = num
        self.reps = 1
        self.ls = (num - 1) // 2
        self.rs = math.ceil((num - 1) / 2)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.num == other.num
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(self.num)

    def __str__(self):
        return str(self.num)+":" + str(self.reps)

    def __repr__(self):
        return str(self.num) + ":" + str(self.reps)


f = open('./C-small-2-attempt2.in', 'r')
w = open('./C-small-2-attempt2.out', 'w')
T = int(f.readline())
for i in range(T):
    line = f.readline()
    info = line.split(' ')
    N = int(info[0])
    K = int(info[1])

    current = {}
    current[N] = Space(N)
    nums = [N]
    lastls = -1
    lastrs = -1
    for k in range(K):
        maxspace = None
        for space_n in current:
            space = current[space_n]
            if maxspace is None or space.ls > maxspace.ls or (space.ls == maxspace.ls and space.rs > maxspace.rs):
                maxspace = space
        if(maxspace is None):
            maxrs=0
            maxls=0
            lastls = maxls
            lastrs = maxrs
            break
        else:
            maxrs = maxspace.rs
            maxls = maxspace.ls
        if maxspace.num == 2:
            new = Space(1)
            if new in current:
                current[1].reps += 1
            else:
                current[1] = new
        elif maxspace.num > 2:
            new = Space(maxrs)
            if maxrs in current:
                current[maxrs].reps += 1
            else:
                current[maxrs] = new
            new = Space(maxls)
            if maxls in current:
                current[maxls].reps += 1
            else:
                current[maxls] = new
        maxspace.reps -= 1
        if maxspace.reps == 0:
            del current[maxspace.num]
        lastls = maxls
        lastrs = maxrs
    w.write("Case #%i: %i %i\n" % (i + 1, lastrs, lastls))


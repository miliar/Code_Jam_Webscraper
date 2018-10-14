__author__ = 'forest'


class Opera:

    def __init__(self, aud):
        self.audience = []
        self.add_friend = 0

        for n in aud:
            self.audience.append(int(n))

        self.standing = self.audience.pop(0)

    def count(self):
        shy_level = 1

        for n in self.audience:
            if n is 0:
                shy_level += 1
                continue

            if shy_level <= self.standing:
                self.standing += n

            else:
                add = shy_level - self.standing
                self.standing += (add + n)
                self.add_friend += add

            shy_level += 1

        return self.add_friend


fr = open('A-large.in')
fw = open('A-large.out', 'w')

test_case = int(fr.readline())

for i in xrange(test_case):
    # print "case: %d" % i+1
    inputs = fr.readline()
    inputs = inputs.split()

    opera = Opera(inputs[1])
    fw.write("Case #%d: %d\n" % (i+1, opera.count()))

fw.close()




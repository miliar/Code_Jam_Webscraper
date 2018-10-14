class Pancake():
    def __init__(self, face):
        if face == "+":
            self.face = True
        else:
            self.face = False
    def flip(self):
        self.face = not self.face

T = int(raw_input())
for case in xrange(T):
    case_input = raw_input()
    seq, K = case_input.split()
    K = int(K)
    pancakes = []
    for elem in seq:
        pancakes.append(Pancake(elem))
    flips = 0
    for i in xrange(len(pancakes) - K + 1):
        if not pancakes[i].face:
            flips += 1
            for elem in pancakes[i:i+K]:
                elem.flip()
    possible = True
    for pancake in pancakes[-K:]:
        if not pancake.face:
            possible = False
            break
    if possible:
        print "Case #" + str(case + 1) + ": " + str(flips)
    else:
        print "Case #" + str(case + 1) + ": " + "IMPOSSIBLE"
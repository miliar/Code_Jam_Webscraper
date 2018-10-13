cases = input()

class Var:
    def __init__(self):
        self.value = None
    def __repr__(self):
        if (self.value):
            return str(self.value)
        else:
            return '_' + str(id(self))
        
for case in xrange(cases):
    k = input()
    deck = [ Var() for x in xrange(k) ]
    original_deck = list(deck)
    for i in xrange(k):
        if i != 0:
            pos = (i) % (len(deck))
            p1 = deck[0:pos]
            p2 = deck[pos:]
            deck = p2 + p1
        deck.pop(0).value = i + 1
    line = raw_input().split(' ')
    line.pop(0) # ignore
    result = ''
    for a in line:
        result += repr(original_deck[int(a) - 1]) + ' '
    print 'Case #' + str(case + 1) + ":", result.strip()
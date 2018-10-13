import unittest

def cut(s, size):
    for i in range(0, len(s), size):
        yield s[i:i + size]

def parse_combining(s):
    d = {}
    for mom, dad, kiddo in cut(s, 3):
        d[frozenset((mom, dad))] = kiddo
    return d

def parse_opposing(s):
    l = []
    for mom, dad in cut(s, 2):
        l.append(frozenset((mom, dad)))
    return l

def invoke(s, combining, opposing):
    combining_pairs = frozenset(combining.keys())
    opposing_pairs = frozenset(opposing)
    result = ""
    for c in s:
        result += c
#        print result
        while len(result) >= 2:
            pair = frozenset((result[-1], result[-2]))
            if pair in combining_pairs:
#                print "*", pair
                result = result[:-2] + combining[pair]
                continue
            fs = frozenset(result)
            for pair in opposing_pairs:
                if fs >= pair:
#                    print "**", pair
                    result = ""
                    continue
            break
    return result
    
class TestMagicka(unittest.TestCase):
    
    def assertInvoke(self, output, combining, opposing, input):
        c = parse_combining(combining)
        o = parse_opposing(opposing)
        self.assertEqual(output, invoke(input, c, o))

    def test_cut(self):        
        self.assertEqual(["12", "34", "56"], [s for s in cut("123456", 2)])

    def test_parse(self):        
        self.assertEqual({frozenset('QR'):'I'}, parse_combining("QRI"))

    def test_all(self):
        self.assertInvoke("EA", "", "", "EA")
        self.assertInvoke("RIR", "QRI", "", "RRQR")
        self.assertInvoke("FDT", "QFT", "QF", "FAQFDFQ")
        self.assertInvoke("ZERA", "EEZ", "QE", "QEEEERA")
        self.assertInvoke("", "", "QW", "QW")
        self.assertInvoke("", "", "QW", "WQ")
        self.assertInvoke("CF", "ABCDEF", "XY", "XYABDE")
        self.assertInvoke("G", "ABCDEFCFG", "XY", "XYABDE")

if __name__ == '__main__':
#    unittest.main()
    count = int(raw_input())
    for i in range(count):
        it = iter(raw_input().split(" "))
        combining = parse_combining(it.next() if int(it.next()) > 0 else "") 
        opposing = parse_opposing(it.next() if int(it.next()) > 0 else "")
        s = it.next() if int(it.next()) > 0 else ""
        print 'Case #%d: [%s]' % (i + 1, ", ".join(invoke(s, combining, opposing)))

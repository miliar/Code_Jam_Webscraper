
goog_to_eng = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z':'q'}

def go(goog_str):
    eng_chars = [goog_to_eng[ch] for ch in goog_str]
    return ''.join(eng_chars)

T = int(raw_input())
for i in range(T):
    line = raw_input()
    res = go(line)
    print 'Case #%i: %s' % (i + 1, res)
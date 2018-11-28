
def build_table(s):
    pos = {}
    for i in xrange(len(s)):
        c = s[i]
        if c in STR:
            if pos[c]:
                pos[c].append(i)
            else:
                pos[c] = [i]
    return pos

def count(text, pattern):
    if not pattern:
        return 1
    if not text:
        return 0
    if pattern[0] == text[0]:
        return count(text[1:], pattern[1:]) + count(text[1:], pattern)
    return count(text[1:], pattern)

def main():
    N = int(raw_input())
    STR = 'welcome to code jam'
    for case in xrange(N):
        text = raw_input()
        #pos = build_table(text)
        print 'Case #%d: %04d' % (case + 1, count(text, STR))

if __name__ == '__main__':
    main()

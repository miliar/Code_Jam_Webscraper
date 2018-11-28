import re

if __name__ == "__main__":
    ldn = raw_input()
    [l, d, n] = [int(x) for x in ldn.split(' ')]

    known_words = []
    for i in range(d):
        known_words.append(raw_input())

    for i in range(n):
        pattern = raw_input()
        pattern = re.sub('\(', '[', pattern)
        pattern = re.sub('\)', ']{1}', pattern)
        o = re.compile(pattern)
        matches = 0
        for word in known_words:
            if o.match(word):
                matches = matches + 1
        print 'Case #%d: %d' % (i+1, matches)


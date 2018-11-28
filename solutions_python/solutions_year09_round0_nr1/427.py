import re

l, d, n = [int(i) for i in raw_input().split(' ')]
words = []

if __name__ == '__main__':
    for i in range(d):
        words.append(raw_input())
    
    for i in range(n):
        regex = raw_input().replace('(', '[').replace(')', ']')
        nummatches = 0
        for word in words:
            if len(re.findall(regex, word)) > 0:
                nummatches += 1
        print 'Case #%d: %d' % (i + 1, nummatches)


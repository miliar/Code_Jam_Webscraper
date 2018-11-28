import re

def to_regular_expressions(patterns):
    for pattern in patterns:
        matches = re.findall('\(.+?\)', pattern)
        for match in matches:
            pattern = pattern.replace(match, '(%s)' % '|'.join(match[1:-1]))
        yield pattern

def find_matches(patterns, words):
    words = '\n'.join(words)
    for pattern in patterns:
        yield len(re.findall(pattern, words))

if __name__ == '__main__':
    with open('A-large.in') as fobj:
        input = fobj.read().split('\n')
    wordlength, wordcount, testcases = map(int, input.pop(0).split())
    words = input[:wordcount]
    patterns = to_regular_expressions(input[wordcount:wordcount+testcases])

    for index, n in enumerate(find_matches(patterns, words)):
        print "Case #%d: %d" % (index+1, n)

__author__ = 'pard'

def splitstring(s):
  result = [s]
  for i in range(1, len(s)):
    result.extend('%s %s' % (s[:i], x) for x in splitstring(s[i:]))
  return result.split()

def algorithm(string):
    import re
    word = string.split()[0]
    n = string.split()[1]

    # test = re.compile("(([b-df-hj-np-tv-z])(?!"+n+")){"+n+"}[b-df-hj-np-tv-z]")
    test = re.compile("([^aeiou]{"+n+"})")

    a = word

    # from  itertools import combinations
    # substrings = map(lambda i: a[i[0]:i[1]+1],combinations(range(len(a)), int(n)))

    # substrings = splitstring(a)

    # if len(a) == 1 and int(n) == 1:
    #     substrings = [ a ]
    # else:

    substrings = [ a[ index : index + length ] for index in range( len( a ) ) for length in range( int(n), len( a ) - index + 1 ) ]

    result = 0

    for string in substrings:
        matches = [ m for m in test.finditer(string) if m is not None ]
        if any(matches): result += 1

    return str(result)
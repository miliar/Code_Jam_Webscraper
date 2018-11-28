# input = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# de kr kd eoya kw aej tysr re ujdr lkgc jv'''

# output = '''our language is impossible to understand
# there are twenty six factorial possibilities
# so it is okay if you want to just give up'''

# mapper = {}

# for i in range(len(input)):
#     if input[i] not in mapper:
#         mapper[input[i]] = output[i]
mapper = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', '\n': '\n', ' ': ' '}
mapper['z'] = 'q'
mapper['q'] = 'z'

T = int(raw_input())
for i in xrange(T):
    caso = raw_input()
    traduc = ''.join([mapper[j] for j in caso])
    print "Case #%d: %s" % (i+1, traduc)

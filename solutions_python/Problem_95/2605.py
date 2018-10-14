keys   = 'abcdefghijklmnopqrstuvwxyz'
values = 'yhesocvxduiglbkrztnwjpfmaq'
dictionary = dict(zip(keys, values))

def translate(sentence):
    return ''.join(map(lambda k: dictionary.get(k, k), sentence))

count = int(raw_input())

for i in xrange(count):
    sentence = raw_input()
    print 'Case #{0}: {1}'.format(i+1, translate(sentence))

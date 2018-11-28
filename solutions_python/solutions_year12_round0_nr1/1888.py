

translator = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f':
        'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o':
        'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't':
        'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(the_dict, i):
    if i in the_dict:
        return the_dict[i]
    else:
        return i

t = int(raw_input())
for i in xrange(t):
    line_in = raw_input()
    line_out = ''.join([translate(translator, letter) for letter in line_in])
    print "Case #{0}: {1}".format(i+1, line_out)

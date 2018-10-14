lang = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q' }

def translate( word ):
    nword = []
    for i in word:
        if i in lang:
            nword.append( lang[i] )
        else:
            print i, 'undef'
            nword.append( i )
    return ''.join( nword )

def problem():
    data = file( 'in', 'r' ).readlines()
    test_count = int( data[0] )
    for index, i in enumerate( data[1: test_count + 1] ):
        print 'Case #%s: %s' % ( index + 1, translate(i) ),

if __name__ == "__main__":
    problem()

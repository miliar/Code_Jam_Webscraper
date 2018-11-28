import sys

def main(argv):
    cipher_msg = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    true_msg = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

    googlerese_dict = {}    
    for i in range(len(cipher_msg)):
        googlerese_dict[cipher_msg[i]] = true_msg[i]
    googlerese_dict['q'] = 'z'
    googlerese_dict['z'] = 'q'
        
    with open(argv[1], 'w') as outfile:
        with open(argv[0], 'r') as infile:
            T = int(infile.readline())
            for case in range(T):
                result = translate(googlerese_dict, infile.readline().strip()) 
                outfile.write('Case #%i: %s\n' % (case + 1, result))

def translate(dct, msg):
    _msg = [dct[i] for i in msg]
    return ''.join(_msg)
    
if __name__ == '__main__':
    main(sys.argv[1:])

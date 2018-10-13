import sys

mapper = {'a':'y',
        'b':'h',
        'c':'e',
        'd':'s',
        'e':'o',
        'f':'c',
        'g':'v',
        'h':'x',
        'i':'d',
        'j':'u',
        'k':'i',
        'l':'g',
        'm':'l',
        'n':'b',
        'o':'k',
        'p':'r',
        'q':'z',
        'r':'t',
        's':'n',
        't':'w',
        'u':'j',
        'v':'p',
        'w':'f',
        'x':'m',
        'y':'a',
        'z':'q',
        ' ':' '
        }

if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    i_file = open(input_filename,'r')
    o_file = open(output_filename,'w')
    n_cases = int(i_file.readline())
    for case in range(n_cases):
        line = i_file.readline().rstrip('\n')
        translated_line = ''.join([mapper[l] for l in line])
        o_file.write('Case #%d: %s\n' % (case+1, translated_line))

    i_file.close()
    o_file.close()


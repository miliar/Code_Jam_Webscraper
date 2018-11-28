__author__ = 'Janek Krukowski'

in1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
in2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
in3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

ot1 = 'our language is impossible to understand'
ot2 = 'there are twenty six factorial possibilities'
ot3 = 'so it is okay if you want to just give up'

def decode_line(line, mapping):
    out = ''
    for letter in line:
        out += mapping[letter]
    return out

def main():

    in_str = in1 + in2 + in3
    out_str = ot1 + ot2 + ot3

    mapping = {}
    for key, value in zip(in_str, out_str):
        mapping[key] = value

    mapping['z'] = 'q'
    mapping['q'] = 'z'
    mapping['\n'] = '\n'

    with open('A-small-attempt0.in', 'r') as input, open('output.OUT', 'w') as output:
        cases = int(input.readline())
        for i in xrange(cases):
            line = input.readline()
            out_line = decode_line(line, mapping)
            output.write('Case #{0}: {1}'.format(i+1, out_line))




if __name__ == '__main__':
    main()

from string import maketrans


def make_dict(sentences_1, sentences_2):
    d = dict()
    for sentence_1, sentence_2 in zip(sentences_1, sentences_2):
        for x, y in zip(sentence_1, sentence_2):
            d[x] = y

    return d

def maketran(durps, hurps):
    return maketrans(''.join(durps), ''.join(hurps))

def test():
    sentences_1 = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
                   'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                   'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    
    sentences_2 = ['our language is impossible to understand',
                    'there are twenty six factorial possibilities',
                    'so it is okay if you want to just give up']

    d = make_dict(sentences_1, sentences_2)

    for sen in sentences_1:
        print sen.translate(maketran(d.keys(), d.values()))

def open_file(filename):
    with open(filename) as f:
        data = [data.strip() for data in f.readlines()[1:]]
    return data

def write_output(data):
    with open('data.txt', 'w') as f:
        for i, d in enumerate(data):
            f.write('Case #{}: {}\n'.format(i+1, d))
        

def main():
    d = {' ': ' ',
         'a': 'y',
         'c': 'e',
         'b': 'h',
         'e': 'o',
         'd': 's',
         'g': 'v',
         'f': 'c',
         'i': 'd',
         'h': 'x',
         'k': 'i',
         'j': 'u',
         'm': 'l',
         'l': 'g',
         'o': 'k',
         'n': 'b',
         'p': 'r',
         's': 'n',
         'r': 't',
         'u': 'j',
         't': 'w',
         'w': 'f',
         'v': 'p',
         'y': 'a',
         'z' :'q',
         'q' : 'z',
         'x': 'm'}

    trans = maketran(d.keys(), d.values())

    data = open_file('A-small-attempt1.in')
    new_data = []
    
    for line in data:
        new_data.append(line.translate(trans))

    write_output(new_data)
    

main()

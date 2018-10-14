
def get_encoding(text1, text2):
    """
    Gets the inverse mapping given
    a text in the new language, and a text in the original.
    """
    language = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}
    for c1, c2 in zip(text1, text2):
        print c1, c2
        language[c1] = c2
    return language

f1 = open('input')
f2 = open('output')
text1 = ''.join([l.strip().replace(' ','') for l in f1.readlines()])
text2 = ''.join([l.strip().replace(' ','') for l in f2.readlines()])

language = get_encoding(text1, text2)
print language
"""
alphabet = [chr(i) for i in range(97,123)]
print alphabet
eng_set = set(alphabet)
for c in alphabet:
    if c not in language:
        print c
    else:
        eng_set.remove(language[c])
print eng_set
"""
def get_original_text(text, language):
    original = []
    for t in text:
        if t not in language:
            original.append(t)
        else:
            original.append(language[t])
    return ''.join(original)

in_file = open('A-small-attempt0.in')
output_file = open('tongues_out', 'w')
for i, line in enumerate(in_file.readlines()):
    if i==0:
        continue
    output_file.write('Case #%d'%(i) + ': ' + get_original_text(line, language))

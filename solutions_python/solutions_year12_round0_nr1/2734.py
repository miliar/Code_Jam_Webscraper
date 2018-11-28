training_input = (
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv',
    'y qee', # initial example
    'z', # only remaining mapping combination
)

training_output = (

    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up',
    'a zoo', # initial example
    'q', # only remaining mapping combination
)

def get_characters(sentences, remove_spaces=False):
    """
    Return a list of all characters contained in the supplied list of sentences.
    Order is preserved.
    Duplicates are not removed.
    """
    s = ''.join(sentences)
    if remove_spaces:
        s = s.replace(' ', '')
    return list(s)

def sanity_check(sentences):
    """
    Test if the available data is sufficient for mapping.
    This method does not return anything and will raise an error if the mapping is incomplete
    """
    # TODO: this method could be made into a unit test
    from sets import Set
    alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
    l = list(Set(get_characters(sentences, remove_spaces=True))) # list of unique character in input data

    for c in alphabet:
        if c not in l:
            raise StandardError

sanity_check(training_input)
sanity_check(training_output)

def create_mapping(input, output):
    mapping = {}

    input_chars = get_characters(input)
    output_chars = get_characters(output)

    if len(input_chars) != len(output_chars):
        # the input and output sentences must contain the same number of characters
        raise StandardError # TODO: make into a unit test

    for i in range(len(input_chars)):
        # loop over input/output and create input -> output map
        if mapping.has_key(input_chars[i]):
            continue
        mapping[input_chars[i]] = output_chars[i]

    return mapping

def map_sentence(sentence, mapping):
    return ''.join([mapping[character] for character in list(sentence)])

def load_data(fn):
    fp = open(fn, 'r')
    lines = fp.readlines()
    fp.close()
    lines = [x.replace('\n', '') for x in lines] # remove newline characters
    n = int(lines.pop(0))

    assert n == len(lines)

    return lines

def construct_output_lines(lines):
    output_lines = []
    for i in range(len(lines)):
        pre = 'Case #%i: ' % (i + 1) # text that precedes the output for each line
        output_lines.append(pre + lines[i] + '\r\n')
    return output_lines

def save_data(lines, fn):
    fp = open(fn, 'w')
    fp.writelines(lines)
    fp.close()


mapping = create_mapping(training_input, training_output)

FN_BASE = 'A-small-attempt0'

input_sentences =  load_data(FN_BASE+'.in')

output_sentences = [map_sentence(sentence, mapping) for sentence in input_sentences]

for sentence in output_sentences:
    print sentence

save_data(construct_output_lines(output_sentences), FN_BASE+'.out')

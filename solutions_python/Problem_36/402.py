import sys

def get_partial_count(seq, text):
    seq = seq.lower()
    text = text.lower()
    if len(text) == 1:
        counters = {}
        for i in range(len(seq)):
            counters[seq[i:]] = 0
        if counters.has_key(text):
            counters[text] = 1
        return counters
    else:
        counters = get_partial_count(seq, text[1:])
        subseqs = get_subseq(seq, text[0])
        if len(subseqs) > 0:
            new_counters = counters.copy()
            for ss in subseqs:
                if len(ss) <= 1:
                    new_counters[ss] += 1
                else:
                    new_counters[ss] = counters[ss] + counters[ss[1:]]
            return new_counters
        else:
            return counters
        
def get_subseq(sequ, letter, mapping_list={}):
    if len(mapping_list) == 0:
        index = 0
        for char in sequ:
            if mapping_list.has_key(char):
                mapping_list[char].add(sequ[index:])
            else:
                mapping_list[char] = set()
                mapping_list[char].add(sequ[index:])
            index += 1
    if mapping_list.has_key(letter):
        return mapping_list[letter]
    else:
        return set()

if __name__ == "__main__":
    input_file = sys.argv[1]
    data = open(input_file)
    cases = int(data.readline().strip())
    for i in range(cases):
        text = data.readline().strip()
        counters = get_partial_count('welcome to code jam', text)
        print "Case #%d: %04d" % (i+1, counters['welcome to code jam'] % 10000)
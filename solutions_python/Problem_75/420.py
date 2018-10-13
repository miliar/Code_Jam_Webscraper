#!/usr/bin/env python

def main(argv):
    # Parsing our file
    assert(len(argv) == 2)
    fname = argv[1]
    lines = None
    with open(fname) as fd:
        lines = fd.readlines()
    if not lines:
        return
    lines = lines[1:]
    lines = [line.split() for line in lines if len(line.strip())]
    for testid, test in enumerate(lines, start=1):
        combine_pairs_len = int(test[0])
        combine_pairs = test[1:1+combine_pairs_len]
        opposed_pairs_len = int(test[combine_pairs_len + 1])
        opposed_pairs = test[combine_pairs_len + 2:combine_pairs_len + 2 +opposed_pairs_len]
        sequence = test[-1]
        #Parse combine & opposeable pairs:
        combineable = [(set(tbase[:2]), tbase[2]) for tbase in combine_pairs]
        opposeable = [set(pair) for pair in opposed_pairs]
        elts = []
        # Process each element sequencialy
        for elt in sequence:
            prev_elt = '#' # invalid char
            if elts:
                prev_elt = elts.pop()
            formula = set([elt, prev_elt])
            # Find possible transformation
            transform = [result for (combine, result) in combineable if combine == formula]
            # Appends the result in the list
            if transform:
                elts.append(transform[0])
            else:
                if prev_elt != '#':
                    elts.append(prev_elt)
                elts.append(elt)
            # Find possbile opposite elements
            if [1 for opset in opposeable if opset <= set(elts)]:
                elts = []
        print 'Case #%d: [%s]' % (testid, ', '.join(elts))


if __name__ == "__main__":
    import sys
    main(sys.argv)


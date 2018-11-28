import string


TEST_CASES = {
    'y qee': 'a zoo',
    'ejp mysljylc kd kxveddknmc re jsicpdrysi':
         'our language is impossible to understand',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':
         'there are twenty six factorial possibilities',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv':
         'so it is okay if you want to just give up'
}


def maketrans_table():
    # Fill the translate table from the test cases given in the problem sample.
    translate_dict = {}
    for key, val in TEST_CASES.items():
        for c, t in zip(key, val):
            assert translate_dict.setdefault(c, t) == t, '%s != %s' % (c, t)

    # Check characters that don't have translation yet.
    rest_key = set(string.lowercase) - set(translate_dict.keys())
    rest_val = set(string.lowercase) - set(translate_dict.values())

    # If they the charcters left are bigger than 1 so we can't decide.
    if len(rest_key) > 1:
        raise ValueError("Too many value left to decide: %r" % rest_key)

    # Add the charcter left to the translation dictionary.
    translate_dict[rest_key.pop()] = rest_val.pop()

    return string.maketrans(
        ''.join(translate_dict.keys()),
        ''.join(translate_dict.values())
    )



def main():
    n = int(raw_input())
    table = maketrans_table()
    for i in range(n):
        print 'Case #%d: %s' % (i + 1, string.translate(raw_input(), table))


if __name__ == '__main__':
    main()

import string

mappings = {'a': 'y', 'o': 'e', 'z': 'q'}

known_sentences = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
]

for googlerese, english in known_sentences:
    for googlerese_char, english_char in zip(googlerese, english):
        if english_char != ' ':
            mappings[english_char] = googlerese_char

for last_english_letter in set(string.ascii_lowercase) - set(mappings.keys()):
    for last_googlerese_letter in set(string.ascii_lowercase) - set(mappings.values()):
        mappings[last_english_letter] = last_googlerese_letter


number_of_tests = int(raw_input())
googlerese_lines = [raw_input() for i in range(number_of_tests)]

translation = mappings.items()
translation = string.maketrans(
    [gc for ec, gc in translation], [ec for ec, gc in translation]
)

for i, line in enumerate(googlerese_lines):
    print "Case #%s: %s" % (i + 1, line.translate(translation))
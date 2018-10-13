
import itertools
from pprint import pprint

def equalize2(words):
    words.sort(key=len, reverse=True)
    last_word = None
    required_actions = 0
    for word in words:
        reduced_word = ""
        for ca, cb in itertools.zip_longest(word, word[1:]):
            # print(ca, cb)
            if ca != cb:
                reduced_word += ca
            else:
                required_actions += 1
        if last_word:
            if last_word != reduced_word:
                return None
        else:
            last_word = reduced_word
        print(word, reduced_word)
    return required_actions


def equalize(words):
    words.sort(key=len, reverse=True)
    actions = 0
    last_word = None
    last_word = None
    counted_words = []
    last_counted = []
    for word in words:
        c_word = ''
        counted_word = []
        for k, g in itertools.groupby(word):
            c_word += k
            counted_word.append(sum(1 for _ in g))

        if last_word:
            if last_word != c_word:
                return None
        else:
            last_word = c_word
        counted_words.append(counted_word)

        if last_counted:
            actions += sum(abs(a - b) for a, b in zip(last_counted, counted_word))

            counted_word = [min(a, b) for a, b in zip(last_counted, counted_word)]
        # print(word, counted_word)
        last_counted = counted_word

    # for p in itertools.combinations(counted_words, 2):
    #     print(p)
    # pprint(list(zip(*[iter(counted_words)] * 2)))
        # print(word, c_word, counted_word)
    #     c_word = ''
    #     c_count = []

    #     for c in word:
    #         if c_word and c_word[-1] == c:
    #             c_count[-1] += 1
    #         else:
    #             c_word += c
    #             c_count.append(1)

    #     if last_word:
    #         if last_word != c_word:
    #             return None
    #         # else:
    #         #     actions += sum(abs(a - b) for a, b in zip(last_counts, c_count))
    #     else:
    #         last_word = c_word
    #         # last_counts = c_count
    #     counts.append(c_count)

    #     print(word, c_word, c_count,actions)

    # for count in counts:
    #     for count in counts:


    return actions


with open('test.in') as fp, open('test.out', 'w+') as fo:
    T = int(fp.readline())
    for t in range(1, T + 1):
        N = int(fp.readline())
        words = [fp.readline().strip() for n in range(N)]
        result = equalize(words)
        if result is None:
            result = 'Fegla Won'
        s = "Case #%d: %s" % (t, result)
        print(s)
        fo.write(s + '\n')



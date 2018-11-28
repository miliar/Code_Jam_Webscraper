# problem a


def letter_counts(word):
    """ return list containing the number of consecutive occurrences of a
        letter

        e.g.
        "aabba" gives [2, 2, 1]
    """
    t = []
    letters = list(word)
    if len(word) == 0:
        return t
    t.append(1)
    last_letter = letters.pop()
    while not letters == []:
        current_letter = letters.pop()
        if current_letter == last_letter:
            t[len(t) - 1] += 1
        else:
            t.append(1)
        last_letter = current_letter
    t.reverse()
    return t


def shrink_word(word):
    letters = list(word)
    t = [letters[0]]
    if len(letters) <= 1:
        return t
    for pos in range(1, len(letters)):
        if letters[pos] != letters[pos - 1]:
            t.append(letters[pos])
    return t


def count_moves(words):
    for n in range(1, len(words)):
        if shrink_word(words[n]) != shrink_word(words[n-1]):
            return 'Fegla Won'
    counts = []
    for word in words:
        counts.append(letter_counts(word))
    word_base = shrink_word(words[0])
    average = []
    for n in range(len(word_base)):
        average.append(0)
        for j in range(len(words)):
            average[n] += counts[j][n]
        average[n] /= len(words)
    moves = 0
    for n in range(len(word_base)):
        for j in range(len(words)):
            moves += int(abs(counts[j][n] - average[n]))
    return str(moves)

for word_list in [['mmaw', 'maw'], ['gcj', 'cj'], ['aaabbb', 'ab', 'aabb'],
                 ['abc', 'abc'], ['aabc', 'abbc', 'abcc']]:
    print count_moves(word_list)


with open('A-small-attempt0.in.txt', 'r') as fin, open('A-small.out', 'w') as fout:
    T = int(fin.readline().split()[0])
    for case in range(T):
        n_words = int(fin.readline())
        words = []
        for n in range(n_words):
            word = fin.readline().strip()
            print word
            words.append(word)
        output = "Case #{0}: {1}".format((case + 1), count_moves(words))
        fout.write(output + '\n')

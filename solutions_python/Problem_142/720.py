__author__ = 'deniskrut'

# https://code.google.com/codejam/contest/2994486/dashboard#s=p0

import sys

t_num = int(sys.stdin.readline())
word_max_len = 100

for i in range(0, t_num):
    words_total_count = int(sys.stdin.readline())

    words = []
    for word_number in range(0, words_total_count):
        cur_word = sys.stdin.readline()
        words.append(cur_word)

    letters_count = [[0 for y in range(min(word_max_len, len(words[0])))] for x in range(words_total_count)]
    word_positions = [0] * words_total_count
    fegla_won = False
    letter_number = 0

    while (not word_positions[0] == len(words[0]) - 1) and (not fegla_won):
        cur_letter = words[0][word_positions[0]]
        for word_number in range(0, words_total_count):
            letter_count = 0
            while len(words[word_number]) > word_positions[word_number] and words[word_number][word_positions[word_number]] == cur_letter:
                letter_count += 1
                word_positions[word_number] += 1
            if letter_count == 0:
                fegla_won = True
                break
            letters_count[word_number][letter_number] = letter_count
        letter_number += 1

    for word_number in range(0, words_total_count):
        if len(words[word_number]) - 1 != word_positions[word_number]:
            fegla_won = True

    unique_letters_count = letter_number
    total_moves_count = 0
    if not fegla_won:
        for letter_number in range(0, unique_letters_count):
            min_moves_count = word_max_len
            for word_number_1 in range(0, words_total_count):
                move_others_count = 0
                for word_number_2 in range(0, words_total_count):
                    if word_number_1 == word_number_2:
                        continue
                    move_others_count += abs(letters_count[word_number_1][letter_number] - letters_count[word_number_2][letter_number])
                min_moves_count = min(min_moves_count, move_others_count)
            total_moves_count += min_moves_count

    res = total_moves_count
    if fegla_won:
        res = "Fegla Won"

    print "Case #" + str(i + 1) + ": " + str(res)
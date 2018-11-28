#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    (n_words,n_lists) = map(int,getline().split())

    all_words = []
    for i in range(n_words):
        word = getline()
        assert 1 <= len(word) <= 10
        all_words.append(word)
    assert len(all_words) == n_words

    lists = []
    for i in range(n_lists):
        llist = getline()
        assert len(llist) == 26
        lists.append(llist)
    assert len(lists) == n_lists

    # possible:
    # for each list,
    #    for each word,
    #        play the game, see how many points lost
    #    pick the word with the most points lost
    # probably too inefficient

    something = {}
    for word in all_words:
        board = '_' * len(word)
        something.setdefault( board, [] ).append(word)

    for (board, words) in something.items():
        trace('board:', board)
        for word in words:
            trace('    ', word)

    def blah(in_board, in_words, in_letters, in_score, in_level ):
        indent = '  ' * in_level
        trace()
        trace(indent, 'in_board:', in_board, '#in_words:', len(in_words), 'in_score:', in_score)
        if len(in_words) == 1:
            # Sean knows the word
            word = in_words[0]
            word_index = all_words.index(word)
            trace(indent, 'word', word, 'at index', word_index, 'has score', in_score)
            global worst_word, worst_word_index, worst_score_so_far
            if (
                in_score > worst_score_so_far
                or
                (
                    in_score == worst_score_so_far
                    and
                    word_index < worst_word_index
                )
            ):
                trace(indent, "    it's the new worst")
                worst_word = word
                worst_word_index = word_index
                worst_score_so_far = in_score
            return
        
        letter = in_letters[0]
        trace(indent, 'letter:', letter)
        out_letters = in_letters[1:]
        foo = {}
        some_word_has_letter = False
        for word in in_words:
            out_board = ''
            for (in_board_char, word_letter) in zip(in_board, word):
                if word_letter == letter:
                    out_board_char = letter
                    some_word_has_letter = True
                else:
                    out_board_char = in_board_char
                out_board += out_board_char
            trace(indent, 'word:', word, ' -> board:', out_board)
            foo.setdefault(out_board, []).append(word)

        if not some_word_has_letter:
            # no distinctions
            assert len(foo) == 1

        for (out_board, out_words) in foo.items():
            trace(indent, 'out_board:', out_board, 'for words:', ' '.join(out_words))
            if some_word_has_letter:
                # Sean asked for it
                if letter in out_board:
                    # it's in the word and we revealed all locations
                    out_score = in_score
                else:
                    # it's not in the word and Sean loses a point
                    out_score = in_score + 1
            else:
                # Sean didn't ask
                out_score = in_score
            blah(out_board, out_words, out_letters, out_score, in_level+1)


    worst_words = []
    for letters in lists:
        trace()
        trace('using list:', letters)
        worst_word = None
        worst_word_index = None
        worst_score_so_far = -1
        for (board, words) in something.items():
            blah(board, words, list(letters), 0, 0)
        worst_words.append(worst_word)

    print 'Case #%d: %s' % (case_num, ' '.join(worst_words))
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab

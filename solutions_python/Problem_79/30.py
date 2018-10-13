#!/usr/local/bin/python3

class UnpossibleWordException(Exception):
    pass

def guess(guessed, actual, dictionary, wordList, points):

    changed = True
    while changed:
        changed = False

        allChars = set(''.join(dictionary))
        newWordList = ''.join(w for w in wordList if w in allChars)
        if newWordList != wordList:
            changed = True
        wordList = newWordList

        for possibleWord in dictionary:
            try:
                for j, guessChar in enumerate(guessed):
                    checkChar = possibleWord[j]
                    if not (guessChar == checkChar or
                            (guessChar == '_' and checkChar in wordList)):
                        raise UnpossibleWordException()
            except UnpossibleWordException:
                changed = True
                dictionary.remove(possibleWord)

    # print(''.join(guessed), actual, dictionary, wordList, points, end=' ')

    assert len(dictionary)
    if len(dictionary) == 1:
        # print("found", actual, "in", points)
        return points
    letterToGuess = wordList[0]
    # print("guessing", letterToGuess)
    wordList = wordList[1:]

    pointChange = 1
    for i, c in enumerate(actual):
        if letterToGuess == c:
            pointChange = 0
            guessed[i] = letterToGuess

    points += pointChange

    return guess(guessed, actual, dictionary, wordList, points)

def solve(dictionary, wordLists):
    #print(wordLists)
    ret = []
    for wordList in wordLists:
        bestWord, bestScore = "OOPS, this shouldn't happen...", -1
        for word in dictionary:
            new_dic = [w for w in dictionary if len(w) == len(word)]
            score = guess(["_"] * len(word), word, new_dic, wordList, 0)
            if score > bestScore:
                bestWord = word
                bestScore = score
        ret.append(bestWord)
    return ' '.join(ret)

# Pp = previous percentage (might not be int)

# Pg = (Pp * (G - D) + Pd * D) / G
# D <= N
# G >= D

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    dictionary = [input() for i in range(N)]
    wordLists = [input() for i in range(M)]
    print("Case #{}: {}".format(i+1, solve(dictionary, wordLists)))


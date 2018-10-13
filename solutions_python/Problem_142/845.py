import sys


def input_generator():
    for line in sys.stdin:
        for token in line[:-1].split(' '):
            if token != '' or token:
                yield token

myin = input_generator()


def feglaWon(words):
    for word1 in words:
        for word2 in words:
            if getLetters(word1) != getLetters(word2):
                return True
    return False


def repeater(words):
    moves = 0
    wordCounts = []
    numOfLetters = len(getLetters(words[0]))
    for word in words:
        wordCounts.append(countConseqLetters(word))
    for i in range(numOfLetters):
        mean = 0
        for j in range(len(wordCounts)):
            mean += wordCounts[j][i]
        mean /= len(words)
        for j in range(len(wordCounts)):
            moves += abs(wordCounts[j][i] - mean)
    return moves


def countConseqLetters(word):
    letterCount = []
    count = 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            letterCount.append(count)
            count = 1
    letterCount.append(count)
    return letterCount


def countSameLetters(index, word):
    newIndex = index+1
    count = 1
    for i in range(index, len(word)-1):
        if word[i] is not word[i+1]:
            break
        count += 1
        newIndex += 1
    return (count, newIndex)


def getLetters(word):
    letters = [word[0]]
    for i in range(len(word)-1):
        if word[i] is not word[i+1]:
            letters.append(word[i+1])
    return letters



if __name__ == '__main__':
    tests = int(myin.next())
    for t in range(tests):
        num_words = int(myin.next())
        words = []
        for w in range(num_words):
            words.append(myin.next())
        if feglaWon(words):
            print 'Case #' + str(t+1) + ': Fegla Won'
        else:
            result = repeater(words)
            print 'Case #' + str(t+1) + ': ' + str(result)


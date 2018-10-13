import sys

def score(letters):
    j = 0
    while j < len(letters):
        if letters[j] == "B":
            k = 0
            while k < j:
                if letters[k] == "A":
                    letters[k] = "C"
                    letters[j] = "C"
                    break
                k += 1
        j += 1

    newLetters = []
    for s in letters:
        if not (s == "C"):
            newLetters.append(s)

    i = len(newLetters) - 1
    result = 0
    while i >= 0 and newLetters[i] == "A":
        i -= 1
        result += 1

    return result

def dscore(letters):
    result = 0
    j = len(letters) - 1
    while j >= 0:
        if letters[j] == "A":
            k = j - 1
            while k >= 0:
                if letters[k] == "B":
                    letters[k] = "C"
                    letters[j] = "C"
                    result += 1
                    break
                k -= 1
        j -= 1
    return result

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        n = int(sys.stdin.readline().strip())
        blocks = []
        arr = sys.stdin.readline().strip().split(" ")
        for s in arr:
            blocks.append((float(s.strip()), "A"))
        arr = sys.stdin.readline().strip().split(" ")
        for s in arr:
            blocks.append((float(s.strip()), "B"))
        blocks = sorted(blocks, key=lambda s : s[0])
        letters = []
        letters2 = []
        for (_, letter) in blocks:
            letters.append(letter)
            letters2.append(letter)

        war = score(letters)
        dwar = dscore(letters2)
        print "Case #%d: %d %d" % (i + 1, dwar, war)
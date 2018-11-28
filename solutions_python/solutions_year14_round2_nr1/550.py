import sys
import math

t = int(sys.stdin.readline())
for i in range(1, t+1):
    n = int(sys.stdin.readline())
    s = [[0]*n for i in range(103)]
    word = ""
    ok = True
    
    for j in range(n):
        line = sys.stdin.readline().strip()
        last = '-'
        count = [0]*26
        this_word = []
        k = 0
        for letter in line:
            if letter == last:
                s[k][j] += 1
            else:
                k += 1
                this_word.append(letter)
            last = letter
        new_word = "".join(this_word)
        if word != "" and new_word != word: ok = False
        else: word = new_word
    
    print("Case #" + str(i) + ":", end=" ")
    if not ok: print("Fegla Won")
    else:
        avg1 = [sum(s[i])//len(s[i]) for i in range(1, 103)]
        avg2 = [sum(s[i])//len(s[i]) + 1 for i in range(1, 103)]
        res1 = 0
        res2 = 0
        for j in range(n):
            for k in range(0, len(word)):
                res1 += abs(avg1[k] - s[k+1][j])
                res2 += abs(avg2[k] - s[k+1][j])
        print(min(res1, res2))
    
        
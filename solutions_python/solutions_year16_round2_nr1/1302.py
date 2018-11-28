import random

def go(word):
    mapp = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
    keys = ["ONE", "TWO", "SIX", "FOUR", "FIVE", "ZERO", "NINE", "THREE", "SEVEN", "EIGHT"]
    l_word = list(word)

    phone = ''
    while l_word:
        l_word = list(word)
        phone = ''
        for string_word in keys:
            while all(let in l_word for let in string_word):
                phone += str(mapp[string_word])
                for lit in string_word:
                    try:
                        p = l_word.index(lit)
                        del (l_word[p])
                    except:
                        continue
        random.shuffle(keys)
    phone = ''.join(sorted(phone))
    return phone

t = int(input())
for i in range(1, t + 1):
    boo = input()
    answer = go(boo)
    print("Case #{}: {}".format(i, answer))

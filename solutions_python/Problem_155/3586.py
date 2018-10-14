__author__ = 'aavu'

text = input()
t = int(text)
i = 0
while i < t:
    text = input()
    no = int(text[0])
    aud_str = list(text)
    aud_str.pop(0)
    aud_str.pop(0)
    aud = list({})
    for c in aud_str:
        aud.append(int(c))
    j = 0
    number = 0
    friends = 0

    for c in aud:
        number += c
        #print(number, c, j)
        while number < j+1:
            friends += 1
            number += 1
        j += 1
    print("Case #" + str(i + 1) + ": " + str(friends))
    i += 1
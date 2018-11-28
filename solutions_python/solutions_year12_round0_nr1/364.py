hints = {
    "a zoo": "y qee",
    "our language is impossible to understand": "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "there are twenty six factorial possibilities": "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "so it is okay if you want to just give up": "de kr kd eoya kw aej tysr re ujdr lkgc jv"}

letters = set("abcdefghijklmnopqrstuvwxyz ")

mapping = {}

for sentence, translation in hints.items():
    for c, d in zip(sentence, translation):
        mapping[d] = c

missing = (letters - set("".join(hints.keys()))).pop()
remaining = (letters - set("".join(hints.values()))).pop()

mapping[remaining] = missing

T = int(input())
for i in range(1, T + 1):
    sentence = input()
    translation = "".join(map(mapping.get, sentence))
    print("Case #%d: %s" % (i, translation))

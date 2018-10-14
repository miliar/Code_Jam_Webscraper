en = {"a": "y",
      "b": "n",
      "c": "f",
      "d": "i",
      "e": "c",
      "f": "w",
      "g": "l",
      "h": "b",
      "i": "k",
      "j": "u",
      "k": "o",
      "l": "m",
      "m": "x",
      "n": "s",
      "o": "e",
      "p": "v",
      "q": "z",
      "r": "p",
      "s": "d",
      "t": "r",
      "u": "j",
      "v": "g",
      "w": "t",
      "x": "h",
      "y": "a",
      "z": "q"}

de = {}
for k in en.keys():
    de[en[k]] = k

T = int(raw_input())
for t in xrange(T):
    G = raw_input()
    S = ""
    for c in G:
        if de.has_key(c):
            S += de[c]
        else:
            S += c
    print "Case #%i: %s" % (t+1, S)

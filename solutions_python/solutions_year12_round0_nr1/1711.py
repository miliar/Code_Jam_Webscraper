# ss = [
#     "our language is impossible to understand",
#     "there are twenty six factorial possibilities",
#     "so it is okay if you want to just give up",
# ]
# 
# ess = [
#     "ejp mysljylc kd kxveddknmc re jsicpdrysi",
#     "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
#     "de kr kd eoya kw aej tysr re ujdr lkgc jv",
# ]
# 
# dic = {"a": "y", "o": "e", "z": "q"}
# 
# for s, es in zip(ss, ess):
#     dic = dict(dic.items()+zip(s,es))

dic = {
    ' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v',
    'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k',
    'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f',
    'x': 'm', 'y': 'a', 'z': 'q'
}

# r_dic = {
#     ' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 
#     'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 
#     'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 
#     'x': 'h', 'z': 'q', 'q': 'z'
# }

f = open("A-small-attempt0.in")
lines = f.readlines()
f.close()

lines.pop(0)
case = 1
for line in lines:
    print "Case #%i: %s" % (case, "".join(map(lambda x: dic[x] if x != "\n" else "", line)))
    case += 1
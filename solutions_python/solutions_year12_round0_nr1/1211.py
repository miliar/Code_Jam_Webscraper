
from itertools import product

def get_words():
    with open("_words") as f_words:
        return set(line.strip().lower() for line in f_words)


def get_temp(word, _word):
    dct = {}
    for c, _c in zip(word, _word):
        if c in dct:
            if dct[c] == _c:
                continue
            else:
                return False, ""
        else:
            dct[c] = _c
    return True, set(dct.items())


def main():
    global all_count
    N = int(raw_input())
    M = []
    words = set()
    for i in range(N):
        line = raw_input()
        M.append(line)
        for word in line.split(' '):
            words.add(word)
        
    _words = get_words()
    _tmp = map(chr, range(97, 97 + 26))
    maybe = set((x,y) for x,y in product(_tmp, _tmp))
    dct_maybe = {}
    for c in _tmp:
        dct_maybe[c] = set()
    for i in range(1,15):
        i_words = filter(lambda x:len(x) == i, words)
        i__words = filter(lambda x:len(x) == i, _words)
        for word in i_words:
            st = set((x,y) for x,y in product(set(word), _tmp))
            for _word in i__words:
                ok, data = get_temp(word, _word)
                if ok and data.issubset(maybe):
                    st.difference_update(data)
            maybe.difference_update(st)
    print maybe , len(maybe)   
    for c, _c in maybe:
        dct_maybe[c].add(_c)

    mapping = {}
 
    while True:
        used = set()
        for c in _tmp:
            if c in dct_maybe and len(dct_maybe[c]) == 1:
                _c = list(dct_maybe[c])[0]
                mapping[c] = _c
                del dct_maybe[c]
                used.add(_c)
        if len(used) == 0:
            break
        for c in _tmp:
            if c in dct_maybe:
                dct_maybe[c].difference_update(used)
    
    x = 1
    for c in _tmp:
        if c in dct_maybe:
            x *= len(dct_maybe[c])
            print c, dct_maybe[c]
    print x
    
    mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'f': 'c', 'i': 'd', 'k': 'i',
               'j': 'u', 'm': 'l', 'l': 'g', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 't': 'w',
               'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'h' :'x', 'u':'j', 'g':'v','o':'k', 'q':'z', 'z':'q'}   
    
    with open("out", "w") as fout:
        for i, s in enumerate(M):
            result = "Case #{0}: {1}\n".format(i+1, ''.join(mapping.get(c, c if c == " "  else "({0})".format(c)) for c in s))
            fout.write(result)
            print result

if __name__ == "__main__":
    main()

                    
##            new_maybe = []
##            for mapping in maybe:
##
##                p = []
##                for i, c in enumerate(word):
##                    if c in runned:
##                        p.append((i, mapping[c]))
##                for _word in i__words:
##                    if all(_word[i] == c for i, c in p):
##                        new_mapping = dict(mapping)
##                        for j, c in enumerate(word):
##                            new_mapping[c] = _word[i]
##                        new_maybe.append(new_mapping)
##            for c in word:
##                if c not in runned:
##                    runned.append(c)

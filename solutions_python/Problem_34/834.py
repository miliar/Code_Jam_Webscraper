import cPickle
import sys

ALIEN_WORDS = {}

def memoize(function, limit=None):
    if isinstance(function, int):
        def memoize_wrapper(f):
            return memoize(f, function)

        return memoize_wrapper

    dict = {}
    list = []
    def memoize_wrapper(*args, **kwargs):
        key = cPickle.dumps((args, kwargs))
        try:
            list.append(list.pop(list.index(key)))
        except ValueError:
            dict[key] = function(*args, **kwargs)
            list.append(key)
            if limit is not None and len(list) > limit:
                del dict[list.pop(0)]

        return dict[key]

    memoize_wrapper._memoize_dict = dict
    memoize_wrapper._memoize_list = list
    memoize_wrapper._memoize_limit = limit
    memoize_wrapper._memoize_origfunc = function
    memoize_wrapper.func_name = function.func_name
    return memoize_wrapper

def addWord(word):
    curDict = ALIEN_WORDS
    for c in word: curDict = curDict.setdefault(c, {})

def findWords(pattern):
    @memoize
    def _group(pattern, words):
        group = pattern[1:pattern.find(")")]
        pattern = pattern[pattern.find(")") + 1:]
        return sum(_letter(c + pattern, words) for c in group)
    @memoize
    def _letter(pattern, words):
        # If we're done parsing the pattern we've found a match.
        if len(pattern) == 0: return 1
        if pattern[0] == "(": return _group(pattern, words)
        if pattern[0] not in words: return 0
        return _letter(pattern[1:], words[pattern[0]])
    return _letter(pattern, ALIEN_WORDS)
    
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ", sys.argv[0], " <filename>"
        exit()

    try:
        f = open(sys.argv[1])
        dict_items = int(f.readline().split()[1])
        for d in range(dict_items): addWord(f.readline()[:-1])
        for test, line in enumerate(f):
            line = line[:-1]
            print "Case #%d:" % (test + 1), findWords(line)
        f.close()
    except IOError, e:
        print "While opening input file:", str(e)

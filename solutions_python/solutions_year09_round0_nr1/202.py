
def split_pattern(pattern):
    while len(pattern)>0:
        if pattern.startswith("("):
            count = pattern.find(")")-1
            yield pattern[1:1+count]
            pattern = pattern[count+2:]
        else:
            yield pattern[0]
            pattern = pattern[1:]

def does_pattern_match(pattern, word):
    for i, letters in enumerate(split_pattern(pattern)):
        if word[i] not in letters:
            return False
    return True

def main():
    l, d, n = (int(s) for s in raw_input().strip().split(" "))

    wordlist = []
    for i in xrange(d):
        wordlist.append(raw_input().strip())

    patternlist = []
    for i in xrange(n):
        patternlist.append(raw_input().strip())

    #wordlist.sort()

    for i, pattern in enumerate(patternlist):
        count = sum(1 for word in wordlist if does_pattern_match(pattern, word))
        print "Case #"+str(i+1)+":", count

if __name__=="__main__":
    main()

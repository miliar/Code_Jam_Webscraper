import itertools
def solve(N, en, fr, sentences):
    """ solve the problem """

    #print(N, en, fr, sentences)
    #if N > 0:
    #    print(sentences[0])
    if N == 0:
        count = 0
        for item in en:
            if item in fr: 
                count += 1
        return count

    all = [i for i in itertools.product(['e', 'f'], repeat=N)]
    #print(len(all))
    #print(all)
    answers = []

    same = set([])
    for item in en:
        if item in fr: 
            same.add(item)

    en = set(item for item in en if item not in same)
    fr = set(item for item in fr if item not in same)
    for p in all:
        e = en.copy() 
        f = fr.copy()
        for i in range(N):
            if p[i] == 'e':
                for w in sentences[i]:
                    if w not in same:
                        e.add(w)
            elif p[i] == 'f':
                for w in sentences[i]:
                    if w not in same:
                        f.add(w)
            else:
                1/0
        count = 0
        for item in e:
            if item in f: count += 1
        #print(e, f, count)
        answers.append(count)
        

    return min(answers) + len(same)


def parse():
    """ parse input """

    N = int(input())
    en = set(i for i in input().split())
    fr = set(i for i in input().split())
    sentences = []
    for i in range(N-2):
        sentences.append(input().split())

    return N-2, en, fr, sentences


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()

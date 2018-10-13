import string
import sys

def find_permutation():
    sample_in  = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    sample_out = ["our language is impossible to understand",
                  "there are twenty six factorial possibilities",
                  "so it is okay if you want to just give up"]

    perm = {
            'a': 'y',
            'o': 'e',
            'z': 'q',
            'q': 'z'
           }

    for i in range(0, len(sample_in)):
        for j in range(0, len(sample_in[i])):
            perm[sample_in[i][j]] = sample_out[i][j]

    #rev_perm = dict()
    #for k in perm.keys():
    #    rev_perm[perm[k]] = k
    #
    #for k in string.ascii_lowercase:
    #    print("%s: %s" % (k, str(perm.get(k))))
    #
    #print(sorted(list(perm.values())))
    return ''.join(perm[k] for k in string.ascii_lowercase)

def main():
    #perm = find_permutation()
    perm = "yhesocvxduiglbkrztnwjpfmaq"
    table = string.maketrans(string.ascii_lowercase, perm)
    cases = int(raw_input())

    #for line in sys.stdin:
    for i in range(1, cases + 1):
        line = str(raw_input())
        print("Case #%s: %s" % (i, line.translate(table)))

if __name__ == "__main__":
    main()


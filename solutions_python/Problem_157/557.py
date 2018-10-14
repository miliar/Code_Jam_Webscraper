#!usr/bin/env
#encoding: utf-8

# sign -> +: 0, -:1
# 1
# i
# j
# k
#i^2=j^2=k^2=-1，ij=k， ji=-k， jk=i， kj=-i， ki=j， ik=-j
multiply = {
    (1, 1):     (0, 1),
    (1, 'i'):   (0, 'i'),
    (1, 'j'):   (0, 'j'),
    (1, 'k'):   (0, 'k'),
    ('i', 1):   (0, 'i'),
    ('i', 'i'): (1, 1),
    ('i', 'j'): (0, 'k'),
    ('i', 'k'): (1, 'j'),
    ('j', 1):   (0, 'j'),
    ('j', 'i'): (1, 'k'),
    ('j', 'j'): (1, 1),
    ('j', 'k'): (0, 'i'),
    ('k', 1):   (0, 'k'),
    ('k', 'i'): (0, 'j'),
    ('k', 'j'): (1, 'i'),
    ('k', 'k'): (1, 1),
};


def multiplyQuaternion(sign, p1, p2):
    r = multiply[(p1, p2)]
    return (r[0] ^ sign, r[1])


def ifPossible(string, count):
    strLen = len(string);
    length = strLen * count;
    split_i = False
    split_j = False
    split_k = False
    split_1 = False
    i = 0;
    p1 = 1;
    sign = 0
    while(i < length):
        sign, p1 = multiplyQuaternion(sign, p1, string[i%strLen]);
        if not split_i:
            if not sign and p1 == 'i':
                split_i = True
                p1 = 1
        elif not split_j:
            if not sign and p1 == 'j':
                split_j = True
                p1 = 1
        elif not split_k:
            if not sign and p1 == 'k':
                split_k = True
                p1 = 1
                split_1 = True
        else:
            split_1 = not sign and p1 == 1
        i += 1
    return split_1;

def run(inputFile, outputFile):
        fp = open(inputFile, 'r');
        fw = open(outputFile, 'w');

        caseCount = int(fp.readline());
        caseIndex = 0;
        while caseIndex < caseCount:
                caseIndex += 1;
                meta = fp.readline().split(' ');
                length, count = int(meta[0]), int(meta[-1]);
                string  = fp.readline().strip()[:length];
                result = ifPossible(string, count);
                if(result):
                        fw.write("Case #%d: %s\n"%(caseIndex, "YES"));
                else:
                        fw.write("Case #%d: %s\n"%(caseIndex, "NO"));

        fp.close();
        fw.close();

if(__name__ == "__main__"):
    run("in", "out")

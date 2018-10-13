def swap(seq, i):
    new = [];
    for q in range(len(seq)):
        if (q < i) or (q > i+1):
            new.append(seq[q]);
        if (q == i):
            new.append(seq[i+1]);
        if (q == i+1):
            new.append(seq[i]);
    return new;

    
def Valid(seq):
    for i in range(1, len(seq)-1):
        if (seq[i] < seq[i-1]) and (seq[i] < seq[i+1]):
            return i;
    return -1;
    
def Try(sequence):
#    print 'trying', sequence
    bad = Valid(sequence);
    if bad == -1:
        return 0;

    seq1 = swap(sequence, bad);
    seq2 = swap(sequence, bad-1);
    old1 = str(seq1) in StringList;
    old2 = str(seq2) in StringList;

    if (old1 and old2):
        return 1000000;
    if (old1 and not old2):
        StringList.append(str(seq2));
        return 1 + Try(seq2);
    if (old2 and not old1):
        StringList.append(str(seq1));
        return 1 + Try(seq1);
    
    StringList.append(str(seq1));
    StringList.append(str(seq2));

    return 1 + min( Try(seq1), Try(seq2) );

def Count(seq, index):
    Amax = max(seq);
    Pos = seq.index(Amax);
    curr = seq.index(max(seq));

    newseq = [];
    for e in seq:
        if e != Amax:
            newseq.append(e);

    newseq = newseq[:index] + [Amax] + newseq[index:];

    return abs(index-Pos) + Try(newseq);


def Binary(n, N):
    ret = [];
    for z in range(N):
        ret.append(n%2);
        n /= 2;
    return ret;


def MakeTargetList(seq):
    Amax = max(seq);
    LIST = []
    newseq = [];
    for e in seq:
        if e != Amax:
            newseq.append(e);
    newseq.sort();

    N = len(newseq);

    for i in range(2**N):
        bin = Binary(i, N);
#        print i, bin;
        parta = [];
        partb = [];
        for e in range(N):
            if bin[e] == 0:
                parta.append(newseq[e]);
            else:
                partb.append(newseq[e]);
        parta.sort();
        partb.sort();
        partb.reverse();
        LIST.append( parta + [Amax] + partb );
    return LIST;
        

#print 'woo';
#print MakeTargetList([1,2,3]);

def Shuffle(seq1, seq2):
    ret = 0;
    for e in seq1:
        ret += seq2.index(e);
        seq2.remove(e);
    return ret;

T = int(raw_input());
for q in range(T):
    StringList = [];
    print "Case #%d:" % (q+1),;

    N = int(raw_input());
    Ai = map(int, raw_input().split());
    Ans = [];

    Targets = MakeTargetList(Ai);
    for target in Targets:
        Ans.append(Shuffle(Ai, target));

    print min(Ans);
#    print Try(Ai);
#    Ans = [];
#    for i in range(N):
#        Ans.append( Count(Ai, i) );
#
##    print Ans;
#    print min(Ans);

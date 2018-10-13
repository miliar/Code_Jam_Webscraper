import pdb
import sys

cypher = [
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
]

plain = [
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
]

def get_mapping():

    cmap = {' ':' ','q':'z','z':'q'}

    # test for collisions ?
    for pl,cl in zip(plain,cypher):
        for pw,cw in zip(pl.split(),cl.split()):
            d = dict(zip(list(pw),list(cw)))
            cmap.update(d)
            assert len(pw) == len(cw)

    assert len(cmap) == 27

    return dict([(v,k) for k,v in cmap.items()])

def translate(cypher_text,cmap):
    return ''.join(cmap[k] for k in list(cypher_text))


if __name__ == '__main__':
    cmap = get_mapping()
    f = open(sys.argv[1],"r")
    cases = int(f.next().strip())
    lines = zip(range(1,cases+1), [ f.next().strip() for x in range(cases) ])
    for i,l in lines:
        print "Case #%d: %s" % (i, translate(l,cmap))


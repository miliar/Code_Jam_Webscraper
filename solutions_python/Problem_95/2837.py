MAP = dict(zip('ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qeeEJP MYSLJYLC KD KXVEDDKNMC RE JSICPDRYSIRBCPC YPC RTCSRA DKH WYFREPKYM VEDDKNKMKRKCDDE KR KD EOYA KW AEJ TYSR RE UJDR LKGC JVY QEEz', 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zooOUR LANGUAGE IS IMPOSSIBLE TO UNDERSTANDTHERE ARE TWENTY SIX FACTORIAL POSSIBILITIESSO IT IS OKAY IF YOU WANT TO JUST GIVE UPA ZOOq"'))

INPUT ="""3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
OUTPUT ="""\
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""

def translate(s):
    return "\n".join(
        "Case #%d: %s" % (i, "".join(map(lambda x: MAP.get(x, 'FUCK' + x), line)))
        for i, line in list(enumerate(s.split('\n')))[1:-1]) + '\n'

assert translate(INPUT) == OUTPUT
if __name__ == '__main__':
    import sys
    print translate(open(sys.argv[1]).read()),

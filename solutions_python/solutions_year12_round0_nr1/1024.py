import string

orig = 'ejp mysljylc kd kxveddknmc re jsicpdrysi;rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd;de kr kd eoya kw aej tysr re ujdr lkgc jv;yeqz'
tran = 'our language is impossible to understand;there are twenty six factorial possibilities;so it is okay if you want to just give up;aozq'

t = string.maketrans(orig, tran)

def tr(text):
    print text
    ret = string.translate(text, t)
    print ret
    print
    return ret

def solve(filename='sample.inp'):
    fi = open(filename)
    fo = open(filename+'.out', 'w')
    fi.readline()
    for i,line in enumerate(fi):
        line = line.rstrip('\n')
        fo.write('Case #%d: %s\n'%(i+1, tr(line)))
    fo.close()
    fi.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv)>1:
        solve(sys.argv[1])
    else:
        solve()

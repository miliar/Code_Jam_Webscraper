# -*- coding: utf-8 -*-

def process_one_case(case):
    cl,ol,s=case
    cr={}
    cc={}
    for cs in cl:
        cr[cs[0]]=cs[2]
        cr[cs[1]]=cs[2]
        cc[cs[0]]=cs[1]
        cc[cs[1]]=cs[0]
    oc={}
    for o in ol:
        oc[o[0]]=o[1]
        oc[o[1]]=o[0]

    ct=''
    ot={}
    osl=''
    for c in s:
        if ct == c:
            ccc=cc[c]
            if ccc in oc:
                toc=oc[cc[c]]
                if toc in ot:
                    ot[toc]-=1
            osl=osl[:-1]+cr[c]
            ct=''
        elif c in ot and ot[c] > 0:
            osl=''
            ot={}
            ct=''
        else:
            if c in cc:
                ct=cc[c]
            else:
                ct=''
            if c in oc:
                occ=oc[c]
                if occ in ot:
                    ot[occ]+=1
                else:
                    ot[occ]=1
            osl+=c
    
    return '['+(', '.join(osl))+']'

def get_one_case(ifs):
    ln=0
    for line in ifs:
        ln+=1
        if ln == 1:
            continue
        line=line.strip()
        if not line:
            continue
        dl=line.split()
        c=int(dl[0])
        cl=dl[1:c+1]
        o=int(dl[c+1])
        ol=dl[c+2:c+o+2]
        s=dl[-1]
        yield(cl,ol,s)
            

def main(argv):
    ifs=open(argv[0],'r')
    ofs=open(argv[0][:-2]+'out','w')
    cc=1
    for case in get_one_case(ifs):
        r=process_one_case(case)
        ofs.write('Case #%d: %s\n'%(cc,r))
        cc+=1
    ofs.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# -*- coding: utf-8 -*-


def process_one_case(case):
    cp=1
    op=1
    ot=0
    ct=0
    cf=case[0][0]
    for f,p in case:
        p=int(p)
        if cf==f:
            ct+=abs(p-cp)+1
            cp=p
        else:
            ot+=abs(p-op)+1
            if ot > ct:
                t=ot
                ot=ct
                ct=t

            else:
                ot=ct+1
                t=ct
                ct=ot
                ot=t
            cf=f
            op=cp
            cp=p
    return str(ct)
                
        
    

def get_one_case(ifs):
    ln=0
    for line in ifs:
        line=line.strip()
        ln+=1
        if ln == 1:
            continue
        if not line:
            continue
        dl=line.split()
        yield zip(dl[1::2],dl[2::2])

def main(argv):
    ifs=open(argv[0],'r')
    ofs=open(argv[0][:-2]+'out','w')
    cc=1    
    for case in get_one_case(ifs):
        r=process_one_case(case)
        ofs.write('Case #%d: %s\n'%(cc,r))
        cc+=1
    print cc-1
    ofs.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

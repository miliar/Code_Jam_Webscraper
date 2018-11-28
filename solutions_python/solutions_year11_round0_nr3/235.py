# -*- coding: utf-8 -*-

def process_one_case(case):
    minn = case[0]
    t=0
    sumn=0
    for n in case:
        t=t^n
        sumn+=n
        if n<minn:
            minn=n
    if t:
        return 'NO'
    else:
        return str(sumn-minn)

def get_one_case(ifs):
    ln=0
    ifs.readline()
    line=ifs.readline()
    while len(line) > 0:
        line = line.strip()
        d=ifs.readline().strip()
        yield map(int,d.split())
        line = ifs.readline()

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

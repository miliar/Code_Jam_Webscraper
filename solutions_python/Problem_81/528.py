# -*- coding: utf-8 -*-

def process_one_case(case):
    n,wm=case
    wp=[]
    owp=[]
    oowp=[]
    for wstr in wm:
        tn=0
        tw=0
        for i in range(n):
            if wstr[i]=='.':
                continue
            tn+=1
            if wstr[i]=='1':
                tw+=1
        if tn != 0:
            wp.append(float(tw)/float(tn))
        else:
            wp.append(0.0)
    for i in range(n):
        tn=0
        tw=0.0
        for j in range(n):
            if wm[i][j]=='.':
                continue
            ttn=0
            ttw=0
            for k in range(n):
                if k==i or wm[j][k]=='.':
                    continue
                ttn+=1
                if wm[j][k]=='1':
                    ttw+=1
            if ttn != 0:
                tw+=float(ttw)/float(ttn)
            tn+=1
        if tn !=0:
            owp.append(tw/tn)
        else:
            owp.append(0)
    for wstr in wm:
        tn=0
        tw=0.0
        for i in range(n):
            if wstr[i]=='.':
                continue
            tn+=1
            tw+=owp[i]
        if tn !=0:
            oowp.append(tw/tn)
        else:
            oowp.append(0)
    ostr=''
    for i in range(n):
        ostr+="\n"+str(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])
    return ostr
                
        
    

def get_one_case(ifs):
    ln=0
    line=ifs.readline()
    line=ifs.readline()
    while len(line)>0:
        line=line.strip()
        if len(line)==0:
            break
        n=int(line)
        wm=[]
        for i in range(n):
            line=ifs.readline().strip()
            wm.append(line)
        yield n,wm
        line=ifs.readline()

def main(argv):
    ifs=open(argv[0],'r')
    ofs=open(argv[0][:-2]+'out','w')
    cc=1    
    for case in get_one_case(ifs):
        r=process_one_case(case)
        ofs.write('Case #%d: %s\n'%(cc,r))
        cc+=1
    print cc
    ofs.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

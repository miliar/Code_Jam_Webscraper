
if __name__ == '__main__':
    f = open('c:\\C-small-attempt0.in')
    fout = open('c:\\result.out', 'w')

    search_str = 'welcome to code jam'
    ccase = int(f.readline().strip())
    print ccase
    for icase in range(ccase):
        str_in = f.readline().strip()
        print str_in
        len_in = len(str_in)
        len_srh = len(search_str)
        cb=range(len_srh)
        rs = 0
        step = 0
        next=True
        while next:
            isFound = False
            while cb[step]<=len_in-len_srh+step:
                if str_in[cb[step]] != search_str[step]:
                    cb[step]+=1
                else:
                    isFound = True
                    break
            if not isFound:
                if step==0:
                    break
                step-=1
                cb[step]+=1
                continue
            if step == len_srh-1:
                rs+=1
                cb[step]+=1
            else:
                step+=1
                cb[step]=cb[step-1]+1
        fout.write('Case #%d: %04d\n'%(icase+1, rs))
        print 'Case #%d: %04d'%(icase+1, rs)
    f.close()
    fout.close()
        
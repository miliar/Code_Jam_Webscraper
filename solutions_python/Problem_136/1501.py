def main():
    T = int(raw_input())
    for TIME in range(T):
        case=[]
        line = raw_input().split(' ')
        cps = 2.0
        time=0.0
        for i in line:
            case.append(float(i))
        while(True):
            completet=case[2]/cps
            farmt=case[0]/cps
            farmcomplete = farmt+case[2]/(cps+case[1])
            if completet < farmcomplete:
                time+= completet
                break
            else:
                time+=farmt
                cps+=case[1]

        print 'Case #%d: %f'%(TIME+1,time)



if __name__=='__main__':
    main()

def read():
    return map(int,raw_input().split())


def work(cases,(N,K)):
    print "Case #%d: %s"%(cases,"ON" if (1<<N)-1==K%(1<<N) else "OFF")


for i in range(int(raw_input())):
    work(i+1,read())

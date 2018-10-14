import datetime

def get_dateobjs(dep, arr,t):
    h,m = dep.split(':')
    depobj = datetime.datetime(2008,06,18,int(h),int(m))
    h,m = arr.split(':')
    arrobj = datetime.datetime(2008,06,18,int(h),int(m))
    arrobj = arrobj + datetime.timedelta(minutes=int(t))
    return depobj,arrobj

tcs = input()
for ip in range(tcs):
    t = input()
    na,nb = (int(x) for x in raw_input().split(' '))
    tablea = []
    for i in range(na):
        d,a = raw_input().split()
        tablea.append(list(get_dateobjs(d,a,t)))
    tableb = []
    for i in range(nb):
        d,a = raw_input().split()
        tableb.append(list(get_dateobjs(d,a,t)))
    nta = len(tablea)
    ntb = len(tableb)

    dep_time_at_a = [x[0] for x in tablea]
    arr_time_at_b = [x[1] for x in tablea]

    dep_time_at_b = [x[0] for x in tableb]
    arr_time_at_a = [x[1] for x in tableb]

    dep_time_at_a.sort()
    arr_time_at_b.sort()
    dep_time_at_b.sort()
    arr_time_at_a.sort()

    for x in dep_time_at_a:
        for i in range(len(arr_time_at_a)):
            if x >= arr_time_at_a[i]:
                if not nta == 0:
                    nta = nta -1
                    arr_time_at_a =arr_time_at_a[i+1:]
            break

    for x in dep_time_at_b:
        for i in range(len(arr_time_at_b)):
            if x >= arr_time_at_b[i]:
                if not ntb == 0:
                    ntb = ntb - 1
                    arr_time_at_b = arr_time_at_b[i+1:]
            break

    print 'Case #%d: %d %d' % (ip+1,nta,ntb)

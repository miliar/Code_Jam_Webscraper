#!/usr/bin/env python

def run(go_arr, back_arr, ttime):
    
    def run_back(time):
        for x in back_arr:
            if time <= x[0]:
                back_arr.remove(x)
                run_go(x[1] + ttime)
                return
        
    def run_go(time):
        for x in go_arr:
            if time <= x[0]:
                go_arr.remove(x)
                run_back(x[1] + ttime)
                return

    s1 = 0
    s2 = 0
    while(go_arr or back_arr):
        arr = go_arr + back_arr
        t = min(arr)
        if t in go_arr:
            run_go(t[0])
            s1 += 1
        else:
            run_back(t[0])
            s2 += 1

    return (s1, s2)

def parse_time(strtime):
    stime = strtime.split(' ')
    return (int(stime[0][0:2]) * 60 + int(stime[0][3:5]),
            int(stime[1][0:2]) * 60 + int(stime[1][3:5]))

def main():
    caseno = int(raw_input())
    for i in range(caseno):
        ttime = int(raw_input())
        n1, n2 = [int(x) for x in raw_input().split(' ')]
        go_arr = []
        back_arr = []
        
        for j in range(n1):
            go_arr.append(parse_time(raw_input()))
        for j in range(n2):
            back_arr.append(parse_time(raw_input()))

        go_arr.sort()
        back_arr.sort()
        res = run(go_arr, back_arr, ttime)
        print 'Case #%d: %d %d'%(i + 1, res[0], res[1])

if __name__ == '__main__':
    main()
    
    

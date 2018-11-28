#-*- coding:utf-8 -*-


def main():

    T = int(raw_input())
    for i in xrange(1, T+1):
        num, peoples = raw_input().split()
        res = 0
        temp = 0
        cur = 0
        for s in peoples:
            if cur != 0:
                need_num = cur
                # print "need_num", need_num
                # print "temp", temp
                if temp < need_num:
                    res = res + (need_num - temp)
                    temp = need_num
            temp = temp + int(s)
            cur = cur + 1
        print "Case #"+str(i)+": "+str(res)
    return

if __name__ == "__main__":
    main()

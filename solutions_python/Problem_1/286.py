#!/usr/bin/env python

def contain(x, arr):
    for t in arr:
        if x in t:
            return t
    return None

def count_eng(eng_arr, arr):

    def count():
        fake_arr = []
        for x in arr:
            if (x in eng_arr) and (x not in fake_arr):
                fake_arr.append(x)
            #if t and (t not in fake_arr):
            #    fake_arr.append(t)
            if len(fake_arr) == len(eng_arr):
                yield
                fake_arr = [x]
    cc = 0
    ct = count()
    try:
        while(True):
            ct.next()
            cc += 1
    except StopIteration:
        pass
    return cc

def main():
    caseno = int(raw_input())
    for i in range(caseno):
        eng_no = int(raw_input())
        eng_arr = []
        for j in range(eng_no):
            eng_arr.append(raw_input())
        arr_no = int(raw_input())
        arr = []
        for j in range(arr_no):
            arr.append(raw_input())
        print 'Case #%d: %d' % (i + 1, count_eng(eng_arr, arr))

if __name__ == '__main__':
    main()

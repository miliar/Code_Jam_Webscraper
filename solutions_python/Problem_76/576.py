#! /usr/bin/env python
# -*- coding: utf8 -*-
# vim:ts=4:sw=4:expandtab:
# vi:ts=4:sw=4

def calc_sum(elems):
    retval = 0
    for v in elems:
        retval += v
    return retval

def calc_xor(elems):
    retval = 0
    for v in elems:
        retval ^= v
    return retval

def do_calc(elems):
    elem_len = len(elems)
    def dfs(i, elem_sum, elem_xor, result):
        if i == elem_len:
            if ( len(elem_sum) == 0 ) or ( len(elem_xor) == 0 ):
                return -1
            sum_val = calc_sum(elem_sum)
            if sum_val < result:
                return -1
#            print elem_sum, elem_xor,
            if calc_xor(elem_sum) == calc_xor(elem_xor):
#                print sum_val
                return sum_val
            else:
#                print -1
                return -1
        tmp_sum = elem_sum[:]
        tmp_xor = elem_xor[:]
        tmp_sum.append(elems[i])
        tmp_xor.append(elems[i])
        result = max(result,dfs( i+1, elem_sum, tmp_xor, result))
        result = max(result,dfs( i+1, tmp_sum, elem_xor, result))
        return result

    result_sum = dfs(0,[],[],-1)        

    return result_sum


def main():
    for c in range(input()):
        n = int(input())
        elems = map(int, raw_input().split())[:n]

        result = do_calc(elems)

        if result < 0:
            print 'Case #%d: NO' % ( c+1 )
        else:
            print 'Case #%d: %d' % ( c+1, result )

if __name__ == '__main__':
    main()

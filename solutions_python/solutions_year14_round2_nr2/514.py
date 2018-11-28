# Encoding: utf-8
'''
Created on 26.04.2014

@author: Los

@version: 0.0.1
'''
import sys

def input_int():
    return int(input())

def input_float():
    return float(input())

def input_str():
    return input().strip()

def input_list_int():
    return list(map(int, tuple(input().split())))

def input_list_float():
    return list(map(float, tuple(input().split())))

def main(argv=None):
    if argv is None:
        argv=sys.argv

    import locale
    locale.setlocale(locale.LC_ALL, '')
    
    CASE_NUM=input_int()
    
    for case_num in range(CASE_NUM):
        
        A, B, K = map(int, tuple(input().split()))
        
        count=0
        for r1 in range(0, A):
            for r2 in range(0, B):
                r0 = r1 & r2
                if r0 < K :
                    count+=1
        
    
        print('Case #{0}: {1}'.format(case_num+1, count))
        


if __name__ == '__main__':
    main()

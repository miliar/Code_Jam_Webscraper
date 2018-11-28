# Encoding: utf-8
'''
Created on 26.04.2014

@author: Los

@version: 0.0.1
'''
import sys
#import re

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
        N=input_int()
        strings=list()
        for i in range(N):
            strings.append(input_str())
        flag=True
        chars=list()
        last_ch=''
        for ch in strings[0]:
            if ch != last_ch:
                chars.append(ch)
                last_ch=ch
        #print(chars)
        flag=True
        steps=0
        for ch in chars:
            #print('ch: {0}'.format(ch))
            blocks=list()
            for s in strings:
                count=0
                if len(s)==0:
                    res='Fegla Won'
                    flag=False
                    break
        
                for c in s:
                    #print('c==ch {0}=={1}'.format(c,ch))
                    if c==ch:
                        count+=1
                    else:
                        break
                if count==0:
                    res='Fegla Won'
                    flag=False
                    break
                else:
                    blocks.append(count)
            if not flag:
                break
            #print(blocks)
            for i in range(len(strings)):
                strings[i]=strings[i][blocks[i]:]

            med=int(sum(blocks)/len(blocks)+0.5)
            while (min(blocks)!=max(blocks)) and flag:
                for i in range(len(blocks)):
                    if blocks[i]<med:
                        blocks[i]+=1
                        steps+=1
                    elif blocks[i]>med:
                        blocks[i]-=1
                        steps+=1
            if not flag:
                break
        for s in strings:
            if len(s)>0 :
                res='Fegla Won'
                flag=False
                break
        if flag:
            print('Case #{0}: {1}'.format(case_num+1, steps))
        else:
            print('Case #{0}: {1}'.format(case_num+1, res))
        


if __name__ == '__main__':
    main()

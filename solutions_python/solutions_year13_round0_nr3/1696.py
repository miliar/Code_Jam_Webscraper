
import copy
import sys
import math

class Log():
    def __init__(self, debug=False):
        self.debug = debug

    def info(self, fmt, *args):
        if self.debug:
            print fmt % args



def ispali(num):
    st = str(num)
    l = len(st)
    first = 0
    second = 0
    ans = False
    
    if l == 1:
        return True
    if l%2 == 0:
        first = l/2
        second = first
        first -= 1
    else:
        first = l/2
        second = first
    
    while first >= 0:
        if st[first] == st[second]:
            first -= 1
            second += 1
            ans = True
        else:
            ans = False
            break
    return ans 

def reverse(st):
    st = str(st)
    nst = ''
    for i in st:
        nst = i + nst
    return nst

def new_pali(l):
    nz = l-2
    z = nz * '0'
    return '1' + z  + '1'

def high_pali(num):
    if ispali(num):
        return next_pali(num)
    num = str(num)
    l = len(num)
    
    if l%2 == 0:
        mid = l /2
        mid -= 1
        f_half = int(num[:mid+1])
        s_half = int(num[mid+1:])
        rev_fhalf = int(reverse(f_half))
        log.info( "%d %d", rev_fhalf , f_half)
        if rev_fhalf >= s_half:
            return str(f_half) + str(rev_fhalf)
        else:
            f_half += 1
            return str(f_half) + str( reverse(f_half))
    else:
        mid = l/2
        f_half = int(num[:mid])
        s_half = int(num[mid+1:])
        log.info("%s %s", f_half, s_half)
        rev_fhalf = int(reverse(f_half))
        log.info( "%d %d", rev_fhalf , s_half)
        if rev_fhalf >= s_half:
            return str(num[:mid+1]) + str(rev_fhalf)
        else:
            new_f_half = int(num[:mid+1]) + 1
            return str(new_f_half) + str( reverse(f_half))
    return ans
    
        
def next_pali(num):
    num = str(num)
    l = len(num)
    if l == 1:
        if num == '9':
            return new_pali(2)
        else:
            ans = int(num) + 1
            return ans
    
    if num == str( '9' * l):
        return new_pali(l +1)
          
    if l%2 == 0:
        mid = l /2
        mid -= 1
        new_num = int(num[:mid+1])
        new_num += 1
        new_st = str(new_num)
        rev_new = reverse(  new_st)        
        ans = str(new_st) + rev_new
        
    else:
        mid = l/2
        new_num = int(num[:mid+1])
        new_num += 1
        new_st = str(new_num)
        rev_new = reverse(  new_st[:-1])        
        ans = str(new_st) + rev_new
    return ans
    
    


a = []

    
def solve(N, M):
    sqr_n = int(math.sqrt(N-1))
    ans = 0
    total_pali = 0
    pali = int(high_pali(sqr_n))
    sq_pali = pali * pali   
    while sq_pali <= M:
        #log.info("checking for %d %d %s",pali,sq_pali,ispali(sq_pali))
        if sq_pali >= N and ispali(sq_pali):
            a.append(sq_pali)
            ans += 1
        pali = int(next_pali(pali))
        sq_pali = pali * pali   
        total_pali += 1
    log.info("total pali %d", total_pali)
    #return ans

def search(num):
    start = 0
    end = len(a)-1
    while start < end:
        mid = start + (end -start)/2
        if a[mid] >= num:
            end = mid
        else:
            start = mid+1
    return start
    
    
def csolve(N, M):
    start = search(N)
    end = search(M)
    ans = 0
    if a[end] == M:
        return end - start + 1
    else:
        return end - start
    
import time                                                                                                                         
log = Log(0)    
if __name__ == '__main__':
    case = int(raw_input())
    solve(1, 1000000000000000)
    for i in range(1, case+1):
        NM = raw_input().split()
        N = int(NM[0])
        M = int(NM[1])
        ans = csolve(N, M)
        print "Case #%d: %s"%(i, ans)

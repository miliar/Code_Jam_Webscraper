import math
def rev(s):
    l = len(s)
    ans = ""
    for i in range(l - 1, -1, -1):
        ans += s[i]
    return ans
def test(x):
    st = str(long(x) * long(x))
    rs = rev(st)
    if st == rs:
        return True;
    return False;
def cal_odd(n):
    if n == 1: return 4
    if n == 3: return 5
    ret = 0
    ans = [0] * n
    all = n / 2 - 1
    ans[0] = 1
    ALL = 1 << all
#    for i in xrange(ALL):
 #       index = 1
  #      for j in xrange(all - 1, -1, -1):
   #         if (1 << j) & i:
    #            ans[index] = 1
     #       else: ans[index] = 0
      #      index += 1
       # k = -1
        #for j in xrange(n / 2):
         #   ans[k] = ans[j]
          #  k -= 1
        #ans[n / 2] = 0
        #if test(long("".join(map(str, ans)))):
         #   ret += 1
        #ans[n / 2] = 1
        #if test(long("".join(map(str, ans)))):
         #   ret += 1
        #ans[n / 2] = 2 
        #if test(long("".join(map(str, ans)))):
         #   ret += 1
    ret = ALL * 3 - 1
    for i in xrange(n): ans[i] = 1
    ans[n / 2] = 2
    if test(long("".join(map(str, ans)))):
        ret += 1    
    for i in xrange(n): ans[i] = 0
    ans[0] = 2; ans[n - 1] = 2
    if test(long("".join(map(str, ans)))):
        ret += 1    
    ans[n / 2] = 1
    if test(long("".join(map(str, ans)))):
        ret += 1
    return ret
def cal_even(n):
    if n == 2: return 2
    if n == 4: return 3
    ret = 0
    ans = [0] * n
    all = n / 2 - 1
    ans[0] = 1
    ALL = 1 << all
  #  for i in xrange(ALL):
   #     index = 1
    #    for j in xrange(all - 1, -1, -1):
     #       if (1 << j) & i:
      #          ans[index] = 1
       #     else: ans[index] = 0
        #    index += 1
   #     k = -1
    #    for j in xrange(n / 2):
     #       ans[k] = ans[j]
      #      k -= 1    
       # if test(long("".join(map(str, ans)))):
        #    ret += 1
    ret = ALL
    for i in xrange(n): ans[i] = 0
    ans[0] = 2; ans[n - 1] = 2   
    if test(long("".join(map(str, ans)))):
        ret += 1
    return ret
d = []
def init():
    for i in xrange(1,51):
        if i & 1:
            d.append(cal_odd(i))
        else:
            d.append(cal_even(i))
    return
def cal(s):
    lens = len(s)
    if lens == 1:
        if s >= '3': return 4
        elif s >= '2': return 3
        elif s >= '1': return 2
        elif s >= '0': return 1
        else : return 0
    elif lens == 2:
        if s >= '22': return 2
        elif s >= '11': return 1
        else: return 0
    if(s[0] > '2'): return d[lens - 1];
    ans = [0] * lens
    if lens & 1:
        if s[0] == '2':
            ans[0] = ans[-1] = 2
            ans[lens / 2] = 1
            tmp = long(s)
            t1 = long("".join(map(str, ans)))
            ans[lens / 2] = 0
            t2 = long("".join(map(str, ans)))
            if tmp >= t1:
                return d[lens - 1]
            elif tmp >= t2:
                return d[lens - 1] - 1L
            else : return d[lens - 1] - 2L
        else:
            t = s[1:lens/2 + 1]
            h = ""
            for i in xrange(len(t) - 1):
                if t[i] == '0':
                    h += '0'
                else:
                    h += '1'
            sum = 0L
            for i in xrange(len(h)):
                sum = sum * 2 + long(h[i])
            sum = (sum) * 3;
            p = long(s)
            v1 = '1' + h + '0' + h + '1'
            v2 = '1' + h + '1' + h + '1'
            v3 = '1' + h + '2' + h + '1'
            sumv1 = long(v1)
            sumv2 = long(v2)
            sumv3 = long(v3)
            if p >= sumv3: sum += 3
            elif p >= sumv2: sum += 2
            elif p >= sumv1: sum += 1
            return sum
    else:
        if s[0] == '2':
            for i in xrange(len(ans)):
                ans[i] = 0
            ans[0] = ans[-1] = 2
            tmp = long(s)
            t = long("".join(map(str, ans)))
            if tmp >= t:
                return d[lens - 1]
            else: return d[lens - 1] - 1L
        else:
            t = s[1:lens / 2]
            h = ""
            for i in xrange(len(t) - 1):
                if t[i] == '0':
                    h += '0'
                else:
                    h += '1'
            sum = 0L
            for i in xrange(len(h)):
                sum = sum * 2 + long(h[i])
            v = '1' + h + rev(h) + '1'
            sumv = long(v)
            p = long(s)
            if p >= sumv:
                return sum + 1
            else:
                return sum
def main():
    init()
    T = input()
    for kase in xrange(1, T + 1):
        AA, BB = map(long,raw_input().split())
        SAA = long(math.sqrt(AA) + 0.000001)
        SBB = long(math.sqrt(BB) + 0.000001)
        SAA = SAA - 1L if SAA * SAA == AA else SAA 
        A = str(SAA)
        B = str(SBB)
        lenA = len(A)
        lenB = len(B)
        ans = 0L
        for i in xrange(lenA + 1, lenB - 1):
            ans += d[i]
        if lenA == lenB:
            ans += cal(B) - cal(A)
        else:
            ans += cal(B) + d[lenA - 1] - cal(A)
        print "Case #" + str(kase) + ":", ans
if __name__ == '__main__':
    main()
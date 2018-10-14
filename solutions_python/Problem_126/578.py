'''
Created on May 12, 2013

@author: kon
'''
import template



def solve(f):
    T = int(f.readline())
    res = []
    
    vowels = {'a','e','i','o','u'}

    consonants = set()
    for c in range(ord('a'), ord('z')+1):
        if chr(c) not in vowels:
            consonants.add(chr(c))
            
    def count(s,n):
        res = 0
        cnt = 0
        cs = 0
        for c in s:
            if c in consonants:
                cs +=1
            else:
                cs = 0
            cnt +=1
            if cs == n:
                res += (cnt-n+1)*(len(s)+1-cnt)
                res += count(s[cnt-n+1:],n)
                break
        return res
    for _ in range(T):
        A, B = f.readline().split()
        res.append(str(count(A, int(B))))
    f.close()
    return res

if __name__ == '__main__':
    template.solve("test.in", solve)
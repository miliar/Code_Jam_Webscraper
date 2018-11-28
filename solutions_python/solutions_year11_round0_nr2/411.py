import sys, time, math

def Find( u, v, s ):
    for i in range(len(s)):
        if s[i][0]==u and s[i][1]==v: return s[i][2]
        if s[i][0]==v and s[i][1]==u: return s[i][2]
    return []

def Ok( u, v, s ):
    for i in range(len(s)):
        if s[i][0]==u and s[i][1]==v: return True
        if s[i][0]==v and s[i][1]==u: return True
    return False

def Base( u ):
    return u=='Q' or u=='W' or u=='E' or u=='R' or u=='A' or u=='S' or u=='D' or u=='F'

def main():  # gcj 2011 round 0 A
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        CDN = (input()).split()

        C = int(CDN[0])
        cs = CDN[1:C+1]
        
        D = int(CDN[C+1])
        ds = CDN[C+2:C+D+2]

        N = int(CDN[C+D+2])
        s = CDN[C+D+3]
        
        st, end = 0, len(s)
        while st<end:
            if st==0:
                st = 1
                continue
            new = Find( s[st-1], s[st], cs )
            if new!=[]:
                ts = s[0:st-1]+new+s[st+1:end]
                s = ts
                end = end-1
                continue
            
            for i in range(st-1,-1,-1):
                if Ok( s[i], s[st], ds ):
                    ts = s[st+1:end]
                    #ts = s[0:ii]+s[st+1:end]
                    s = ts
                    st, end = 0, len(s)
                    #st, end = ii, len(s)
                    break
            else:
                st = st+1

        print("Case #",case+1,": [",sep='',end='')
        for i in range(len(s)):
            print(s[i],end='')
            if i!=len(s)-1: print(', ',end='')
        print(']')

    return 0


if __name__ == '__main__':
    main()

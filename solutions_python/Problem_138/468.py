'''
Code jam 2014: D. Deceitful War
'''
def main():
    f = open('/home/ayush/D-large.in','r')
    o = open("/home/ayush/Downloads/output.txt",'w')
    t=int(f.readline())
    k=0
    while t:
        t-=1
        k+=1
        deceitfulscore=0
        warscore=0
        n = f.readline()
        nw = map(float,f.readline().split())
        kw = map(float,f.readline().split())
        nw.sort();kw.sort()
        nw_war=nw[:];kw_war=kw[:]
        while len(nw)!=0:
            if nw[0] < kw[0]:
                nw.pop(0);kw.pop(-1)
            else:
                deceitfulscore+=1
                nw.pop(0);kw.pop(0)
        while len(nw_war)!=0:
            if nw_war[-1] > kw_war[-1]:
                nw_war.pop(-1);kw_war.pop(0)
                warscore+=1
            else:
                nw_war.pop(-1);kw_war.pop(-1)
        s = 'Case #%d: %d %d\n' %(k,deceitfulscore,warscore)
        o.write(s)
        
        
main()

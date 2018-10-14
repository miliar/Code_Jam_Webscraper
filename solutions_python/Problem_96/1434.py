'''
Created on 2012-4-14

@author: mzh.li
'''

if __name__ == '__main__':
    with open('B-large.in', 'r') as fi, open('Blarge.output','w') as fo:
        lines = int(fi.readline());
        for i in range(1,lines + 1):
            l = fi.readline()
            l = l.split()
            print(l)
            l = [int(a) for a in l]
            print(l)
            N = l[0]
            S = l[1]
            P = l[2]
            max = 0
            for s in l[3:]:
                if 0 == s % 3 and s / 3 >= P:
                    max += 1
                elif s >= 2 and 0 == (s + 1) % 3 and (s + 1) / 3 >= P:
                    max += 1
                elif s >= 1 and 0 == (s - 1) % 3 and (s - 1) / 3 + 1 >= P:
                    max += 1
                elif S > 0:
                    if s >= 3 and 0 == s % 3 and s / 3 + 1 >= P:
                        S -= 1
                        max += 1
                    elif s >= 4 == (s + 2) % 3 and (s + 2) / 3 >= P:
                        S -= 1
                        max += 1
                    elif s >= 2 and 0 == (s - 2) % 3 and (s - 2) / 3 + 2 >= P:
                        S -= 1
                        max += 1
            if i !=lines:
                fo.write("Case #%d: %d\n"%(i,max))
            else:
                fo.write("Case #%d: %d"%(i,max))
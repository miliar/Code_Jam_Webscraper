# B.py

import sys
import os

def main():
    s = map(int, ''.join(sys.stdin.readlines()).split())
    os.close(0)

    T = s[0]
    s = s[1:]
    for i in range(1,T+1):
        N = s[0]
        Pd = s[1]
        Pg = s[2]
        s = s[3:]
        if (Pg == 100 or Pg == 0) and Pg != Pd:
            print "Case #" + str(i) + ": Broken"
            continue
        if Pd == 100 or Pd == 0 or N >= 10000:
            print "Case #" + str(i) + ": Possible"
            continue
        for j in range(1,N):
            if (j * 100) / Pd <= N and (j * 100) % Pd == 0:
                print "Case #" + str(i) + ": Possible"
                break
        else:
            print "Case #" + str(i) + ": Broken"

if __name__ == "__main__":
 	main()

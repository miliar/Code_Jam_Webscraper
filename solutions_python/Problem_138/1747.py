#!/usr/bin/env python
import sys

    

def main():
    f = sys.stdin
    cases = int(f.readline())
    for case in range(1, cases+1):
        blocks = int(f.readline())
        naomi_blks = [float(b) for b in f.readline().split(" ")]
        naomi_blks.sort()
        naomi_blks_2 = naomi_blks[:]
        ken_blks = [float(b) for b in f.readline().split(" ")]
        ken_blks.sort()
        ken_blks_2 = ken_blks[:]
        # print naomi_blks
        # print ken_blks
        points_deceitful = 0
        points_optimal = 0
        
        while len(naomi_blks) > 0:
            naomi = naomi_blks.pop()
            ken = -1
            for b in reversed(ken_blks):
                if b > naomi:
                    ken = b
                    
            if ken == -1:
                ken = ken_blks[0]

            if (naomi > ken):
                points_optimal += 1

            ken_blks.remove(ken)

        
        while len(naomi_blks_2) > 0:
            naomi_told = max(ken_blks_2) - 0.001
            ken = -1
            for b in ken_blks_2:
                if b > naomi_told:
                    ken = b
                    
            if ken == -1:
                ken = ken_blks_2[0]

            naomi = -1
            for b in reversed(naomi_blks_2):
                if b > ken and b not in ken_blks_2:
                    naomi = b
            if naomi == -1:
                naomi = naomi_blks_2[0]

                
            if (naomi > ken):
                points_deceitful += 1

            # print
            # print naomi_told
            # print naomi
            # print ken
                
            assert naomi > ken if naomi_told > ken else True
            

            ken_blks_2.remove(ken)
            naomi_blks_2.remove(naomi)
            
        print "Case #%s: %s %s" % (case, points_deceitful, points_optimal)
            
if __name__ == "__main__":
    main()

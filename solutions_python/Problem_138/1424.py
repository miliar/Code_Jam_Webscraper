#!usr/bin/python

import sys

with open(sys.argv[1],"r") as inf:
    with open(sys.argv[2],"w") as outf:
        if inf and outf:
            # get num of cases
            T = int(inf.readline().strip())
            # parse inputs per case
            def getValues():
                size = int(inf.readline().strip())
                N = [float(i) for i in inf.readline().strip().split(" ")]
                K = [float(i) for i in inf.readline().strip().split(" ")]
                return size, N, K
            
            for t in range(1,T+1):
                nBlocks, Nao, Ken = getValues()
                Nao.sort(reverse=True)
                Ken.sort(reverse=True)
                agaNao = Nao[:]
                agaKen = Ken[:]
                ### war of lies ###
                scoreLie = 0
                # trim off Ken's bigger end
                while( Ken and Nao and (Ken[0] > Nao[0]) ):
                    del Ken[0]
                    del Nao[-1]
                # remove ken's smallest and nao's smallest
                n = len(Nao)-1
                k = n
                while( n >= 0 and k >= 0 ):
                    if( Nao[n] > Ken[k] ):
                        del Nao[n]
                        del Ken[k]
                        n-=1
                        k-=1
                        scoreLie+=1
                    else:
                        n-=1

                del Ken
                del Nao #safety

                ### war of truth ###
                scoreTruthKen = 0
                n = len(agaNao)-1
                k = n
                while( n >= 0 and k >= 0 ):
                    if( agaKen[k] > agaNao[n] ):
                        del agaNao[n]
                        del agaKen[k]
                        n-=1
                        k-=1
                        scoreTruthKen+=1
                    else:
                        k-=1

                # print submission
                outf.write("Case #%d: %d %d\n" % (t, scoreLie, (nBlocks-scoreTruthKen)))

            #END for T
        #END inf and outf
    #END open outf
#END open inf

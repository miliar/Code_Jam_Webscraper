try:
        fi=open("A-large.in","r")#Input File
        fo=open("A-large.out","w")#Output File
        T=int(fi.readline())
        for case in range(1,T+1,1):
                input=fi.readline()
                N=int(input[0:input.find(" ")])
                K=int(input[input.find(" ")+1:])
                if K %(2**N)==(2**N-1):
                        fo.write("Case #"+str(case)+": ON\n")
                else:
                        fo.write("Case #"+str(case)+": OFF\n")
except:
        print("Input File Not Found")

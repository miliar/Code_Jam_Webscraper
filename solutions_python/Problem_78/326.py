import copy

def function(fi,fo):
    f = open(fi)
    f2 = open(fo,"w")
    cases = int(f.readline())
    
    for nc,case in enumerate(range(cases)):
        test = f.readline()[0:-1].split(" ")
        # ----------------------------------
        # Code here
        # ---------------------------------
        N = int(test[0])
        Pd = int(test[1])
        Pg = int(test[2])
        text = "Possible"
        if Pd == 0:
            if Pg == 100:
                text = "Broken"
        if Pd == 100:
            if Pg == 0:
                text = "Broken"
        if 0 < Pd < 100:
            if Pg == 100:    
                text = "Broken"
            if Pg == 0:
                text = "Broken"
            if 0<Pg<100:
                text = "Broken"
                for i in range(1,N+1):
                    D = float(Pd)/100*i
                    if D == int(D):
                        text = "Possible"
                        break
        text = "Case #" + str(nc+1) + ": "  + text
        f2.write(text + "\n")
        

#function("test.in","test.txt")
function("short.in","short.txt")
#function("long.in","long.txt")


T=int(raw_input(""))
for i in range(T):


    G=str(raw_input(""))
    S=""
    for l in G:
        Sl=""
        
        if(l=="a"):
            sl="y"
        if(l=="b"):
            sl="h"
        if(l=="c"):
            sl="e"
        if(l=="d"):
            sl="s"
        if(l=="e"):
            sl="o"
        if(l=="f"):
            sl="c"
        if(l=="g"):
            sl="v"
        if(l=="h"):
            sl="x"
        if(l=="i"):
            sl="d"
        if(l=="j"):
            sl="u"
        if(l=="k"):
            sl="i"
        if(l=="l"):
            sl="g"
        if(l=="m"):
            sl="l"
        if(l=="n"):
            sl="b"
        if(l=="o"):
            sl="k"
        if(l=="p"):
            sl="r"
        if(l=="q"):
            sl="z"
        if(l=="r"):
            sl="t"
        if(l=="s"):
            sl="n"
        if(l=="t"):
            sl="w"
        if(l=="u"):
            sl="j"
        if(l=="v"):
            sl="p"
        if(l=="w"):
            sl="f"
        if(l=="x"):
            sl="m"
        if(l=="y"):
            sl="a"
        if(l=="z"):
            sl="q"
        if(l==" "):
            sl=" "
        S+=sl
    print "Case #"+str(1+i)+": "+S
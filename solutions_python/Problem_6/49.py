from math import sqrt

f = open("C-small.in")
of = open("./numbers_output2.txt", "w")

cases = int(f.readline())
for i in range(cases):
    num = int(f.readline())
    
    pad = 10L ** 159L;
    mult = long(3L * pad + 2236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782274969508176150773783504253267724447073863586360121533452708866L)
    
    result = long(mult) ** long(num)
    
    result = result / (long(pad) ** long(num))
    
    
    strres = repr(result).rstrip("L").split(".")[0]
    
    strres = strres[-3:].rjust(3, "0")
    
    
    out = "Case #" + repr(i+1) + ": " + strres + "\n"
    print out
    of.write(out)
of.close()
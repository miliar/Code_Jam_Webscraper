import os
import string

#input = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
#         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
#         "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

def solve(inp = ""):
    #inp = input
    dic = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 
           'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'w', 'n': 'b', 'p': 'r', 
           's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q':'z', 'o': 'k'}
#    for i in range(inp.__len__()):
#        for j in range(inp[i].__len__()):
#            chr = inp[i][j]
#            if (chr != " "):
#                dic[chr] = output[i][j]
#                #print inp[i][j] + "=" + output[i][j]
#                print dic
    for i in range(inp.__len__()):
        curinp = inp[i]
        for j in range(curinp.__len__()):
            chr = inp[i][j]
            if (chr != " " and chr in dic.keys()):
                curinp = list(curinp)
                curinp[j] = string.replace(curinp[j], chr, dic[chr])
                curinp = "".join(curinp)
        print "Case #{0}: {1}".format(i+1, curinp)

def getinput(filename = ""):
    inputpath = "../input/"
    inpfile = open(inputpath + filename)
    inplist = []
    for line in inpfile:
        line = line.strip()
        if (not line.isdigit()):
            inplist.append(line)
    return inplist

output = ["our language is impossible to understand",
          "there are twenty six factorial possibilities",
          "so it is okay if you want to just give up"]


#solve()

inplist = getinput("Speaking in Tongues.in")
solve(inplist)

#!/usr/bin/python
import re

#Read input
f       = open('inp.txt', 'r')
lines   = f.readlines()
f.close()

#Output
f       = open('out.txt', 'w')
total   = lines.pop(0)
c_i     = 0

debug   = False
  

while(True):
    if len(lines) == 0:
        break

    listn = lines.pop(0)
    listn = listn.rstrip('\n')
    listn = listn.split(" ")

    blistt = int(listn.pop(0))
    blist  = []
    i=0
    while(i<blistt):
        blist.append(listn.pop(0))
        i += 1
    
    olistt = int(listn.pop(0))
    olist  = []
    i=0
    while(i<olistt):
        olist.append(listn.pop(0))
        i += 1

    strt   = int(listn.pop(0))
    stri   = list(listn.pop(0))

    #print blist, olist, stri
    if len(stri) < 2:
        result = stri
    else:
        prev_char   = stri[0]
        i           = 1
        run = True
        while(run):
            curr_char = stri[i]
            # does it need to replace bcoz of blist
            replace   = False
            replace_c = ''
            for each in blist:
                temp  = list(each)
                if ((temp[0] == prev_char) and (temp[1] == curr_char)) or ((temp[1] == prev_char) and (temp[0] == curr_char)):
                    replace     = True
                    replace_c   = temp[2]
                    break
            if replace: #
                stri[i-1] = replace_c
                stri.pop(i)
                prev_char = replace_c
            else:   #no replacement, check for oppose
                ofound = True
                while(ofound):
                    ofound = False
                    for each in olist:
                        l = each[0]
                        r = each[1]
                        try:
                            c1 = stri.index(l)
                            c2 = stri.index(r)
                            if (c1 <=i) and (c2<=i):
                                #we need to remove every item in range c1,c2
#                                if c1>c2:   #little swap    
 #                                   temp = c1
  #                                  c1   = c2
   #                                 c2   = temp

                                #c=0
                                #newlist = []
                                #for each in stri:   #remove here
                                #    if not (c>=c1 and c<=c2):
                                #        newlist.append(each)
                                #    else:
                                #        i -= 1
                                #    c += 1
                                #stri = newlist     
                                #if (i<0):
                                #    i = 0
                                newlist = stri[(i+1):]
                                i = 0                             
    #                            print c1,c2, newlist
                                stri = newlist
                                ofound = True
                        except:
                            pass

                i += 1
            
            if i >= len(stri):
                run = False
            else:
                prev_char = stri[i-1]

    #print stri
    result = stri
    #result = "".join(stri)
    c_i   += 1
    output = "Case #"+str(c_i)+": "+str(result)
    #output  = result
    print output

    output += "\n"
    #break
    f.write(output)
f.close()

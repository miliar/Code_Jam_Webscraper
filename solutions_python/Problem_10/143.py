#encoding=utf8
import jamio
import math
from decimal import *

def get_cases():
    lines = jamio.get_file_lines()
    for x in range(1,len(lines),2):
        cs = []
        cs.append(map(int,lines[x].split()))
        cs.append(map(int,lines[x+1].split()))
        yield cs
   
def deal(cs):
    p,k,l = cs[0]
    letters = list(reversed(sorted(cs[1])))
    ret = 0
    for i in range(1,l/k+3):
        ret+=i*sum(letters[(i-1)*k:k*i])

    return ret




idx=1
text=""
for cs in get_cases():
    text+="Case #%d: %d\n" % (idx,deal(cs))
    idx+=1

jamio.output(text)

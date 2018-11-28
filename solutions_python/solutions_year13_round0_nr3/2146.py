# Google Code Jam 2013 C.Fair and Square
import sys

def reverse(st):
    rst = ""
    for i in range(len(st)-1, -1, -1):
        rst  += st[i]
    return rst

def find_pals(l, h):
    num = l
    while num <= h:
        st = str(num)
        rst = reverse(st)
        
        if st == rst:
            yield num

        num += 1


def is_pal(num):
    stnum = str(num)
    if stnum == reverse(stnum):
        return True
    return False

def find_fairs(l, h):
    result = 0
    lo = int(len(str(l))/2) 
    ho = int(len(str(h))/2) + 2

    ln = '1'
    hn = '1'

    for i in range(lo-1):
        ln += '0' 
    for i in range(ho - 1):
        hn += '0'

    #pals = find_pals(int(ln), int(hn))
    
    for i in find_pals(int(ln), int(hn)):
        square = i*i
        if square > h:
            break
        elif square < l:
            continue

        if is_pal(square):
            result += 1

    return result

def fair_square(f):
    result = []
    lines = f.read().splitlines()
    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(ncases):
       limit = [int(a) for a in lines[i].split(" ")]
       l = limit[0]
       h = limit[1]
       result.append((i+1, find_fairs(l, h)))

    return result

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = open("simple.txt")

#print(fair_square(f))
#f.close()

def write_output():
    fairs = fair_square(f)
    out = open("output_fairs", "w")
    for num, res in fairs:
        out.write("Case #{}: {}\n".format(num, res))
write_output()






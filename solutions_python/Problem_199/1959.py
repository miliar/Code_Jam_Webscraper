def parse_input(inp):
    s = []
    p = inp.split(' ')
    for c in p[0]:
        s.append(c == "+")
    return [s, int(p[1])]
    
def positive(inp):
    for i in inp[0]:
        if not i:
            return False
    return True

def flip(inp, n=0): 
    if n > 2000:
        return (inp, "IMPOSSIBLE")

    for i,s in enumerate(inp[0][:len(inp[0]) - 2]):
        if not s:
            for k in range(i, i+inp[1]):
               inp[0][k] = not inp[0][k]



            return flip(inp, n+1)
    return (inp,n)        

numinp = int(input())

inp = []

for i in range(0, numinp + 1):
    try:
        inp = parse_input(input())
    except EOFError:
        break
    n = 0
    #print(inp)
#    while not positive(inp):
    inp,n = flip(inp)   
    print("Case #{}: {}".format(i+1, n))


from math import pi
f = open("Output.txt", "w")

def aria(r):#Calculeaza aria ringului negru ce inconjoara cercul alb de raza r
    return 2*r+1#(r+1)**2 - r**2

i = 0
for e in open("Input.txt", "r"):
    if i != 0:
        cercuri = 0
        list = e.split(' ')
        
        r = int(list[0])#raza primului cerc alb
        t = int(list[1])#t mm of black paint
        #1 mm of t required to cover PI centimetri patrati
        
        
        while t >= 0:
            t -= aria(r)
            cercuri += 1
            r += 2
        
        ans = "Case #" + str(i) + ": " + str(cercuri-1) + "\n"
        f.write(ans)
    i += 1
f.close()

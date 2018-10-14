import math
def calculate(r, x, y):
    S1 = r*r*math.acos(1.0*x/r)-x*math.sqrt(r*r-x*x)
    if (y <= r):
        S2 = r*r*math.acos(1.0*y/r)-y*math.sqrt(r*r-y*y)
        return S1-S2
    else:
        return S1
    
def calculatepart(r, x, y, c):
    edge = math.sqrt(r*r-c*c)
    if y >= edge:
        y=edge
    result = calculate(r,x,y)
    rectangle = (y-x)*c * 2
    return (result-rectangle)/2

def format(number):
    result = "%0.6f" % number
    return result

input = open("input.txt").readlines()
output = open("output.txt", "w")
for i in range(len(input)):
    if input[i][-1] == '\n':
        input[i] = input[i][:-1]

nOfCases = int(input[0])
cursor = 1

for casecount in range(nOfCases):
    tempinput = input[cursor].split()
    cursor+=1
    result = 0
    f, R, t, r, g = [float(i) for i in tempinput]
    #if casecount != 2 :
    #    continue

    if (g <= 2*f):
        area = 0
    else:
        side = g-2*f
        radius = R-t-f
        area = 0
        
        start = r+f
        while start < radius:
            other = start + side
            if (other >= radius):
                other = radius
                
            pivot = math.sqrt(radius*radius - other*other)
            
            temp = 0
            a = r+f
            while a < math.sqrt(radius*radius - start*start):
                old =temp
                b = a+side
                if b <= pivot:
                    temp += side*side
                else:
                    if  a>=pivot:
                        y = calculatepart(radius,a,b, start)
                        temp += y
                    else:
                        temp += side*(pivot-a)
                        y = calculatepart(radius,pivot, b, start)
                        temp += y
                
                a += g+2*r         

            
            area += temp*4
                
#           raw_input()
            start += g+2*r
#        print area, math.pi*R*R
        
    result = area / (math.pi * R*R)
    result = 1- result
    print>>output, "Case #"+str(casecount+1)+": " +  format(result)
    print "Case #"+str(casecount+1)+": " +  format(result)


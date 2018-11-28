level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    r,o,y,g,b,v = 1,3,2,6,4,5
    colorxor = {'R':1,'O':3, 'Y' : 2 , 'G':6,'B':4,'V':5}
    [N,R,O,Y,G,B,V] = [int(x) for x in input_file.readline().split()]
    R -= G
    Y -= V
    B -= O
    d = {'R':R,'B':B, 'Y':Y}
    if(min(R,Y,B) < 0 or max(R,Y,B) > R+Y+B - max(R,Y,B)):
        return "IMPOSSIBLE"
    green = "GR" * G
    violet = "VY" * V
    orange = "OB" * O
    color = d.keys()
    color.sort(key = lambda x: d[x])
    co = [d[c] for c in color]
    first = co[1] + co[0] - co[2]
    second = co[2] - co[0]
    third = co[2] - co[1]
    string = (color[2]+color[0]+color[1])*first + (color[2]+color[1])*second + (color[2]+color[0])*third
    for c in color:
        i = (string+c).index(c)
        s = ""
        if(c == 'R'):
            s = green
        if(c == 'Y'):
            s = violet
        if(c == 'B'):
            s = orange
        string = string[:i+1] + s + string[i+1:]
    for i in xrange(N):
        if(colorxor[string[i]] & colorxor[string[i-1]] != 0):
            return "IMPOSSIBLE"
    return string
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()

import math
import sys
import random

def int_circ(x,R):
    if R**2 - x**2 > 0:
        return 0.5*x*(R**2-x**2)**0.5 + 0.5*(R**2)*math.atan(1/(R**2-x**2)**0.5*x)
    else:
        return 0.5*x*(R**2-x**2)**0.5 + 0.5*(R**2)*(math.pi/2)
        
def int_range(x1,x2,R):
    result = int_circ(x2,R) - int_circ(x1,R)
    return result

def find_partial(x,y,Ri,gf):
    bottom_right_in = (x+gf)**2+y**2 < Ri**2
    top_left_in = x**2+(y+gf)**2 < Ri**2
    if bottom_right_in and top_left_in:
        p1x = x+gf
        p1y = math.sqrt(Ri**2-p1x**2)
        p2y = y+gf
        p2x = math.sqrt(Ri**2-p2y**2)
        #print "case 1 - p1: "+ repr((p1x,p1y)) + " p2: " +repr((p2x,p2y))
        area1 = (p2x-x)*gf
        area2 = int_range(p2x,p1x,Ri)-y*(p1x-p2x)
        #print "area 1: " + repr(area1)
        #print "area 2: " + repr(area2)
        result = area1+area2
    elif bottom_right_in and (not top_left_in):
        p1x = x+gf
        p1y = math.sqrt(Ri**2-p1x**2)
        p2x = x
        p2y = math.sqrt(Ri**2-p2x**2)
        #print "case 2 - p1: "+ repr((p1x,p1y)) + " p2: " +repr((p2x,p2y))
        result = int_range(p2x,p1x,Ri)-y*(p1x-p2x)
        #print "area: " + repr(result)
    elif (not bottom_right_in) and top_left_in:
        p1y = y
        p1x = math.sqrt(Ri**2-p1y**2)
        p2y = y+gf
        p2x = math.sqrt(Ri**2-p2y**2)
        #print "case 3 - p1: "+ repr((p1x,p1y)) + " p2: " +repr((p2x,p2y))
        area1 = (p2x-x)*gf
        area2 = int_range(p2x,p1x,Ri)-y*(p1x-p2x)
        result = area1+area2
        #print "area 1: " + repr(area1)
        #print "area 2: " + repr(area2)
    else:
        p1y = y
        p2x = x
        p1x = math.sqrt(Ri**2-p1y**2)
        p2y = math.sqrt(Ri**2-p2x**2)
        #print "case 4 - p1: "+ repr((p1x,p1y)) + " p2: " +repr((p2x,p2y))
        result = int_range(p2x,p1x,Ri)-y*(p1x-p2x)
        #print "area: " + repr(result)
    #print repr(result)
    return result

def squat_chance(f, R, t, r, g):
    gf = g-2*f
    R = R
    Ri = R-t-f
    edge = r+f
    block = gf+2*edge
    #survive_ring = (Ri / R)**2 # both *pi

    full_num = 0
    partials = []
    empty_num = 0
    for j in range(0,int(math.floor(R/block))+1):
        for i in range(0,int(math.floor(R/block))+1):
            cur_x = (i*block)+edge
            cur_y = (j*block)+edge
            #print "now at " + repr((cur_x,cur_y))
            #print repr(cur_x+gf) + ", "+ repr(cur_y+gf)
            if (cur_x+gf)**2+(cur_y+gf)**2 < Ri**2:
                full_num += 1
                #print "full"
            elif (cur_x)**2 + (cur_y)**2 > Ri**2:
                empty_num += 1
                #print "empty"
            else:
                partials.append(find_partial(cur_x,cur_y,Ri,gf))

    #print "full: " + repr(full_num)
    #print "empty: " + repr(empty_num)
    #print "partials: \n" + repr(partials)
    good_area = full_num*(gf**2)
    for elem in partials:
        good_area += elem
    #print "good/all : " + repr(good_area*4) + "/" + repr(math.pi*R**2)
    return 1 - (good_area*4 / (math.pi*R**2))
        

def processFile(source, target):
    sf = open(source)
    tf = open(target,"w")
    num_cases = int(sf.readline())
    for case in range(1,num_cases+1):
        [f,R,t,r,g] = sf.readline().strip('\n').split(' ')
        f = float(f)
        R = float(R)
        t = float(t)
        r = float(r)
        g = float(g)
        result = squat_chance(f, R, t, r, g)        
        newline = 'Case #' + repr(case) + ': ' + "%f" % result
        #print(newline)
        tf.write(newline)
        if not case==num_cases: tf.write('\n')

    sf.close
    tf.close

def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    

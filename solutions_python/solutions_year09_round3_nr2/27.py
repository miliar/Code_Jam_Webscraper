#!/usr/bin/env python
""" """
import sys

def analyse_test_case(C):
    N = len(C[0])
    # expression for centre of swarms position
    x0 = sum(C[0])/(N*1.0)
    y0 = sum(C[1])/(N*1.0)
    z0 = sum(C[2])/(N*1.0)
    Vx = sum(C[3])/(N*1.0)
    Vy = sum(C[4])/(N*1.0)
    Vz = sum(C[5])/(N*1.0)
    # d**2(t) = (Vx*t + x0)**2 + (Vy*t + y0)**2 + (Vz*t + z0)**2
    # minimum of function at dirivative = 0
    # 0 = 2*Vx*(Vx*t_min + x0) + 2*Vy*(Vy*t_min + y0) + 2*Vz*(Vz*t_min + z0)
    # t_min = -(Vx*x0+Vy*y0+Vz*z0)/(Vx**2+Vy**2+Vz**2)
    if (Vx**2 + Vy**2 + Vz**2) > 0 :
        t_min =  -(Vx*x0 + Vy*y0 + Vz*z0)/(Vx**2 + Vy**2 + Vz**2)
    else :
        t_min = 0
    if t_min < 0 :
        t_min = 0
    d_min_sqrd = (Vx*t_min + x0)**2 + (Vy*t_min + y0)**2 + (Vz*t_min + z0)**2
    return t_min, d_min_sqrd**0.5



def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    f.close()
    T = int(lines[0].strip())
    print('file "%s" contains %i cases' % (datafile,T))
    i_ind = 1
    
    cases = []
    for i in range(T) :
        N = int(lines[i_ind].strip())
        x = []
        y = []
        z = []
        Vx = []
        Vy = []
        Vz = []
        for j in range(N) :
            #print(lines[i_ind+1+j].strip().split(' '))
            val_x,val_y,val_z, val_Vx,val_Vy,val_Vz = [int(v) for v in lines[i_ind+1+j].strip().split(' ')]
            x.append(val_x)
            y.append(val_y)
            z.append(val_z)
            Vx.append(val_Vx)
            Vy.append(val_Vy)
            Vz.append(val_Vz)
        #print('x', x)
        #print('y', y)
        #print('z', z)
        #print('Vx', Vx)
        #print('Vy', Vy)
        #print('Vz', Vz)
        cases.append([x,y,z,Vx,Vy,Vz])
        i_ind = i_ind + 1 + N
    output = []
    count = 1
    for case in cases :
        t,d = analyse_test_case(case)
        output.append("Case #%i: %10.8f %10.8f" % (count,d,t))
        count = count + 1
        print(output[-1])
    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()

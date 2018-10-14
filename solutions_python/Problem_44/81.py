from __future__ import division
import math

if __name__ == '__main__':
    f = open('e:\\B.in')
    fout = open('e:\\result.out', 'w')

    ccase = int(f.readline().strip())
    print ccase
    for icase in range(ccase):
        num=int(f.readline().strip())
        print num
        xm,ym,zm,vxm,vym,vzm=0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for i in range(num):
            x,y,z,vx,vy,vz=[float(n) for n in f.readline().split()]
            print x,y,z,vx,vy,vz
            xm+=x
            ym+=y
            zm+=z
            vxm+=vx
            vym+=vy
            vzm+=vz
        '''xm/=num
        ym/=num
        zm/=num
        vxm/=num
        vym/=num
        vzm/=num'''
        #print xm,ym,zm,vxm,vym,vzm
        at2=vxm*vxm+vym*vym+vzm*vzm
        #at2/=num*num
        #print 2*vxm*xm,2*vym*ym,2*vzm*zm
        bt=2*vxm*xm+2*vym*ym+2*vzm*zm
        #bt/=num*num
        c=xm*xm+ym*ym+zm*zm
        #c/=num*num
        #print c,bt,at2,'......'
        if bt==0 and at2==0:
            d=0
            rs = math.sqrt(c)
            rs/=num
        else:
            d=-bt/(2*at2)
            print d
            if d<=0:
                d=0
                rs=xm*xm+ym*ym+zm*zm
            else:
                #xm+=vxm*d
                #ym+=vym*d
                #zm+=vzm*d
                #rs=c+bt*(-bt)/2/at2+at2*bt*bt/4/(at2*at2)
                #rs=-bt*bt/(4*at2)+c
                rs=-(vxm*xm+vym*ym+vzm*zm)*(vxm*xm+vym*ym+vzm*zm)/at2+c
            rs = math.sqrt(rs)
            rs/=num
            print rs
            
        fout.write('Case #%d: %.08f %.08f\n'%(icase+1, rs,d))
        print 'Case #%d: %.08f %.08f'%(icase+1, rs,d)
    f.close()
    fout.close()

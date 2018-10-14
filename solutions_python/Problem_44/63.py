import sys

def readline():
    return sys.stdin.readline().strip()

T = int( readline() )

for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N = int( readline() )
    x_total = 0
    y_total = 0
    z_total = 0
    vx_total = 0
    vy_total = 0
    vz_total = 0
    for n in range( N ):
        x, y, z, vx, vy, vz = ( int( x ) for x in readline().split() )
        x_total += x
        y_total += y
        z_total += z
        vx_total += vx
        vy_total += vy
        vz_total += vz
    # xyz0 is dragonfly origin
    x0 = x_total*1./N
    y0 = y_total*1./N
    z0 = z_total*1./N
    # dxyz is motion vector
    dx = vx_total*1./N
    dy = vy_total*1./N
    dz = vz_total*1./N
    dl = ( dx*dx + dy*dy + dz*dz )**0.5
    if dx == 0 and dy == 0 and dz == 0:
        print ( x0*x0 + y0*y0 + z0*z0 )**0.5, 0
        continue
    tmin = max( 0, -( x0*dx + y0*dy + z0*dz )/dl**2 )
    dmin = ( ( x0 + tmin*dx )**2 + ( y0 + tmin*dy )**2 + ( z0 + tmin*dz )**2 )**0.5
    print '%0.8f %0.8f' % ( dmin, tmin )

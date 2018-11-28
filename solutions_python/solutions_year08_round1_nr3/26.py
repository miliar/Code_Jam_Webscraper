## google code jam 2008, round 1a
## numbers

from math import *
from decimal import Decimal
rt5 = Decimal('2.23606797749978969640917366873127623544061835961152572427089724541052092563780489941441440837878227496950817615077378350425326772444707386358636012153345270886677817319187916581127664532263985658053576135041753378500342339241406444208643253909725259262722887629951740244068161177590890949849237139072972889848208864154268989409913169357701974867888442508975413295618317692149997742480153043411503595766833251249881517813940800056242085524354223555610630634282023409333198293395974635')


inputf = open('C-small-attempt1.in','r')
outputf = open('C-small-attempt1.out','w')
lines = inputf.readlines()
T = int(lines[0])

def one_up(x):
    return (3*x[0]+5*x[1], x[0]+3*x[1])

for case in range(1,T+1):
    n = int(lines[case])
    x = (1,0)
    for i in range(n):
        x = one_up(x)
    value = str(((x[0] % 1000) + int(((x[1]*rt5) % 1000))) % 1000)
    if len(value) == 1:
        value = '00' + value
    elif len(value) == 2:
        value = '0' + value
    outputf.write('Case #%d: %s\n' % (case, value))

inputf.close()
outputf.close()

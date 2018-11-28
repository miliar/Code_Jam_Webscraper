a = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz'
b = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq'
table = str.maketrans( a, b )

import sys

t = int( sys.stdin.readline() )
for i in range( t ):
    print( 'Case #{}: {}'.format( i + 1, sys.stdin.readline().translate( table ) ), end = '' )

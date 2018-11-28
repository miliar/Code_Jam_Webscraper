#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
char a[2000] ;
int fl[2000] ;
int main()
{
    int n ;
    freopen("D://in" ,"r" ,stdin ) ;
    freopen("D://out" ,"w" ,stdout ) ;
    scanf( "%d" ,&n ) ;
    int _ = 1 ;
    while( n -- ){
        long long s ,k ;
        cin >> s >> k ;
        s -- ;
        long long a = s/2 ,b = s-s/2 ;
        long long cnta = 1 ,cntb = 1 ,total = 2 ;
        if( k != 1 ){
            k -- ;
            if( a > b ) swap(a,b) ,swap(cnta,cntb);
            while( k > total ){
                k -= total ;
                long long ta ,tb ,ca ,cb ;
                if( a == b ) ta = (a-1)/2 ,tb = (a-1) - (a-1)/2 ,ca = cb = cnta + cntb ;
                else{
                    if( a > b ) swap(a,b) ,swap(cnta,cntb);
                    if( a % 2 == 1 ){ //5 6    2 3
                        ta = a/2 ;
                        tb = a-a/2 ;
                        ca = cnta + cnta + cntb ;
                        cb = cntb ;
                    } else { // 6 7   2 3
                        ta = b/2 - 1 ;
                        tb = b/2 ;
                        ca = cnta  ;
                        cb = cnta + cntb + cntb ;
                    }
                }
                total *= 2 ;
                a = ta ,b = tb ,cnta = ca , cntb = cb ;
                //cout << a << "-" << cnta << " " ;
                //cout << b << "-" << cntb << endl ;
            }
            long long ans ;
            if( a > b ) swap(a,b) ,swap(cnta,cntb);
            if( k <= cntb ) ans = b ;
            else ans = a ;
            if( ans % 2 ) a = b = ans / 2 ;
            else a = ans / 2 ,b = a - 1 ;
        }
        cout << "Case #" << _++  <<": " ;
        cout << max( a ,b ) << " " << min( a ,b ) << endl ;
    }
}

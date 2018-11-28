#include <iostream>
#include <cstdio>
#include <cstring>
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
        int x ,ans = 0 ,k = 0 ,l ,p = 0 ;
        memset( fl ,0 ,sizeof(fl) ) ;
        scanf( "%s %d" ,a ,&x ) ;
        l = strlen(a) ;
        for( int i = 0 ;i < l ;i ++ ){
            if( i >= x ) k -= fl[i-x] ;
            if( i + x > l ){
                if( k % 2 != 0 && a[i] == '+' ) p = 1 ;
                if( k % 2 == 0 && a[i] == '-' ) p = 1 ;
            } else if( a[i] == '+' ){
                if( k % 2 != 0 ) ans ++ ,k ++ ,fl[i] = 1 ;
            } else {
                if( k % 2 == 0 ) ans ++ ,k ++ ,fl[i] = 1 ;
            }
        }
        cout << "Case #" << _++ << ": " ;
        if( p )
            cout << "IMPOSSIBLE" << endl ;
        else
            cout << ans << endl ;
    }
}

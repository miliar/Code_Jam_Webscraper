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
        scanf( "%s" ,a ) ;
        int l = strlen(a) ,ni = 0 ;
        string ans ;
        int p = 0 ;
        while( p + 1 < l && a[p] <= a[p+1] ) p ++ ;

        for( int i = p + 1 ;i < l ;i ++ ) a[i] = '9' ;
        if( p != l - 1 && a[p] != '1' ){
            int o = 0 ;
            for( int i = 0 ;i <= p ;i ++ ){
                if( o ) a[i] = '9' ;
                else if( a[i] == a[p] ) a[i] -= 1 ,o = 1 ;
            }
        } else if( p != l - 1 ){
            a[0] = '0' ;
            for( int i = 1 ;i <= p ;i ++ ) a[i] = '9' ;
        }
        char *b ;
        for( int i = 0 ;i < l ;i ++ ){
            if( a[i] != '0' ){
                b = a + i ;
                break ;
            }
        }
        cout << "Case #" << _ ++ << ": " ;
        cout << b << endl ;
    }
}

#include <bits/stdc++.h>
using namespace std ;

int t , cs , n , k , ans ;
string s ;
int a[10004] ;
int main()
{
    freopen("A-large.txt" , "r" , stdin);
    freopen("os0.txt" , "w" , stdout) ;
    cin>>t ;
    while(cs<t)
    {

        cs++ ;
        cin>>s >> k ;
        //cout<< s << " " << k << endl ;
         n = s.size() ;
         ans = 0;
        for(int i = 0 ; i < n ; i++ )
        {
             if( s[i] == '+' ) a[i] = 1 ;
             else a[i] = 0 ;
        }
        n = n - k + 1 ;
        for( int i = 0 ; i < n ; i++ )
        {
            if( a[i] == 0 )
            {
                for( int j = i , c = 0 ; c < k ; j++,c++ ) a[j] ^= 1 ;
                ans++ ;
               // cout << i << endl ;
            }
        }
        int cn  = 0 ;
        n = s.size() ;
        for( int i = 0 ; i < n ; i++ ) cn += a[i] ;

        if( cn == s.size() ) printf("Case #%d: %d\n", cs , ans) ;
        else printf("Case #%d: IMPOSSIBLE\n", cs  ) ;
    }





return 0 ;
}

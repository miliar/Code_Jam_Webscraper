
#include <bits/stdc++.h>
using namespace std ;

int t , cs , n ;
string s ,ans ;
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("o.txt" , "w" , stdout) ;
    cin>>t ;
    while(cs<t)
    {

        cs++ ;
        cin>>s  ;
        n = s.size() - 1 ;
        for( int i = 0 ; i < n ; i++ )
        {
            if( s[i] > s[i+1] )
            {
                while( i != 0 && s[i] == s[i-1] )i-- ;
                s[i]-- ;
                for( int j = i+1 ; j <= n ; j++ ) s[j] = '9' ;
                break ;
            }
        }
        cout<<"Case #"<<cs<<": ";
        int f=  0 ;
        for( int i = 0 ; i <= n ; i++ )
        {
            if( s[i] == '0' && f == 1 )printf("%c", s[i] ) ;
            else if( s[i] != '0' ) f = 1 , printf("%c", s[i] ) ;
        }
        printf("\n");


    }





return 0 ;
}

#include <bits/stdc++.h>

using namespace std;
typedef long long ll ;


int t ;
string s;
int k ;

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;

    scanf("%d",&t) ;
    int ans, tmp ;
    string tmps ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {
        cin >> s >> k ;
        ans = 0;
        tmps = s;
        reverse(tmps.begin(),tmps.end()) ;
        tmp = 0 ;
        for ( int i = 0 ; i+k <= s.size() ; i++ )
        {
            if ( s[i] == '-' )
            {
                ans++ ;
                for ( int j = 0 ; j < k ; j++ )
                    s[j+i] = ( s[j+i] == '-' ? '+' : '-' ) ;
            }
        }
        bool lol = 1, lol2 = 1 ;
        for ( int i = 0 ; i < s.size() ; i++ )
            lol &= (s[i] == '+') ;
        for ( int i = 0 ; i+k <= s.size() ; i++ )
        {
            if ( tmps[i] == '-' )
            {
                tmp++ ;
                for ( int j = 0 ; j < k ; j++ )
                    tmps[j+i] = ( tmps[j+i] == '-' ? '+' : '-' ) ;
            }
        }
        for ( int i = 0 ; i < s.size() ; i++ )
            lol2 &= (tmps[i] == '+') ;

        printf("Case #%d: ",ctr) ;
        if ( !lol2 && !lol)
            printf("IMPOSSIBLE\n") ;
        else if ( !lol2 )
            printf("%d\n",ans) ;
        else if ( !lol )
            printf("%d\n",tmp) ;
        else
            printf("%d\n",min(tmp,ans)) ;

    }

    return 0;
}

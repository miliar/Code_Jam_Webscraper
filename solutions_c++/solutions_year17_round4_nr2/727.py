#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;

int n , c , m ;
int x , y ;
int cnt[1001][1001] ;

int main()
{
    freopen("B-small-attempt1.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    int t ;
    scanf("%d",&t) ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {
        scanf("%d%d%d",&n,&c,&m) ;
        memset(cnt,0,sizeof cnt) ;
        int ans = 0 ;
        int pro = 0 ;
        for ( int i = 0 ; i < m ;i++ )
        {
            scanf("%d%d",&x,&y) ;
            cnt[y][x]++ ;
        }
        for ( int i = 1 ; i < 1001 ; i++ )
        {
            while ( cnt[1][i] )
            {
                int k = -1 ;
                for ( int j = i+1 ; j < 1001 ; j++ )
                {
                    if ( cnt[2][j] )
                    {
                        k = j ;
                        break;
                    }
                }
                if ( k == -1 ) break ;
                cnt[2][k]-- ;
                cnt[1][i]-- ;
                ans++ ;
            }
        }
        for ( int i = 1 ; i < 1001 ; i++ )
        {
            while ( cnt[2][i] )
            {
                int k = -1 ;
                for ( int j = i+1 ; j < 1001 ; j++ )
                {
                    if ( cnt[1][j] )
                    {
                        k = j ;
                        break;
                    }
                }
                if ( k == -1 ) break ;
                cnt[1][k]-- ;
                cnt[2][i]-- ;
                ans++ ;
            }
        }
        for ( int i = 2 ; i < 1001 ; i++ )
            if ( cnt[1][i] && cnt[2][i] )
            {
                int tmp = min(cnt[1][i],cnt[2][i]) ;
                pro += tmp ;
                ans += tmp ;
                cnt[1][i] -= tmp ;
                cnt[2][i] -= tmp ;
            }
        for ( int i = 1 ; i < 1001 ; i++ )
            ans += cnt[1][i] + cnt[2][i] ;
        printf("Case #%d: %d %d\n",ctr,ans,pro) ;
    }

    return 0;
}

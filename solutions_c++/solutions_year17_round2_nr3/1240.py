#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;

int n, q ;
ll e[1111], s[1111] ;
ll d[1111][1111] ;
int u, v ;
int gloV ;
double dist[1111] ;

double dp[111][111] ;
double f(int idx, int last)
{
    if ( dist[idx] - dist[last] - e[last] > 1e-9 ) return 1e15 ;
    if ( idx == gloV ) return ( dist[idx]-dist[last] ) / s[last];
    if ( dp[idx][last] >= 0 ) return dp[idx][last] ;
    double ans = f(idx+1,last) ;
    ans = min(ans, f(idx+1,idx) + ( dist[idx]-dist[last] ) / s[last]  );
    return dp[idx][last] = ans ;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    int t;
    scanf("%d",&t) ;
    for ( int ctr = 1 ; ctr <= t; ctr++ )
    {
        memset(dp,-1,sizeof dp) ;
        scanf("%d%d",&n,&q) ;
        for ( int i = 1 ; i <= n ; i++ )
            scanf("%I64d%I64d",&e[i],&s[i]) ;

        for ( int i = 1 ;i <=  n ; i++ )
        {

            for ( int j = 1 ; j <= n ; j++ )
                scanf("%I64d",&d[i][j]) ;
            dist[i] = (i > 1 ? d[i-1][i] + dist[i-1] : 0) ;
        }
        s[0] = s[1] ;
        dist[0] = dist[1] ;
        for ( int i = 0 ; i < q ; i++ )
        {
            scanf("%d%d",&u,&v);
            gloV = v;
            printf("Case #%d: %.9f\n",ctr,f(1,1));
        }

    }
    return 0;
}

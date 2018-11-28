#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;


int n , m ;
int a[422] ;
int b[422] ;
int first[2][2000] ;
int dp[2000][2000][2][2] ;
int f(int time, int timeFirst, bool who, bool start)
{
    if ( timeFirst > 720 || time-timeFirst > 720 ) return 1e6 ;
    if ( time == 1440 )
       return ((timeFirst == 720)? start != who : 1e6) ;
    if ( dp[time][timeFirst][who][start]!= -1 ) return dp[time][timeFirst][who][start] ;
    int ans = 1e6 ;

    if ( first[0][time] == 0 )
    {
        ans = min(ans,f(time+1,timeFirst+1,0,time?start:0)+(who!=0)) ;
    }
    if ( first[1][time] == 0 )
    {
        ans = min(ans,f(time+1,timeFirst,1,time?start:1)+(who!=1)) ;
    }
    return dp[time][timeFirst][who][start] = ans ;
}
int main()
{
    freopen("B-large.in","r",stdin) ;
    freopen("out.out","w",stdout) ;
    int t ;
    scanf("%d",&t) ;
    for ( int ctr = 1 ;  ctr <= t ; ctr++ )
    {
        memset(first,0,sizeof first) ;
        memset(dp,-1,sizeof dp) ;
        scanf("%d%d",&n,&m) ;
        for ( int i = 0 ; i < n ; i++ )
        {
            scanf("%d%d",&a[i],&b[i]) ;
            for ( int j = a[i] ; j < b[i] ; j++ )
                first[0][j] = 1 ;
        }
        for ( int i = 0 ; i < m ; i++ )
        {
            scanf("%d%d",&a[i+n],&b[i+n]) ;
            for ( int j = a[i+n] ; j < b[i+n] ; j++ )
                first[1][j] = 1 ;
        }
        int a1 = f(0,0,0,0) ;
        memset(dp,-1,sizeof dp) ;
        int a2 = f(0,0,1,0) ;
        printf("Case #%d: %d\n",ctr,min(a1,a2)) ;
    }

    return 0;
}

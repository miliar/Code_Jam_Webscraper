#include <bits/stdc++.h>
using namespace std ;

#define rr first
#define hh second
typedef long long ll ;
int t , cs ;
ll dp[1003][1003] ;
int ck[1003][1003] ;
int n , k ;
pair < ll , ll > rh[1003] ;
const ll inf = 1e15 ;
const double pi = acos(-1.00 ) ;

ll go( int u , int nisi )
{
    if( nisi == k )return 0  ;
    if( u == n ) return -inf ;
    if( ck[u][nisi] == cs ) return dp[u][nisi] ;
    ck[u][nisi] = cs ;

    ll ret = go(u+1 , nisi+ 1 ) + rh[u].rr * rh[u].hh ;
    ret = max ( ret , go(u+1,nisi) ) ;
    return dp[u][nisi] = ret ;

}
int main()
{
    freopen("in.txt", "r", stdin ) ;
    freopen("out.txt", "w" , stdout ) ;
    cin >> t ;

    while(cs < t )
    {
        cs++ ;
        scanf("%d %d",&n,&k) ;

        for( int i = 0 ; i < n ; i++ )
            scanf("%lld %lld",&rh[i].rr , &rh[i].hh ) ;
        sort(rh, rh+ n ) ;
        reverse(rh, rh + n ) ;
//        for( int i = 0 ; i < n ; i++ )
//            printf("%lld %lld\n",rh[i].rr , rh[i].hh ) ;
        double ans = 0.00 ;
        for( int i = 0 ; i < n ; i++ )
        {
            ll tot = go(i+1,1 ) + rh[i].rr * rh[i].hh ;
            double res = pi * rh[i].rr * rh[i].rr + 2 * pi * tot ;
            if( ans < res )ans = res ;
        }
        printf("Case #%d: %0.9lf\n",cs, ans );
    }


return 0 ;
}

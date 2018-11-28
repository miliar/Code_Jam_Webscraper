#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;


ll r[1111], h[1111] ;

bool comp(int i, int j)
{
    if ( r[i] > r[j] ) return 1 ;
    if ( r[i] < r[j] ) return 0 ;
    return h[i] > h[j] ;
}
ll dp[1111][1111] ;
bool vis[1111][1111] ;
double mo[1111];
double to[1111] ;

int k, n ;
int a[1111] ;
ll f(int idx, int cnt)
{
    if ( cnt > k ) return -2e18 ;
    if ( idx == n ) return (cnt == k ? 0 : -2e18) ;
    if ( vis[idx][cnt] ) return dp[idx][cnt] ;
    ll ans  = -2e18 ;
    ll bla = f(idx+1,cnt) ;
    if ( bla - ans > 0 )
        ans = bla ;
    int ti = a[idx] ;
    bla = f(idx+1,cnt+1)+(!cnt? r[ti]*r[ti] :0 ) + h[ti]*2.*r[ti]  ;
    if ( bla - ans > 0 )
        ans = bla ;
    vis[idx][cnt] = 1;
    return dp[idx][cnt] = ans ;
}
int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("out.out","w",stdout) ;
    int t ;
    scanf("%d",&t) ;
    for ( int ctr = 1 ;  ctr <= t ; ctr++ )
    {
        cin >> n >> k;
        memset(dp,0,sizeof dp) ;
        memset(vis,0,sizeof vis) ;
        for ( int i = 0 ; i < n ; i++ ) a[i] = i ;
        for ( int i = 0 ; i < n;i++ )
            cin >> r[i] >> h[i] ;
        sort(a,a+n,comp) ;



        double ans = f(0,0)*acos(-1);


        printf("Case #%d: ",ctr) ;
        cout << setprecision(9) << fixed << ans << endl;
    }

    return 0;
}

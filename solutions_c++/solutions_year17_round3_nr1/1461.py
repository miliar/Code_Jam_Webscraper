#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

#define sf scanf
#define pf printf
#define pb push_back
#define mp make_pair
#define PI ( acos(-1.0) )
#define mod 1000000007
#define maxn 300005
#define IN freopen("Al.in","r",stdin)
#define OUT freopen("output1.txt","w",stdout)
#define FOR(i,a,b) for(i=a ; i<=b ; i++)
#define DBG pf("Hi\n")
#define INF 1000000000000000
#define i64 long long int
#define eps (1e-8)
#define pos first
#define cap second
#define ln 17
#define off 2

using namespace __gnu_pbds;
using namespace std ;

typedef tree< i64, null_type, less<i64>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

pair<i64,i64>  p[10005] ;
i64 r[10005],h[10005];

int main()
{
    i64 i , j , k , l , m, n , t=1 , tc ;

    IN ; OUT ;

    scanf("%lld",&tc) ;

    while(t<=tc)
    {
    sf("%lld %lld",&n,&k) ;

    for(i=1 ; i<=n ; i++)
    {
        sf("%lld %lld",&r[i],&h[i]) ;
        p[i] = make_pair(2*r[i]*h[i],i) ;
    }

    sort(p+1,p+n+1) ;

    i64 ans = 0 , ret ;

    for(i=1 ; i<=n ; i++)
    {
        ret = r[i]*r[i] + 2*r[i]*h[i] ;

        for(j=n,l=1; l<k ; j-- )
        {
            if(i==p[j].second) continue ;
            if( r[i] < r[ p[j].second ] ) continue ;
            else ret += p[j].first ;
            l++ ;
        }
        ans = max(ans,ret) ;
    }

    printf("Case #%lld: %0.10f\n",t++,(double)ans*PI) ;

    }


    return 0 ;
}

#include <bits/stdc++.h>

using namespace std;
typedef long long ll ;


int main()
{
    freopen("C-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    int t;
    scanf("%d",&t) ;

    ll n , k ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {
        scanf("%I64d %I64d",&n,&k) ;
        map < long long , long long > m ;
        m[n] = 1;
        k-- ;
        pair < ll ,ll > tm ;
        ll nu = -1;
        while ( k > 0 )
        {
            auto it2 = m.end() ;
            it2-- ;
            pair < ll , ll > it = *it2 ;
            if ( it.second > k )
            {
                nu = it.first ;
                break;
            }
            else
            {
                k -= it.second ;
                if ( it.first & 1 )
                    m[it.first/2ll] += it.second*2ll ;
                else m[it.first/2ll] += it.second ,
                    m[it.first/2ll-1ll]+=it.second ;
            }
            m.erase(it.first) ;
        }
        if ( nu == -1 )
        {
            auto it2 = m.end();
            it2-- ;
            nu = it2->first ;
        }
        if ( nu & 1 )
            tm = {nu/2ll,nu/2ll} ;
        else tm= {nu/2ll,max(0ll,nu/2ll-1ll)} ;
        printf("Case #%d: %I64d %I64d\n",ctr,tm.first,tm.second) ;
    }

    return 0;
}

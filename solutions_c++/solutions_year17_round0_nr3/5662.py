//
#include <bits/stdc++.h>
//StAn_
using namespace std ;

#define nl cout<<endl;
#define pb push_back
#define deb(x) cout<<#x<<" : "<<x<<endl;
#define deb2(x, y) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<endl;
#define MAX 100005
#define FOR(i,start,end) for(int i=start;i<end;i++)
typedef long long ll ;


ll n, dp[1000][2] ;
bool is_occupied[1000] ;


ll choose( void )
{
    ll ans=1001, minLR = -1 , maxLR = INT_MAX, LRmin, LRmax ;
    for(ll i=n-1; i>=0; i--)
    {
        if(!is_occupied[i])
        {
            LRmin = min(dp[i][0], dp[i][1]) ;
            LRmax = max(dp[i][0], dp[i][1]) ;
            if(LRmin > minLR)
            {
                minLR = LRmin ;
                maxLR = LRmax ;
                ans = i ;
            }
            if( (LRmin == minLR) && (LRmax > maxLR) )
            {
                maxLR = LRmax ;
                ans = i ;
            }
            if( (LRmin == minLR) && (LRmax == maxLR) )
            {
                ans = i ;
            }
        }
    }
    is_occupied[ans] = true ;
    return ans ;
}

void set_dp( ll pos )
{
    ll put = 0 ;
    FOR(i,pos+1,n)
    {
        if(is_occupied[i])
            break ;
        dp[i][0] = put++ ;
    }

    put = 0 ;
    for(ll i=pos-1; i>=0; i--)
    {
        if(is_occupied[i])
            break ;
        dp[i][1] = put++ ;
    }
}

void show( void )
{
    FOR(i,0,n)
    {
        deb2(dp[i][0], dp[i][1])
    }
    nl
    nl

}



//Driver Function
int main()
{
      #ifndef ONLINE_JUDGE
            freopen( "sm.txt", "r", stdin ) ;
            freopen( "smo.txt", "w", stdout ) ;
      #endif
      std::ios_base::sync_with_stdio( false ) ;
//_________________________________________________________________

      ll Test, i ;
      cin>>Test ;
      FOR(T,1,Test+1)
      {
            ll k, ans, temp, Ls, Rs, lastmin, lastmax ;
            cin>>n>>k ;

            temp = n-1 ;
            FOR(i,0,n)
            {
                dp[i][0] = i ;
                dp[i][1] = temp ;
                temp-- ;
            }
            memset(is_occupied,false,sizeof(is_occupied)) ;

            while(k--)
            {
                ll position = choose( ) ;
                Ls = dp[position][0] ;
                Rs = dp[position][1] ;
                lastmax = max(Ls, Rs) ;
                lastmin = min(Ls, Rs) ;

                set_dp( position ) ;
            }

            cout<<"Case #"<<T<<": "<<lastmax<<" "<<lastmin<<endl ;
      }

      return 0;
}

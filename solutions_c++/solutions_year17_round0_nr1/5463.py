//
#include <bits/stdc++.h>
//StAn_
using namespace std ;

#define nl cout<<endl;
#define pb push_back
#define MAX 100005
#define FOR(i,start,end) for(int i=start;i<end;i++)
typedef long long ll ;


ll solve( string s, ll n )
{
    ll ans = 0 ;
    ll i;
    FOR(i, 0, s.length() - n + 1)
    {
        if(s[i] == '+')
            continue ;
        if(s[i] == '-')
        {
            ans++ ;
            FOR(j, i, i+n)
            {
                if(s[j] == '-')
                    s[j] = '+' ;
                else
                    s[j] = '-' ;
            }
        }
    }
    FOR(i, s.length() - n, s.length())
    {
        if(s[i] == '-')
            return -1 ;
    }
    return ans ;
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
            ll n, m, ans ;
            string s;
            cin>>s;
            cin>>n ;
            ans = solve(s,n) ;

            if(ans == -1)
                cout<<"Case #"<<T<<": IMPOSSIBLE\n" ;
            else
                cout<<"Case #"<<T<<": "<<ans <<endl ;
      }

      return 0;
}

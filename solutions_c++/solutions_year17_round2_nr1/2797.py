//
#include <bits/stdc++.h>
//StAn_
using namespace std ;

#define MAX 100005
#define FOR(i,start,end) for(int i=start;i<end;i++)
typedef long long ll ;

//Driver Function
int main()
{
      #ifndef ONLINE_JUDGE
            //freopen( "sm.txt", "r", stdin ) ;
            //freopen( "smo.txt", "w", stdout ) ;
      #endif
      std::ios_base::sync_with_stdio( false ) ;
//_________________________________________________________________

      ll Test, i ;
      cin>>Test ;
      FOR(T,1,Test+1)
      {
            ll n, d ;
            long double ans , tim, speed, temp ;
            tim = INT_MIN ;
            cin>>d>>n ;
            ll k, s ;
            FOR(i, 0, n)
            {
                  cin>>k>>s ;
                  temp  = d - k ;
                  temp /= s ;

                  //speed = d / temp ;
                  tim = max(tim, temp) ;
            }
            ans = d / tim ;
            cout<<"Case #"<<T<<": " ;
            cout<<fixed<<setprecision(6)<<ans <<endl ;
      }

      return 0;
}




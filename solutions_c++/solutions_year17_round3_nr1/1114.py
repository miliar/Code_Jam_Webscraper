
#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; i++)
#define FOR(i, n) for (int i = 0; i < n; i++)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )

#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define Int long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define ff first
#define ss second
#define bit(n) (1<<(n))
#define Last(i) ( (i) & (-i) )
#define sq(x) ((x) * (x))
#define INF INT_MAX
#define mp make_pair
using namespace  std ;
const long double pi = 3.141592653589793238 ;
const int MAXN = 1e3 + 50;

Int dp[ MAXN ][ MAXN ] ;
int N , K ;
Int rec(  vector<pair<Int,Int> >&A  , int idx ,  int Left   )
  {
     if( Left == 0 or idx < 0 )return 0 ;
     if( dp[idx][Left] != -1 )return dp[idx][ Left ] ;
     Int ans = 0;
     ans = max(  ans ,  2*(A[idx].ff)*(A[idx].ss) + rec( A , idx - 1 , Left - 1 ) ) ;
     ans = max(  ans ,  rec( A , idx - 1 , Left ) ) ;
     dp[idx][Left] = ans ;
     return ans ;
  }
int main()
{

  freopen("aa.in", "r", stdin);
  freopen("aa.out", "w", stdout);

  int t ;
  cin >> t ;
  for( int p = 1 ; p <= t ; p ++ )
   {

        memset(dp,-1,sizeof(dp));
        cin >> N >> K ;
        vector<pair<Int,Int> >A( N ) ;
        FOR( i , N )
          {
              scanf("%lld%lld",&A[i].ff,&A[i].ss) ;
          }
        sort( A.begin() , A.end() ) ;
        Int ans = 0 ;
        for( int i =  N - 1 ; i >= 0 ; i -- )
           {
             ans = max(  ans , A[i].ff*A[i].ff + 2*A[i].ff*A[i].ss + rec( A , i - 1  , K - 1 ) )  ;
             //cout<<ans<<endl;
            // cout<<A[i].ff*A[i].ff<<" "<<ans<<" "<<i <<endl;
           }

        double As = ans*pi ;
        //cout<<ans<<endl;
        cout<<"Case #"<<p<<": ";
        printf("%.9lf\n",As);
   }


}

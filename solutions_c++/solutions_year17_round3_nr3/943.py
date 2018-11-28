
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
double EPSILON = 1e-9 ;
int main()
{

  freopen("aa.in", "r", stdin);
  freopen("aa.out", "w", stdout);

  int t ;
  cin >> t ;
  for( int p = 1 ; p <= t ; p ++ )
   {
        double Lim = 0 ;

        int N , K ;
        cin >> N >> K ;
        vector<double>A( N ),C( N );

        cin >>  Lim ;
        FOR( i , N )
         {  cin >> A[i] ;
            C[i] = A[i] ;
         }

        double lo = 0.00;
        double hi = 1.00 ;
        double ans = 0  ;

        while( hi - lo >= EPSILON )
          {
             double mid = ( lo + hi )/ 2 ;
             double use = Lim ;
             FOR( i , N )A[i] = C[i] ;

             bool f =  true ;
             FOR( i , N )
               {
                 if( A[i] - mid  >= EPSILON )continue ;
                 if( use - (mid - A[i])  >= EPSILON )
                   {
                        double sub = mid - A[i] ;
                        use -= sub ;
                        A[i] = mid ;
                   }
                 else f  =  false ;

               }

             double product = 1 ;
             FOR( i , N )
               product  = product*A[i] ;

             ans = max(  ans ,  product ) ;

           //  cout<<f<<" "<<mid<<endl;
             if( f )
               {
                  lo = mid + EPSILON ;
               }
              else hi = mid - EPSILON ;




          }

          cout<<"Case #"<<p<<": ";
        printf("%.7lf\n",ans);

   }


}

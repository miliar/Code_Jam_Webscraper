#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()  {

  freopen ( "A-large.in" , "r" , stdin );
  freopen ( "out.txt" , "w" , stdout );

  int t , n;
  ll d , i , v;
  double res;

  scanf ( "%d" , &t );

  for ( int it = 0 ; it < t ; it++ ) {

    scanf ( "%lld%d" , &d , &n );
    res = DBL_MAX;

    while ( n-- ) {
      scanf ( "%lld%lld" , &i , &v );
      res = min ( res , ( d * v ) / double ( d - i ) );
    }
    printf ( "Case #%d: %f\n" , it + 1 , res );

  }

  return 0;

}

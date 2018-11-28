#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    double D;
    int N;
    cin >> D >> N;
    double tt = 0;
    for( int i=0; i<N; i++ ){
      double K, S;
      cin >> K >> S;
      double t = (D-K) / S;
      tt = max( tt, t );
    }
    printf( "Case #%d: %.12f\n", testcase, D/tt );
  }
}

#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
double P[55];
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    int N, K;
    double U;
    cin >> N >> K;
    cin >> U;
    for( int i=0; i<N; i++ ) cin >> P[i];
    sort( P, P+N );
    int c = 1;
    for( int i=0; i<N; i++ ){
      double p;
      if( i == N-1 ) p = 1.0;
      else p = P[i+1];
      double d = p - P[0]; 
      if( d * c <= U ){
        U -= d * c;
        c++;
        P[0] = p;
      } else {
        P[0] += U / c;
        break;
      }
    }
    double ret = 1;
    for( int i=0; i<c; i++ ) ret *= P[0];
    for( int i=c; i<N; i++ ) ret *= P[i];

    printf( "Case #%d: %.12f\n", testcase, ret );
  }
}

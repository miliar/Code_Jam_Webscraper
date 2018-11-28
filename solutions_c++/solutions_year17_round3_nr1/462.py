#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;
typedef long long ll;
typedef pair<double,pair<ll,ll> > P;
P d[1005];
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    double PI = 3.14159265358979323846264338327950288;
    int N, K;
    cin >> N >> K;
    ll r,h;
    for( int i=0; i<N; i++ ){
      cin >> r >> h;
      d[i].first = r * h;
      d[i].second.first = r;
      d[i].second.second = h;
    }
    sort( d, d+N );

    double ret = 0;

    for( int i=0; i<N; i++ ){
      int c = 1;
      double s = d[i].first;
      for( int j=N-1; j>=0; j-- ){
        if( c == K ) break;
        if( i == j ) continue;
        if( d[i].second.first < d[j].second.first ) continue;
        s += d[j].first;
        c++;
      }
      if( c < K ) continue;
      ret = max( ret, d[i].second.first * d[i].second.first * PI + s * 2 * PI );
    }
    printf( "Case #%d: %.12f\n", testcase, ret );
  }
}

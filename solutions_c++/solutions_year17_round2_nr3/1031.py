#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
typedef long long ll;
ll E[105];
ll S[105];
ll D[105][105];
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    int N, Q, U, V;
    cin >> N >> Q;
    for( int i=0; i<N; i++ ){
      cin >> E[i] >> S[i];
    }
    for( int i=0; i<N; i++ ){
      for( int j=0; j<N; j++ ){
        cin >> D[i][j];
      }
    }
    for( int i=0; i<Q; i++ ){
      cin >> U >> V;
    }
    double t[105];
    t[0] = 0;
    for( int i=1; i<N; i++ ){
      t[i] = 1.0e20;
    }
    for( int i=0; i<N; i++ ){
      ll s = 0;
      for( int j=i+1; j<N; j++ ){
        s += D[j-1][j];
        //cout << s << endl;
        if( s <= E[i] ){
          t[j] = min( t[j], t[i] + ((double)s)/S[i] );
          //cout << j << " " << t[j] << endl;
        }
      }
    }
    printf( "Case #%d: %.12f\n", testcase, t[N-1] );
  }
}

#include <iostream>
#include <algorithm>
using namespace std;
int d[2][1024];
int main()
{
  ios::sync_with_stdio(false);
  int T, N, M, C;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    cin >> N >> C >> M;
    for( int i=0; i<2; i++ ) for( int j=0; j<1024; j++ )
      d[i][j] = 0;
    int c[2] = {0,0};
    for( int i=0; i<M; i++ ){
      int B, P;
      cin >> P >> B;
      d[B-1][P]++;
      c[B-1]++;
    }
    int ret0 = max( c[0], c[1] );
    ret0 = max( ret0, d[0][1] + d[1][1] );
    int ret1 = 0;
    for( int i=2; i<=N; i++ ){
      if( d[0][i] + d[1][i] > ret0 ){
        ret1 += d[0][i] + d[1][i] - ret0;
      }
    }
    cout << "Case #" << testcase << ": " << ret0 << ' ' << ret1 << endl;
  }
}

#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
  ios::sync_with_stdio(false);
  int T, N, P, G;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    cin >> N >> P;
    int d[4] = {0,0,0,0};
    for( int i=0; i<N; i++ ){
      cin >> G;
      d[G%P]++;
    }
    int ret = 0;
    ret += d[0];
    if( P == 2 ){
      ret += d[1] / 2;
      d[1] -= (d[1] / 2) * 2;
      ret += d[1];
    } else if( P == 3 ){
      ret += min( d[1], d[2] );
      int remain = max( d[1], d[2] ) - min( d[1], d[2] );
      ret += remain / 3;
      remain -= (remain/3) * 3;
      if( remain > 0 ) ret++;
    } else {
      ret += d[2] / 2;
      d[2] -= (d[2] / 2) * 2;
      ret += min( d[1], d[3] );
      int remain = max( d[1], d[3] ) - min( d[1], d[3] );
      ret += remain / 4;
      remain -= (remain/4) * 4;
      if( d[2] > 0 ) ret++;
      if( d[2] > 0 && remain > 2 ) ret++;
    }
    cout << "Case #" << testcase << ": " << ret << endl;
  }
}

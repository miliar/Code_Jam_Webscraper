#include <bits/stdc++.h>
using namespace std;

signed main(){
  ios::sync_with_stdio( 0 );
  int T; cin >> T;
  for( int ti = 0; ti < T; ++ti ){
    int N, K;
    cin >> N >> K;
    if( K * 2 > N + 50000 ){
      cout << "Case #" << ti + 1 << ": 0 0\n";
      continue;
    }
    priority_queue< tuple< int, int, int, int > > pq;
    pq.emplace( N - 1 >> 1, N >> 1, 0, N );
    int ans_l, ans_r;
    for( int i = 0; i < K; ++i ){
      int mi, mx, lb, rb;
      tie( mi, mx, lb, rb ) = pq.top();
      pq.pop();
      lb *= -1;
      ans_l = mx, ans_r = mi;
      int mid = lb + ( rb - lb - 1 ) / 2;
      if( mid - lb > 0 ){
        int n = mid - lb;
        pq.emplace( n - 1 >> 1, n >> 1, - lb, mid );
      }
      if( rb - ( mid + 1 ) > 0 ){
        int n = rb - ( mid + 1 );
        pq.emplace( n - 1 >> 1, n >> 1, - ( mid + 1 ), rb );
      }
    }
    cout << "Case #" << ti + 1 << ": " << ans_l << " " << ans_r << "\n";
  }
  return 0;
}

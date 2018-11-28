#include <iostream>
#include <iomanip>
#include <cassert>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int tc=1;tc<=T;tc++) {
    int N, K;
    cin >> N >> K;
    assert(N == K);
    double U;
    double P[64];
    cin >> U;
    for(int i=0;i<N;i++) cin >> P[i];
    double lo = 0, hi = 1;
    int it = 300;
    while(--it) {
      double mid = (lo+hi)/2;
      double needed = 0;
      for(int i=0;i<N;i++) {
        needed += max(0.,mid-P[i]);
      }
      if (needed > U + 1e-9) {
        hi = mid;
      } else {
        lo = mid;
      }
    }
    double res = 1;
    for(int i=0;i<N;i++) {
      res *= max(lo,P[i]);
    }
    cout << "Case #" << tc << ": " << fixed << setprecision(9) << res << endl;
  }
  return 0;
}
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    ll D, N; cin >> D >> N;
    ld mt = 0.0;
    for (int i = 0; i < N; i++) {
      ll K, S; cin >> K >> S;
    ld t = (D-K)/(ld)S;
    if (mt < t) mt = t;
    }
    printf("Case #%d: %.6LF\n", t, D/mt);
  }
  return 0;
}

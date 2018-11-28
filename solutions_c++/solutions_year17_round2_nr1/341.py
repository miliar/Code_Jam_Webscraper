#define NDEBUG
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)

double solve() {
  int D, N;
  cin >> D >> N;
  vector<int> x(N), S(N);
  for (int i = 0; i < N; ++i) {
    cin >> x[i] >> S[i];
  }
  double lo = 0.0, hi = 1e18;
  repeat (300) {
    const double v = (lo + hi) / 2;
    const double t = D / v;
    bool ok = true;
    for (int i = 0; i < N; ++i) {
      if (x[i] + t * S[i] < D) {
        ok = false;
        break;
      }
    }
    if (ok) {
      lo = v;
    } else {
      hi = v;
    }
  }
  return lo;
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    printf("Case #%d: %.6f\n", tt, solve());
    fflush(stdout);
  }
}

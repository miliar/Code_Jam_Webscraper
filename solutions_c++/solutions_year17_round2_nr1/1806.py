#include <iostream>
#include <iomanip>

using namespace std;

static const double EPS = 1e-7;

typedef long long ll;

int T, N;
ll D, K[1005], S[1005];

inline double Abs(const double& v) {
  return v > 0.0 ? v : -v;
}

bool good(const double& speed) {
  for (int i = 0; i < N; ++i) {
    if (D * S[i] - speed * (D - K[i]) < 0.0)
      return false;
  }
  return true;
}

double search() {
  double lo = 0.0, hi = 1e20, mid;
  while (Abs(hi - lo) >= EPS && Abs(hi - lo) / lo >= EPS) {
    //cerr << lo << " " << hi << endl;
    mid = lo + (hi - lo) / 2.0;
    bool f = good(mid);
    if (f) {
      lo = mid;
    } else {
      hi = mid;
    }
  }
  return lo;
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> D >> N;
    for (int i = 0; i < N; ++i) {
      cin >> K[i] >> S[i];
    }
    //cerr << "Case " << t << " " << D << " " << K[0] << " " << S[0] << endl;
    cout << "Case #" << t << ": " << setprecision(10) << search() << endl; 
  }
  return 0;
}
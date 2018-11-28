#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

using ll = long long;
using ld = long double;
const string filename = "";

template <class T>
T sqr(T x) {
  return x * x;
}

void solve() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int N;
    ld D;
    cin >> D >> N;
    ld ans = 1e18;
    for (int j = 0; j < N; ++j) {
      ld K, S;
      cin >> K >> S;
      ans = std::min(ans, D / (D - K) * S);
    }
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
}

int main() {
#ifdef DEBUG
#else
  if (!filename.empty()) {
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
  }

#endif

  cin.sync_with_stdio(false);
  cout << std::fixed << std::setprecision(10);
  solve();
  return 0;
}

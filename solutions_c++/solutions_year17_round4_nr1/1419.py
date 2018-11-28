#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solver {
 public:
  void Solve() {
    int64_t N, P;
    cin >> N >> P;
    std::vector<int64_t> groups;
    std::vector<int64_t> mod;
    mod.resize(P);
    for (int i = 0; i < N; ++i) {
      int s;
      cin >> s;
      ++mod[s % P];
    }
    if (P == 2) {
      cout << mod[0] + (mod[1] + 1) / 2 << endl;
      return;
    }
    if (P == 3) {
      int64_t mn = std::min(mod[1], mod[2]);
      int64_t ans = mod[0] + mn;
      int64_t r = std::max(mod[1] - mn, mod[2] - mn);
      ans += (r + 2) / 3;
      cout << ans << endl;
      return;
    }
    int64_t ans = mod[0];
    int64_t mn = std::min(mod[1], mod[3]);
    ans += mn;
    int64_t o = std::max(mod[1] - mn, mod[3] - mn);
    ans += mod[2] / 2;
    int64_t t = mod[2] % 2;
    if (t == 1) {
      o -= 2;
      ans++;
    }
    if (o <= 0) {
      cout << ans << endl;
      return;
    }
    ans += (o + 3) / 4;
    cout << ans << endl;
    return;
  }
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ": ";
    solver.Solve();
  }
}

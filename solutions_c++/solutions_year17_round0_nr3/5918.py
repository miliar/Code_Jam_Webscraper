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
    int64_t N, K;
    cin >> N >> K;
    stalls_.resize(N, false);
    int LL = -1, RR = -1;
    for (int k = 0; k < K; ++k) {
      int L = -1, R = -1, S = -1;
      for (int s = 0; s < N; ++s) {
        if (stalls_[s]) continue;
        int l = left(s);
        int r = right(s);
        if (S == -1) {
          L = l;
          R = r;
          S = s;
          continue;
        }
        if (std::min(l, r) < std::min(L, R)) {
          continue;
        }
        if (std::min(l, r) > std::min(L, R)) {
          L = l;
          R = r;
          S = s;
          continue;
        }
        if (std::max(l, r) < std::max(L, R)) {
          continue;
        }
        if (std::max(l, r) > std::max(L, R)) {
          L = l;
          R = r;
          S = s;
          continue;
        }
      }
      stalls_[S] = true;
      LL = L;
      RR = R;
    }
    cout << std::max(LL, RR) << " " << std::min(LL, RR) << endl;
  }

  int left(int p) {
    p--;
    int c = 0;
    while (p >= 0 && !stalls_[p--]) c++;
    return c;
  }

  int right(int p) {
    p++;
    int c = 0;
    while (p < stalls_.size() && !stalls_[p++]) c++;
    return c;
  }

  vector<bool> stalls_;
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

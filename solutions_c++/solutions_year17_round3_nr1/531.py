#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

const long double PI = 3.141592653589793238L;

struct Pancake {
  int64_t R;
  int64_t H;
  int64_t area = 0;
};

class Solver {
 public:
  void Solve() {
    int N, K;
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
      Pancake cake;
      cin >> cake.R;
      cin >> cake.H;
      cake.area = 2 * cake.R * cake.H;
      cakes_.push_back(cake);
    }
    double ans = 0;
    std::sort(cakes_.begin(), cakes_.end(),
              [](const Pancake& l, const Pancake& r) {
                return l.area > r.area;
              });
    for (int i = 0; i < N; ++i) {
      auto& base = cakes_[i];
      double area = (PI * base.R * base. R) + (PI * base.area);
      vector<Pancake> filtered;
      for (int j = 0; j < N; ++j) {
        if (j == i) continue;
        if (cakes_[j].R > base.R) continue;
        filtered.push_back(cakes_[j]);
      }
      if (filtered.size() < K - 1) continue;
      for (int j = 0; j < K - 1; ++j) {
        area += (PI * filtered[j].area);
      }
      ans = std::max(ans, area);
    }
    printf("%.10f\n", ans);
  }

  vector<Pancake> cakes_;
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

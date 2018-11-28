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
    int N, K;
    cin >> N >> K;
    double ex;
    cin >> ex;
    for (int i = 0; i < N; ++i) cin >> p[i];
    std::sort(p, p + N);
    int i = 0;
    while (ex > 1e-9) {
      if (i == N - 1) {
        for (int j = 0; j < N; ++j) {
          p[j] += ex / N;
        }
        break;
      }
      double jump = p[i + 1] - p[i];
      double required = jump * (i+1);
      double given = std::min(ex, required);
      for (int j = 0; j < i + 1; ++j) {
        p[j] += given / (i+1);
      }
      ex -= given;
      ++i;
    }
    double ans = 1;
    for (int i = 0; i < N; ++i) ans *= p[i];
    printf("%.6lf\n", ans);
  }

  double p[50];
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

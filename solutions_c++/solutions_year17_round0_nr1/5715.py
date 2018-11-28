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
    std::cin >> S_ >> K_;
    int flips = 0;
    for (int i = 0; i < S_.size(); ++i) {
      if (S_[i] == '+') continue;
      if (i + K_ - 1 >= S_.size()) continue;
      ++flips;
      for (int j = i; j < i + K_; ++j) {
        if (S_[j] == '+') S_[j] = '-';
        else if (S_[j] == '-') S_[j] = '+';
      }
    }
    bool done = true;
    for (int i = 0; i < S_.size(); ++i) {
      if (S_[i] == '-') done = false;
    }
    if (not done) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << flips << endl;
    }
  }

  std::string S_;
  int K_;
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

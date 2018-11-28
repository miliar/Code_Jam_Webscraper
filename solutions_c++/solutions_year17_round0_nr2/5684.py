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
    cin >> N_;
    digitize();
    int p = 0;
    for (p = 0; p < digits_.size(); ++p) {
      if (p == digits_.size() - 1) continue;
      if (digits_[p] <= digits_[p + 1]) continue;
      int q = p;
      while (q >= 0 && digits_[q] == digits_[p]) q--;
      if (q != -1 || digits_[p] != 1) {
        p = q + 1;
        digits_[p++]--;
        break;
      }
      digits_.pop_back();
      p = 0;
      break;
    }
    while (p < digits_.size()) {
      digits_[p++] = 9;
    }
    int64_t combined = combine();
    cout << combined << endl;
  }

  int64_t combine() {
    int64_t n = 0;
    int64_t p = 1;
    std::reverse(digits_.begin(), digits_.end());
    for (int i = 0; i < digits_.size(); ++i) {
      n += digits_[i] * p;
      p *= 10;
    }
    return n;
  }

  void digitize() {
    int64_t n = N_;
    while (n > 0) {
      int d = n % 10;
      digits_.push_back(d);
      n /= 10;
    }
    std::reverse(digits_.begin(), digits_.end());
  }

  vector<int> digits_;
  int64_t N_;
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

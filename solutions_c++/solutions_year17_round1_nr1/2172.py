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
  unordered_set<char> done_;
  void Solve() {
    int R, C;
    cin >> R >> C;
    std::string row;
    for (int i = 0; i < R; ++i) {
      cin >> row;
      in_.push_back(row);
    }
    for (int i = 0; i < in_.size(); ++i) {
      for (int j = 0; j < in_[i].size(); ++j) {
        if (in_[i][j] == '?' || done_.find(in_[i][j]) != done_.end()) {
          continue;
        }
        done_.insert(in_[i][j]);
        int l = j, r = j;
        for (int k = j + 1; k < in_[i].size(); ++k) {
          if (in_[i][k] != '?') break;
          in_[i][k] = in_[i][j];
          r = k;
        }
        for (int k = j - 1; k >= 0; --k) {
          if (in_[i][k] != '?') break;
          in_[i][k] = in_[i][j];
          l = k;
        }
        for (int t = i - 1; t >= 0; --t) {
          bool all = true;
          for (int j = l; j <= r; ++j) {
            if (in_[t][j] != '?') all = false;
          }
          if (!all) break;
          for (int j = l; j <= r; ++j) {
            in_[t][j] = in_[i][j];
          }
        }
        for (int t = i + 1; t < in_.size(); ++t) {
          bool all = true;
          for (int j = l; j <= r; ++j) {
            if (in_[t][j] != '?') all = false;
          }
          if (!all) break;
          for (int j = l; j <= r; ++j) {
            in_[t][j] = in_[i][j];
          }
        }
      }
    }
    for (int i = 0; i < in_.size(); ++i) {
      cout << in_[i] << endl;
    }
  }

 private:
  vector<string> in_;
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ":" << endl;
    solver.Solve();
  }
}

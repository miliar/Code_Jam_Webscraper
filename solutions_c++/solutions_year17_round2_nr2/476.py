#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string lt = "ROYGBV";

bool share(char a, char b) {
  int i = find(lt.begin(), lt.end(), a) - lt.begin();

  int j = find(lt.begin(), lt.end(), b) - lt.begin();
  if (i == 0 && j == 5) return 0;
  return abs(i - j) <= 1;
}
void solve() {
  int n;
  vector<int> x(6);
  cin >> n;
  for (int i = 0; i < 6; ++i) {
    cin >> x[i];
  }
  string ans;
  ans.resize(n, 'a');
  for (int k = 0; k < 6; ++k) {
    size_t pos = 0;

    for (int ii = 0; ii < 6; ++ii) {
      int i = (ii + k) % 6;
      for (int j = 0; j < x[i]; ++j) {
        ans[pos] = lt[i];
        pos += 2;
        if (pos >= ans.size()) {
          pos -= ans.size();
          if (pos == 0) pos = 1;
        }
      }
    }
    bool good = true;
    for (size_t i = 0; i < ans.size(); ++i) {
      if (share(ans[i], ans[(i + 1) % ans.size()])) {
        good = false;
      }
    }
    if (good) {
      cout << ans;

      return;
    }
  }
  cout << "IMPOSSIBLE";
}
int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }
}

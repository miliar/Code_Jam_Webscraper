#include <iomanip>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using namespace std;

using ll = long long;
using ld = long double;

void solve() {
  int T = 0;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    string s;
    int k = 0;
    cin >> s >> k;
    queue<int> q;
    int j = 0;
    int ans = 0;
    for (char c : s) {
      if (!q.empty() and q.front() == j) {
        q.pop();
      }
      if (c == '-' xor q.size() % 2 == 1) {
        q.push(j + k);
        ans += 1;
      }
      j++;
    }

    if (!q.empty() and q.front() == s.size()) {
      q.pop();
    }
    if (q.empty()) {
      cout << "Case #" << i + 1 << ": " << ans << endl;
    } else {
      cout << "Case #" << i + 1 << ": "
           << "IMPOSSIBLE" << endl;
    }
  }
}

int main() {
  cin.sync_with_stdio(false);
  cout << std::fixed << std::setprecision(10);
  solve();
}

#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef pair<int, int> PII;

const int N = 300004;

int main() {
  int T, K;
  string s;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int res = 0;
    cin >> s >> K;
    for (int i = K - 1; i < s.size(); ++i) {
      if (s[i - K + 1] == '-') {
        for (int j = i - K + 1; j <= i; ++j) {
          s[j] = s[j] == '+' ? '-' : '+';
        }
        ++res;
      }
    }
    bool ok = 1;
    for (int i = 0; i < s.size(); ++i) {
      if (s[i] == '-') {
        ok = 0;
        break;
      }
    }
    if (ok) {
      cout << res << "\n";
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
  return 0;
}
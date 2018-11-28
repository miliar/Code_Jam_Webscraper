#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef pair<int, int> PII;

const int N = 300004;

int main() {
  int T;
  string s;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> s;
    int n = s.size();
    string res = "";
    if (is_sorted(s.begin(), s.end())) res = s;
    for (int i = 0; i < n; ++i) {
      if (s[i] > '0') {
        string t = s;
        t[i]--;
        for (int j = i + 1; j < n; ++j) {
          t[j] = '9';
        }
        for (int j = i - 1; j >= 0; --j) {
          t[j] = min(t[j], t[j + 1]);
        }
        res = max(res, t);
      }
    }
    while (res[0] == '0') res = res.substr(1);
    cout << res << "\n";
  }
  return 0;
}
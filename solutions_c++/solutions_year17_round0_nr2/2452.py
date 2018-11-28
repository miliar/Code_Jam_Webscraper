#include <bits/stdc++.h>
using namespace std;

const int N = 20;

string Solve(string s) {
  s = string(N - s.size(), '0') + s;
  string res = string(N, '0');

  for (int i = 0; i < N; ++i) {
    for (char c = '9';; --c) {
      for (int j = i; j < N; ++j) {
        res[j] = c;
      }
      if (res > s) continue;
      break;
    }
  }

  while (res[0] == '0') {
    res.erase(res.begin());
  }

  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";
    string s;
    cin >> s;
    cout << Solve(s) << '\n';
  }
}


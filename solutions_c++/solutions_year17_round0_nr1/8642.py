#include <iostream>

using namespace std;

bool happy(const string &s, int l, int r) {
  for (int i = l; i <= r; i++)
    if (s[i] == '-') return false;
  return true;
}

void change(string &s, int l, int r) {
  for (int i = l; i <= r; i++)
    if (s[i] == '-')
      s[i] = '+';
    else
      s[i] = '-';
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    cout << "Case #" << tc << ": ";
    string s; cin >> s;
    int n = s.size();
    int k; cin >> k;
    if (!happy(s, 0, n-1) && k > n) {
      cout << "IMPOSSIBLE";
      continue;
    }
    long long ans = 0;
    for (int i = 0; i <= n-k; i++) {
      if (s[i] == '+') continue;
      change(s, i, i+k-1);
      ans++;
    }
    if (!happy(s, 0, n-1))
      cout << "IMPOSSIBLE" << endl;
    else
      cout << ans << endl;
  }
}

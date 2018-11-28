#include <bits/stdc++.h>

using namespace std;

string s;
int k;

void read() {
  cin >> s >> k;
}

void kill() {
  int ans = 0;
  int n = s.length();

  for (int i = 0; i + k <= n; ++i) {
    if (s[i] == '-') {
      for (int j = 0; j < k; ++j)
        s[i + j] ^= '-' ^ '+';
      ++ans;
    }
  }

  for (int i = 0; i < n; ++i)
    if (s[i] == '-') {
      cout << "IMPOSSIBLE\n";
      return;
    }
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}

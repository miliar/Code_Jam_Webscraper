#include <iostream>
using namespace std;

int solve(string s, int k) {
  int cnt = 0;
  int i = 0;
  int n = s.size();
  while (i < n - k + 1) {
    if (s[i] == '-') {
      ++cnt;
      for (int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '+') ? '-' : '+';
      }
    }
    ++i;
  }
  while (i < n) {
    if (s[i] == '-')
      return -1;
    ++i;
  }
  return cnt;
}

void tcase(int t) {
  string s;
  int k;
  cin >> s >> k;
  int ans = solve(s, k);
  cout << "Case #" << t << ": ";
  if (ans == -1) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << ans << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    tcase(i);
  }
  return 0;
}

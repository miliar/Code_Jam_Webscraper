#include <iostream>
using namespace std;
int main() {
  int t, tt, k, i, j, cnt;
  string s;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> s >> k;
    cnt = 0;
    for (i = 0; i + k <= s.size(); i++) {
      if (s[i] != '+') {
        cnt++;
        for (j = 0; j < k; j++) s[i + j] = (s[i + j] == '-') ? '+' : '-';
      }
    }
    for (j = i; j < s.size(); j++) if (s[j] != '+') break;
    cout << "Case #" << tt << ": ";
    if (j < s.size()) cout << "IMPOSSIBLE" << endl;
    else cout << cnt << endl;
  }
  return 0;
}

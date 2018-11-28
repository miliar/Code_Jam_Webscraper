#include <bits/stdc++.h>

using namespace std;

map<char, int> counts;
char out[1005];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int n; cin >> n;
    char type[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
    cout << "Case #" << t << ": ";
    counts.clear();
    for (int i = 0; i < 6; i++) {
      int x; cin >> x;
      counts[type[i]] = x;
    }

    int idx = 0;
    char last = '?';
    while (idx < n-2) {
      sort(type, type + 6, [&](const char& a, const char& b) {
        return counts[a] > counts[b];
      });

      char cc = type[0];
      if (last == cc) cc = type[1];
      out[idx] = cc;
      counts[cc]--;
      last = cc;
      idx++;
    }

    char c1='-', c2='-';
    for (auto& p : counts) {
      if (p.second>=1&&c1=='-')c1=p.first;
      if (c1!=p.first&&c1!='-'&&p.second>=1)c2=p.first;
    }
    counts[c1]--;
    counts[c2]--;

    bool ok = true;
    for (auto&p : counts) {
      if (p.second != 0) {
        ok = false;
        break;
      }
    }
    if (!ok) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    if (c1 == out[0]) {
      out[n-1]=c2;
      out[n-2]=c1;
    } else {
      out[n-1]=c1;
      out[n-2]=c2;
    }
    for (int i = 1; i < n; i++) {
      if (out[n-1]==out[0]||out[i]==out[i-1]) {
        ok = false;
        break;
      }
    }
    if (!ok) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    for (int i = 0; i < n; i++) cout << out[i];
    cout << endl;
  }

  return 0;
}

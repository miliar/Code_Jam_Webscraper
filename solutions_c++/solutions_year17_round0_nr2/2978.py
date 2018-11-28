#include <iostream>
#include <string>

using namespace std;

int n;
string s;
string a;

bool bt(int p, int l, bool fix) {
  if (p == n) return true;
  int u = (fix ? s[p] - '0' : 9);
  for (int i = u; i >= l; --i) {
    a[p] = '0' + i;
    if (bt(p + 1, i, fix and (i == u))) return true;
  }
  return false;
}

int main() {
  ios::sync_with_stdio(false);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cin >> s;
    n = s.size();
    a = string(n, ' ');
    bt(0, 0, true);
    cout << "Case #" << t << ": ";
    int nz = 0;
    while (nz < n and a[nz] == '0') ++nz;
    for (int i = nz; i < n; ++i) cout << a[i];
    cout << endl;
  }
}

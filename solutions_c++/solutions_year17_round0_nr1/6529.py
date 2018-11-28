#include <bits/stdc++.h>
using namespace std;

void solve(int Case) {
  string s;
  int k, c = 0;
  cin >> s >> k;
  for (int i=0; i<s.length(); i++) {
    if (s[i] == '-') {
      if (i > s.length() - k) {
        cout << "Case #" << (Case+1) <<": " << "IMPOSSIBLE" << "\n";
        return;
      }
      for (int j=0;j<k;j++) {
        s[i+j] = s[i+j] == '+' ? '-' : '+';
      }
      c++;
    }
  }
  cout << "Case #" << (Case+1) <<": " << c << "\n";
}

int main () {
  // freopen("A.in", "r", stdin);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  int T;
  cin >> T;
  for (int i=0;i<T;i++) solve(i);
}
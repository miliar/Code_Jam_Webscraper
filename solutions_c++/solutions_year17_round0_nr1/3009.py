#include <bits/stdc++.h>

using namespace std;

void solve() {
  string s;
  cin >> s;
  int k;
  cin >> k;
  int l = s.length();
  int counter = 0;
  for(int i = 0; i < l; i++) {
    if(s[i]=='+') continue;
    counter++;
    for(int j = 0; j < k; j++) {
      if(i+j>=l) {
        cout << "IMPOSSIBLE";
        return;
      }
      if(s[i+j] == '+') s[i+j] = '-';
      else s[i+j] = '+';
    }
  }
  cout << counter;
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}

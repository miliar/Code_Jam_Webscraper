#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("b.in", "rt", stdin);
  freopen("b.out", "wt", stdout);
  int t; cin >> t;
  for(int tst = 1; tst <= t; ++tst) {
    string s; cin >> s;
    int n = s.size();
    int id = -1;
    for(int i = 0; i + 1 < n; ++i) {
      if(s[i] > s[i + 1]) {
        id = i;
        break;
      }
    }
    cout << "Case #" << tst << ": ";
    if(id == -1) {
      cout << s << endl;
    }else {
      if(s[id] == '1') {
        for(int i = 0; i < n - 1; ++i) {
          cout << '9';
        }
        cout << endl;
      }else {
        char sid = s[id];
        while(id >= 0 && s[id] == sid) {
          --id;
        }
        s[++id]--;
        for(int i = id + 1; i < n; ++i) {
          s[i] = '9';
        }
        cout << s << endl;
      }
    }
  }
  return 0;
}

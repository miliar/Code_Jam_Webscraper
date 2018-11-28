#include <bits/stdc++.h>




using namespace std;
#define MAXN 25
void solve() {
  string m[MAXN];
  int r, c;
  cin >> r >> c;
  for (int i = 0; i < r; ++i) {
    cin >> m[i];
    char cur = '?';
    for (int j = 0; j < c; ++j) {
      if (m[i][j]!='?') {
        cur = m[i][j];
        break;
      }
    }
    if (cur!='?') {
      for (int j = 0; j < c; ++j) {
        if (m[i][j]!='?') {
          cur = m[i][j];
        } else {
          m[i][j] = cur;
        }
      }
    }
  }
  string cus = "";
  for (int i = 0; i < r; ++i) {
    if (m[i][0]!='?') {
      cus = m[i];
      break;
    }
  }
  for (int i = 0; i < r; ++i) {
    if (m[i][0]!='?') {
      cus = m[i];
    }
    cout << cus << endl;
  }
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": " << endl;
    solve();
  }
  return 0;
}

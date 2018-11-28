#include <bits/stdc++.h>

using namespace std;

int R, C;
char cake[30][30];

void solve() {
  bool present[30][30];
  for (int i = 0; i < R; i++)
    for (int j = 0; j < C; j++) {
      if (cake[i][j]) present[i][j] = true;
      else present[i][j] = false;
    }
  for (int i = 0; i < R; i++)
    for (int j = 0; j < C; j++) {
      if (present[i][j]) {
        for (int k = i - 1; k >= 0; k--) {
          if (cake[k][j] == '?')
            cake[k][j] = cake[i][j];
          else
            break;
        }
        for (int k = i + 1; k < R; k++) {
          if (cake[k][j] == '?')
            cake[k][j] = cake[i][j];
          else
            break;
        }
      }
    }
  for (int j = 0 ; j < C; ) {
    if (cake[0][j] == '?') {
      int l = j;
      while (j < C && cake[0][j] == '?') j++;
      int r = j - 1;
      if (r != C - 1) {
        for (int k = r; k >= l; k--)
          for (int i = 0; i < R; i++) {
            cake[i][k] = cake[i][k + 1];
          }
      } else {
        for (int k = l; k <= r; k++)
          for (int i = 0; i < R; i++)
            cake[i][k] = cake[i][k - 1];
      }
    }
    else
      j++;
  }
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++)
      cout << cake[i][j];
    cout << endl;
  }
}


int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    freopen("a.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum) {
        cin >> R >> C;
        for (int i = 0; i < R; i++)
          scanf("%s", cake[i]);
        cout << "Case #" << tnum << ":" << endl;
        solve();
    }
    return 0;
}

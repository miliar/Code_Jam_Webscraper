/**
 * A solution that automatically proves itself.
 */
#include <bits/stdc++.h>
using namespace std;

void solve(int sx, int ex, int sy, int ey, int px, int py, const vector<string> &s, vector<string> &ans) {

  for (int i = sx; i <= ex; ++i)
    for (int j = sy; j <= ey; ++j)
      ans[i][j] = s[px][py];

  for (int i = sx; i <= ex; ++i)
    for (int j = sy; j <= ey; ++j)
      if (s[i][j] != '?' && s[i][j] != s[px][py]) {
        if (i == px) {
          int x1, y1, x2, y2;
          if (py < j) x1 = px, y1 = py, x2 = i, y2 = j;
          else x1 = i, y1 = j, x2 = px, y2 = py;
          solve(sx, ex, sy, y2 - 1, x1, y1, s, ans);
          solve(sx, ex, y2, ey, x2, y2, s, ans);

        }
        else {
          int x1, y1, x2, y2;
          if (px < i) x1 = px, y1 = py, x2 = i, y2 = j;
          else x1 = i, y1 = j, x2 = px, y2 = py;
          solve(sx, x2 - 1, sy, ey, x1, y1, s, ans);
          solve(x2, ex, sy, ey, x2, y2, s, ans);
        }
        return;
      }
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int cases; cin >> cases;
  for (int cc = 0; cc < cases; ++cc) {
    cout << "Case #" << cc + 1 << ":" << "\n";

    int R, C;
    cin >> R >> C;
//    vector<string> s(R, string('?', C)), ans(R, string('?', C)); // Tried to be clean :'(
    vector<string> s(R), ans(R);
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
        s[i] += '#', ans[i] += '#';

    int px, py;
    for (int i = 0; i < R; ++i) {
      cin >> s[i];
      for (int j = 0; j < C; ++j)
        if (s[i][j] != '?')
          px = i, py = j;
    }

    solve(0, R - 1, 0, C - 1, px, py, s, ans);

    for (int i = 0; i < R; ++i)
      cout << ans[i] << "\n";
  }
  return 0;
}

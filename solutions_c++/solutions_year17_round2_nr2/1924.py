#include <bits/stdc++.h>
#define ll long long

using namespace std;

const int N = 1234;

vector <int> ans;
vector <vector <int> > ret;
int n;
unordered_map <int, int> dp[N][N][3];

void solve(int r, int y, int b, int cur, bool &solved, int &start) {
  if (solved) {
    return;
  }
  if (dp[r][y][cur][b]) {
    return;
  }
  ans.push_back(cur);
  if (r == 0 && y == 0 && b == 0 && (n <= 1 || cur != start)) {
    solved = true;
    ret.push_back(ans);
    return;
  }
  if (cur != 0 && r > 0) {
    solve(r - 1, y, b, 0, solved, start);
  }
  if (cur != 1 && y > 0) {
    solve(r, y - 1, b, 1, solved, start);
  }
  if (cur != 2 && b > 0) {
    solve(r, y, b - 1, 2, solved, start);
  }
  if (! solved) {
    dp[r][y][cur][b] = 1;
  }
  ans.pop_back();
}

void io() {
  freopen("B-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

int main() {
  io();
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    int r, o, y, g, b, v;
    ans.clear();
    ret.clear();
    cin >> n >> r >> o >> y >> g >> b >> v;
    if (n == 1) {
      if (r) cout << "R";
      else if (y) cout << "Y";
      else if (b) cout << "B";
    } else {
      if (r <= (y + b) && y <= (r + b) && b <= (y + r)) {
        bool solved = false;
        for (int i = 0; i < 3; i++) {
          if (! solved) {
            if (i == 0 && r > 0) solve(r - 1, y, b, i, solved, i);
            else if (i == 1 && y > 0) solve(r, y - 1, b, i, solved, i);
            else if (i == 2 && b > 0) solve(r, y, b - 1, i, solved, i);
          }
        }
        if (! solved) {
          cout << "IMPOSSIBLE";
        } else {
          for (int i = 0; i < ret[0].size(); i++) {
            int cur = ret[0][i];
            if (cur == 0) cout << "R";
            else if (cur == 1) cout << "Y";
            else cout << "B";
          }
        }
      } else cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
  return 0;
}

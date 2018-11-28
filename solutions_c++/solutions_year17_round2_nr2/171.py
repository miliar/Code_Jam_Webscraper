#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

const string col = "RBY", inv = "GOV";
string solve (int n, vector <int>& x, vector <int>& y) {
  vector <pair <int, int>> V(3);
  string s;
  for (int i = 0; i < 3; i++) {
    if (y[i] > x[i]) {
      return "IMPOSSIBLE";
    }
    else if (y[i] == x[i] && x[i] > 0) {
      if (x[i] + y[i] < n) {
        return "IMPOSSIBLE";
      } else {
        for (int j = 0; j < x[i]; j++) {
          s += col[i];
          s += inv[i];
        }
        return s;
      }
    }
    V[i] = {x[i] - y[i], i};
  }

  sort(V.begin(), V.end());

  vector <int> flag(3, true);

  if (V[2].x > V[0].x + V[1].x) {
    return "IMPOSSIBLE";
  } else {
    for (int i = 0; i < V[0].x + V[1].x - V[2].x; i++) {
      for (int j: {2, 0, 1}) {
        if (flag[j]) {
          flag[j] = false;
          for (int k = 0; k < y[V[j].y]; k++) {
            s += col[V[j].y];
            s += inv[V[j].y];
          }
        }
        s += col[V[j].y];
      }
    }
    for (int i = 0; i < V[2].x - V[0].x; i++) {
      for (int j: {2, 1}) {
        if (flag[j]) {
          flag[j] = false;
          for (int k = 0; k < y[V[j].y]; k++) {
            s += col[V[j].y];
            s += inv[V[j].y];
          }
        }
        s += col[V[j].y];
      }
    }
    for (int i = 0; i < V[2].x - V[1].x; i++) {
      for (int j: {2, 0}) {
        if (flag[j]) {
          flag[j] = false;
          for (int k = 0; k < y[V[j].y]; k++) {
            s += col[V[j].y];
            s += inv[V[j].y];
          }
        }
        s += col[V[j].y];
      }
    }
  }
  return s;
}

void verify(string&s, vector <int> x, vector <int> y) {
  for (char c: s) {
    for (int i: {0, 1, 2}) {
      if (c == col[i])  --x[i];
      if (c == inv[i])  --y[i];
    }
  }
  for (int i: {0, 1, 2}) assert(x[i] == 0 && y[i] == 0);
}

using ll = long long;

int main() {
  ios::sync_with_stdio(false);

  int t;
  cin >> t;

  for (int cs = 0; cs < t; cs++) {
    int n;
    vector <int> x(3), y(3);
    cin >> n >> x[0] >> y[1] >> x[2] >> y[0] >> x[1] >> y[2];

    cout << "Case #" << cs + 1 << ": ";
    string ans = solve(n, x, y);
    cout << ans << endl;
    if (ans != "IMPOSSIBLE")
      verify(ans, x, y);
  }

  return 0;
}

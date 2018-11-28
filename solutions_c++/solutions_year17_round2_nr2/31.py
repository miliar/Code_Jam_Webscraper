#include <algorithm>
#include <array>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

const char* x = "RYB";
const char* y = "GVO";

string solve(array<int, 3> X) {
  if (X[0] > X[1] + X[2] || X[1] > X[0] + X[2] || X[2] > X[0] + X[1]) {
    return "IMPOSSIBLE";
  } else {
    string ans;
    int a = -1, b = -1, c = -1;
    for (int i = 0; i < 3; i++) {
      if (a == -1 || X[i] > X[a]) {
        a = i;
      }
    }
    for (int i = 0; i < 3; i++) {
      if (i != a) {
        if (b == -1 || X[i] > X[b]) {
          b = i;
        }
      }
    }
    for (int i = 0; i < 3; i++) {
      if (i != a && i != b) {
        if (c == -1 || X[i] > X[c]) {
          c = i;
        }
      }
    }
    int rb = (X[b] + X[c] - (X[a] - 1) + 1) / 2;
    int rc = (X[b] + X[c] - (X[a] - 1)) / 2;
    for (int i = 0; i < X[a] - 1; i++) {
      ans += x[a];
      if (X[b] > rb) {
        ans += x[b];
        X[b]--;
      } else if (X[c] > rc) {
        ans += x[c];
        X[c]--;
      }
    }
    ans += x[a];
    for (int i = 0; i < rb; i++) {
      ans += x[b];
      if (rc != 0) {
        ans += x[c];
        rc--;
      }
    }
    return ans;
  }
}

void solve(array<int, 3> X, array<int, 3> Y) {
  cout << " ";
  for (int i = 0; i < 3; i++) {
    if (X[i] == 0 && Y[i] != 0) {
      for (int j = 0; j < 3; j++) {
        if (j != i && X[j] + Y[j] != 0) {
          cout << "IMPOSSIBLE" << endl;
          return;
        }
      }
      for (int j = 0; j < Y[i]; j++) {
        cout << x[i] << y[i];
      }
      cout << endl;
      return;
    }
  }
  string ans = solve(X);
  if (ans == "IMPOSSIBLE") {
    cout << ans << endl;
    return;
  }
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i];
    for (int j = 0; j < 3; j++) {
      if (Y[j] && ans[i] == x[j]) {
        for (int k = 0; k < Y[j]; k++) {
          cout << y[j] << x[j];
        }
        Y[j] = 0;
      }
    }
  }
  cout << endl;
}

void solve() {
  int N, R, O, Y, G, B, V;
  cin >> N >> R >> O >> Y >> G >> B >> V;
  solve({R - G, Y - V, B - O}, {G, V, O});
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":";
    solve();
  }
}

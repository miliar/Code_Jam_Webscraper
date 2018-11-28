#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int main() {
  int t; cin >> t;

  const int R = 0;
  const int O = 1;
  const int Y = 2;
  const int G = 3;
  const int B = 4;
  const int V = 5;

  for (int tc = 1; tc <= t; tc++) {
    int n; cin >> n;
    vector<int> colors(6, 0);
    for (int i = 0; i < 6; i++) {
      cin >> colors[i];
    }
    string ans = "";

    int prev = -1;
    int start = -1;
    for (int i = 0; i < n; i++) {
      int target = -1;
      int maxnum = 0;
      if (prev != R && colors[R] > 0) { target = R; maxnum = colors[R]; }
      if (prev != Y && colors[Y] > maxnum){ target = Y; maxnum = colors[Y]; }
      if (prev != B && colors[B] > maxnum){ target = B; maxnum = colors[B]; }
      if (i == (n - 2) && target != start && prev != start && colors[start] > 0) {
        target = start;
      }
      if (target < 0) {
        ans = "IMPOSSIBLE";
        break;
      }
      if (target == R) {
        ans = ans + "R";
        colors[R]--;
        prev = R;
      } else if (target == Y) {
        ans = ans + "Y";
        colors[Y]--;
        prev = Y;
      } else {
        ans = ans + "B";
        colors[B]--;
        prev = B;
      }
      if (start < 0) {
        start = prev;
      }
    }
    if (ans[0] == ans[ans.size() - 1]) {
      ans = "IMPOSSIBLE";
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
}

#include <bits/stdc++.h>
using namespace std;

int main() {
  int t, n, r, o, y, g, b, v;
  string ans;
  char temp;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> n >> r >> o >> y >> g >> b >> v;
    if (r > y + b|| y > r + b || b > r + y) {
      ans = "IMPOSSIBLE";
    } else {
      ans = "";
      if(r >= y && r >= b) {
          ans += "R";
          r--;
        } else if (y >= r && y >= b ) {
          ans += "Y";
          y--;
        } else {
          ans += "B";
          b--;
        }
      for(int j = 1; j < n; j++) {
        /*if(r < 0|| y < 0 || b < 0) {
          cout << "gg" << endl;
        }/**/
        if(ans.back() == 'R') {
          if(y >= b) {
            ans += "Y";
            y--;
          } else {
            ans += "B";
            b--;
          }
        } else if (ans.back() == 'Y') {
          if(r >= b) {
            ans += "R";
            r--;
          } else {
            ans += "B";
            b--;
          }
        } else {
          if(r >= y) {
            ans += "R";
            r--;
          } else {
            ans += "Y";
            y--;
          }
        }
      }
    }
    if(ans.front() == ans.back()) {
      temp = ans.back();
      ans[ans.length()-1] = ans[ans.length()-2];
      ans[ans.length()-2] = temp;
    }
    cout << "Case #" << i << ": " << ans << endl;
  }

  return 0;
}
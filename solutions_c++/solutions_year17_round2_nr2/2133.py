#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
  int tc, n, r, o, y, g, b, v;
  cin >> tc;
  for(int t = 1; t <= tc; ++t) {
    cin >> n >> r >> o >> y >> g >> b >> v;
    cout  << "Case #" << t << ": ";
    string ans;
    while(o) {
      if(b) {
        ans += "B";
        --n; --b;
      }
      ans += "O";
      --n;
      if(b) {
        ans += "B";
        --n; --b;
      }
      --o;
    }
    while(g) {
      if(r) {
        ans += "R";
        --r;
        --n;
      }
      ans += "G";
      --n;
      if(r) {
        ans += "R";
        --r;
        --n;
      }
      --g;
    }
    while(v) {
      if(y) {
        ans += "Y";
        --y;
        --n;
      }
      ans += "V";
      --n;
      if(y) {
        ans += "Y";
        --y;
        --n;
      }
      --v;
    }
    char last = 'X';
    while((b || r || y) && n--) {
      if((b == 0 && r == 0)||(r == 0 && y == 0)||(b == 0 && y == 0)) {
        if(b == 1 && ans[0]!='B')
          ans += "B", --b;
        else if(r == 1 && ans[0]!='R')
          ans += "R", --r;
        else if(y == 1 && ans[0]!='Y')
          ans += "Y", --y;
        break;
      }
      if((b >= r && b >= y)) {
        if(last != 'B')
        ans += "B",
        last = 'B',
        --b;
        else if(r >= y) ans+="R",last='R',--r;
        else ans+="Y",last='Y',--y;
        continue;
      }
      if((r >= b && r >= y)) {
        if(last != 'R')
        ans += "R",
        last = 'R',
        --r;
        else if(b >= y) ans+="B",last='B',--b;
        else ans+="Y",last='Y',--y;
        continue;
      }
      if((y >= r && y >= b) && last != 'Y') {
        if(last != 'Y')
        ans += "Y",
        last = 'Y',
        --y;
        else if(r >= b) ans+="R",last='R',--r;
        else ans+="B",last='B',--b;
        continue;
      }
    }
    if(b || r || y) ans = "IMPOSSIBLE";
    cout << ans << endl;  
  }
  return 0;
}

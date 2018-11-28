#include <iostream>
using namespace std;
int t, n, r, o, y, g, b, v;
int last;
int mm() {
  switch (last) {
    case 0:
      if(y >= b) return 1;
      return 2;
    case 1:
      if(r >= b) return 0;
      return 2;
    case 2:
      if(r >= y) return 0;
      return 1;
    default:
      if( r >= y and r >= b) return 0;
      if(y >= r and y >= b) return 1;
      if(b >= r and b >= y) return 2;
      return 0;
    }
}
int main() {
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cin >> n >> r >> o >> y >> g >> b >> v;
    if(r > n/2 or y > n/2 or b > n/2) {
      printf("Case #%d: IMPOSSIBLE\n", tc);
    }
    else {
      cout << "Case #" << tc << ": ";
      char ans[1001];
      last = -1;
      last = mm();
      switch (last) {
        case 0:
          r--;
          ans[0] = 'R';
          break;
        case 1:
          y--;
          ans[0] = 'Y';
          break;

        case 2:
          b--;
          ans[0] = 'B';
          break;
      }
      char ulti;
      if(n > 1) {
        switch (mm()) {
          case 0:
            r--;
            ulti = 'R';
            break;
          case 1:
            y--;
            ulti = 'Y';
            break;

          case 2:
            b--;
            ulti = 'B';
            break;
        }
      }
      for(int i = 1; i < n-1; i++) {
        last = mm();
        switch (last) {
          case 0:
            r--;
            ans[i] = 'R';
            break;
          case 1:
            y--;
            ans[i] = 'Y';
            break;

          case 2:
            b--;
            ans[i] = 'B';
            break;
        }
      }
      if(n > 1) {
        bool found = false;
        if(ulti == ans[n-2]) {
          for(int j = 1; j < n-2; j++) {
            if(ans[j] != ulti and ans[j-1] != ulti and ans[j+1] != ulti and ans[j] != ans[0]) {
              ans[n-1] = ans[j];
              ans[j] = ulti;
              found = true;
              break;
            }
          }

          if(!found) {
            cout << "IMPOSSIBLE\n";
            continue;
          }

        }
        else {
          ans[n-1] = ulti;
        }
      }
      for(int i = 0; i < n; i++) {
        cout << ans[i];
      }
      //printf("valori %d %d %d\n", r, y, b);
      cout << '\n';
    }
  }
}

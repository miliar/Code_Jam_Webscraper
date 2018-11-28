#include <cstdio>
#include <string>
#include <iostream>
#define min(a, b) (a < b ? a : b)
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int _ = 1; _ <= T; ++_) {
    cout << "Case #" << _ << ": ";

    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    if (r * 2 > n || o * 2 > n || y * 2 > n || g * 2 > n || b * 2 > n || v * 2 > n) {
      cout << "IMPOSSIBLE" << endl;
    } else if ((g + 1 > r && g) || (v + 1 > y && v) || (o + 1 > b && o)) {
      if (g == r && n == g + r) {
        while (r--) { cout << "RG"; }
      } else if (v == y && n == v + y) {
        while (y--) { cout << "YV"; }
      } else if (o == b && n == o + b) {
        while (b--) { cout << "BO"; }
      } else {
        cout << "IMPOSSIBLE";
      }
      cout << endl;
    } else {
      r -= g;
      y -= v;
      b -= o;

      if (r >= y && r >= b) {
        b -= r - y;
        while (r-- > 0) {
          cout << 'R';
          if (g-- > 0) cout << "GR";

          if (y-- > 0) {
            cout << 'Y';
            if (v-- > 0) cout << "VY";
            if (b-- > 0) {
              cout << 'B';
              if (o-- > 0) cout << "OB";
            }
          } else {
            cout << 'B';
            if (o-- > 0) cout << "OB";
          }
        }
      } else if (y >= r && y >= b) {
        b -= y - r;
        while (y-- > 0) {
          cout << 'Y';
          if (v-- > 0) cout << "VY";

          if (r-- > 0) {
            cout << 'R';
            if (g-- > 0) cout << "GR";
            if (b-- > 0) {
              cout << 'B';
              if (o-- > 0) cout << "OB";
            }
          } else {
            cout << 'B';
            if (o-- > 0) cout << "OB";
          }
        }
      } else if (b >= r && b >= y) {
        y -= b - r;
        while (b-- > 0) {
          cout << 'B';
          if (o-- > 0) cout << "OB";

          if (r-- > 0) {
            cout << 'R';
            if (g-- > 0) cout << "GR";
            if (y-- > 0) {
              cout << 'Y';
              if (v-- > 0) cout << "VY";
            }
          } else {
            cout << 'Y';
            if (v-- > 0) cout << "VY";
          }
        }
      } else cout << "???";

      cout << endl;
    }
  }
  return 0;
}

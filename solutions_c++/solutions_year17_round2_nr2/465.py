#include <iostream>
using namespace std;

int res[1010], ct[1010];
char m[3];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, r, o, y, g, b, v; cin >> n >> r >> o >> y >> g >> b >> v;

    // o = g = v = 0
    // cout << r << " " << y << " " << b << endl;
    if (r >= y && r >= b) {
      m[0] = 'R'; ct[0] = r;
      if (y >= b) {
        m[1] = 'Y'; ct[1] = y;
        m[2] = 'B'; ct[2] = b;
      } else {
        m[1] = 'B'; ct[1] = b;
        m[2] = 'Y'; ct[2] = y;
      }
    } else if (y >= b) {
      m[0] = 'Y'; ct[0] = y;
      if (r >= b) {
        m[1] = 'R'; ct[1] = r;
        m[2] = 'B'; ct[2] = b;
      } else {
        m[1] = 'B'; ct[1] = b;
        m[2] = 'R'; ct[2] = r;
      }
    } else {
      m[0] = 'B'; ct[0] = b;
      if (r >= y) {
        m[1] = 'R'; ct[1] = r;
        m[2] = 'Y'; ct[2] = y;
      } else {
        m[1] = 'Y'; ct[1] = y;
        m[2] = 'R'; ct[2] = r;
      }
    }

    bool imp = false;
    for (int i = 0; i < n; i++) {
      int bestc = 0, bestj = -1;
      for (int j = 0; j <= 2; j++) {
        if ((i == 0 || res[i-1] != j) && (bestj == -1 || ct[j] > bestc) && ct[j] > 0) {
          bestc = ct[j]; bestj = j;
        }
      }
      // cout << bestc << " " << bestj << endl;

      if (bestj == -1) {
        imp = true;
        break;
      }
      res[i] = bestj; ct[bestj]--;
    }

    if (!imp && res[0] == res[n-1]) {
      int tmp = res[n-2];
      res[n-2] = res[n-1];
      res[n-1] = tmp;

      for (int i = 0; i < n; i++)
        imp = imp || res[i] == res[(i+1)%n];
    }

    cout << "Case #" << c << ": ";
    if (imp) cout << "IMPOSSIBLE" << endl;
    else {
      for (int i = 0; i < n; i++) cout << m[res[i]];
      cout << endl;
    }
  }
  return 0;
}

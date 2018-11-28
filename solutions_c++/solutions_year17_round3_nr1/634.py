#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#define PI 3.1415926535897932384626433832795028841971693
using namespace std;

struct pan {
  int r, h;
  double s;
} p[2000];

double ans, st[2000];

int main () {
  int T;
  cin >> T;

  for (int _ = 1; _ <= T; ++_) {
    cout << "Case #" << _ << ": ";

    int k, n;
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
      cin >> p[i].r >> p[i].h;
      p[i].s = double(2.0f * p[i].r) * p[i].h;
    }

    ans = 0;
    int tot = 0;
    double t = 0;

    for (int i = 0; i < n; ++i) {
      tot = 0;
      for (int j = 0; j < n; ++j) if (i != j && p[j].r <= p[i].r) {
        st[tot++] = -p[j].s;
      }
      t = p[i].s + double(p[i].r) * p[i].r;
      if (tot >= k - 1) {
        sort(st, st + tot);
        for (int j = 0; j < k - 1; ++j) {
          t -= st[j];
        }
      }
      if (t > ans) ans = t;
    }

    // cout << t * PI << endl;
    printf("%.9f\n", ans * PI);
  }

  return 0;
}

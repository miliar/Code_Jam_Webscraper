#include <bits/stdc++.h>

const double eps = 1e-8;
using namespace std;

int n;
double k[1020], s[1020];
double d;

bool check(double v) {
  for (int i = 0; i < n; i++) {
    if (d*s[i] < v*(d-k[i])) return false;
  }
  return true;
}

int main () {
  int T;
  cin >> T;
  for (int ka = 1; ka <= T; ka++) {
    cin >> d >> n ;
    for (int i = 0; i < n; i++) {
      cin >> k[i] >> s[i];
    }
    double l = 0, r = 1e15;
    double ans = 0;

    for (int tt = 0; tt < 1000; tt++) {
      double mid = (l+r) * 0.5;
      //cout << mid << endl;
      if (check(mid)) {
        ans = max(mid, ans);
        l = mid;
      }
      else {
        r = mid;
      }
    }
    printf("Case #%d: %.9f\n", ka, ans);
  }
  return 0;
}


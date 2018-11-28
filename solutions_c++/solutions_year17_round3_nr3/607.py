#include <bits/stdc++.h>

using namespace std;

const int N = 105;

double p[N];

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    for (int j = 0; j < n; j++) {
      cin >> p[j];
    }

    double l = 0, r = 1;    
    for (int j = 0; j < 100; j++) {
      double rem = u;
      double mid = (l + r) / 2;
      for (int t = 0; t < n; t++) {
        if (p[t] < mid) {
          rem -= mid - p[t];          
        }
      }
      if (rem < 0) {
        r = mid;
      } else {
        l = mid;
      }
    }
    double ans = 1;
    for (int j = 0; j < n; j++) {
      ans *= max(l, p[j]);
    }
    cout << "Case #" << (i + 1) << ": ";
    cout.precision(6);
    cout << fixed << ans << endl;
  }
}

#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  cout << fixed;
  cout.precision(20);

  for (int tst = 0; tst < T; tst++) {
    int n, q;
    cin >> n >> q;
    vector <long double> E(n), S(n);
    vector <vector <long double> > dst(n, vector <long double>(n));

    for (int i = 0; i < n; i++) {
      cin >> E[i] >> S[i];
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        long long x;
        cin >> x;

        if (x == -1) {
          dst[i][j] = 1e18;
        } else {
          dst[i][j] = x;
        }
      }
      dst[i][i] = 0;
    }

    for (int k = 0; k < n; k++) {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j]);
        }
      }
    }

    cout << "Case #" << tst + 1 << ": ";

    for (int ii = 0; ii < q; ii++) {
      int a, b;
      cin >> a >> b;
      a--, b--;
      vector <long double> d(n, 1e18);
      d[a] = 0;
      bool changed = true;

      while (changed) {
        changed = false;

        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
            if (dst[j][i] <= E[j] + 1e-9) {
              if (d[i] > d[j] + dst[j][i] / S[j] + 1e-9) {
                d[i] = d[j] + dst[j][i] / S[j];
                changed = true;
              }
            }
          }
        }
      }
      cout << d[b] << ' ';
    }
    cout << '\n';
  }
}

#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    int d, n;
    cin >> d >> n;

    vector<double> k(n), s(n);
    for (int i = 0; i < n; ++i) {
      cin >> k[i] >> s[i];
    }

    // for (int i = 0; i < n; ++i) {
    //   for (int j = i + 1; j < n; ++j) {
    //     bool op1 = k[i] > k[j];
    //     bool op2 = (k[i] == k[j]) and (s[j] < s[i]);
    //     if (op1 or op2) {
    //       swap(k[i], k[j]);
    //       swap(s[i], s[j]);
    //     }
    //   }
    // }

    // for (int i = 0; i < n; ++i) {
    //   D(i); D(k[i]); D(s[i]);
    // }

    double time_annie = 0;
    for (int i = n - 1; i >= 0; --i) {
      double t = (d - k[i]) / s[i];
      time_annie = max(time_annie, t);
    }

    double ans = d / time_annie;
    cout << fixed << setprecision(8) << ans << endl;
  }

  return 0;
}

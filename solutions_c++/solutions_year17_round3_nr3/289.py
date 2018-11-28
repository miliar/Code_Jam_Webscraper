#include <bits/stdc++.h>

using namespace std;

const int N = 50;
using ld = long double;
const ld eps = 1e-8;

ld p[N];

int main() {
  cout.setf(ios::fixed);
  cout.precision(10);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cerr << t << endl;
    int n, spam;
    cin >> n >> spam;
    ld u;
    cin >> u;
    cerr << n << ' ' << u << endl;
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
      cerr << p[i] << ' ';
    }
    cerr << endl;
    while (u > eps) {
      cerr << u << endl;
      vector<int> idxs;
      ld mn = 2, mn2 = 2;
      for (int i = 0; i < n; ++i) {
        if (p[i] < mn - eps) {
          mn2 = mn;
          mn = p[i];
          idxs.clear();
        }
        if (abs(p[i] - mn) < eps) {
          idxs.push_back(i);
        } else if (p[i] < mn2) mn2 = p[i];
      }
      if (mn2 > 1.5) {
        for (int i = 0; i < n; ++i) p[i] += u / ld(n);
        u = 0;
      } else {
        int k = idxs.size();
        ld inc = min(mn2 - mn, u / ld(k));
        u -= ld(k) * inc;
        for (int i : idxs) p[i] += inc;
      }
    }
    ld prod = 1;
    for (int i = 0; i < n; ++i) prod *= p[i];
    cout << "Case #" << t << ": " << prod << endl;
  }
}

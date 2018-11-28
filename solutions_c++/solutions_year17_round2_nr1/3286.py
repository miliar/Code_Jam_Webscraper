#include <bits/stdc++.h>

using namespace std;

typedef pair<double, double> ii;
const int N = 1e3 + 10;
const double EPS = 1e-9;
ii ks[N];
int d, n; 

bool pass(const double s, const double ts) { 
  double cpt;
  for (int i = 0; i < n; i++) {
    if (ks[i].second < s) {
      cpt = (ks[i].first / (s - ks[i].second));
      if (cpt < ts) return false;
    }
  }
  return true;
}

int main() {
  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      cin >> ks[i].first >> ks[i].second;
    }
    sort(ks, ks + n, greater<ii>());
    double high = 1e15, low = 0, m;
    int iter = 0;
    //while (high - low > EPS) {
    while (++iter < 500) {
      m = (low + high) / 2;
      if (pass(m, d/m)) low = m; 
      else high = m;
    }
    printf("%.10lf\n", m);
  }
  return 0;
}

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

vector<pair<long long, double> > h;

bool good(double v, double d) {
  for(int i = 0; i < h.size(); ++i) {
    if (v <= h[i].second) continue;
    double q = (double)h[i].first / (1.0 - (h[i].second / v));
    if (q < d) return false;
  }
  return true;
}

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    double d;
    int n;
    cin >> d >> n;

    h.clear();
    h.resize(n);
    for(int i = 0; i < n; ++i) {
      cin >> h[i].first >> h[i].second;
    }

    double ub = 1e100;
    double lb = 0;

    for(int i = 0; i < 10000; ++i) {
      double md = lb + (ub - lb) / 2.0;
      if (good(md, d)) {
        lb = md;
      } else {
        ub = md;
      }
    }

    double ans = lb + (ub - lb) / 2.0;
    printf("Case #%d: %.8f\n", t + 1, ans);
  }
}

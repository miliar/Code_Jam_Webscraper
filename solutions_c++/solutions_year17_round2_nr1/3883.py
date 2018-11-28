/*
  Created on 22-04-2017
  Author: bshankar (Bhavani Shankar)
  Email: ebs@openmailbox.org
*/

#include <bits/stdc++.h>

using namespace std;

#define NL "\n"

#define FR(r, ri, rf) for (auto r = ri; r < rf; ++r)
#define FRR(r, ri, rf) for (auto r = ri; r >= rf; --r)
#define FFR(r, ri, rf, c, ci, cf) FR(r, ri, rf) FR(c, ci, cf)
#define Rn(r, rf) FR(r, 0, rf)
#define RnR(r, rf) FRR(r, 0, rf)
#define RRn(r, rf, c, cf) FR(r, 0, rf) FR(c, 0, cf)

#define B begin()
#define E end()
#define SIZE(vec) int(vec.size())
#define FND(vec, start, end, val) find(start, end, val) != vec.E

typedef pair<double,double> dd;
vector<pair<double, double> > hi;


bool canCatchUp(int i) {
}


void solveCase(int t) {

  double D, N;
  cin >> D >> N;
  hi.clear();

  Rn(i, N) {
    double k, s;
    cin >> k >> s;
    hi.push_back({k, s});
  }

  sort(hi.B, hi.E, [&](dd x, dd y) {
      return x.first < y.first;
    });

  double min_v = 100000000, min_k = 0;
  double min_v2 = 100000000, min_k2 = 0, max_t = 0;
  for (int i = 0; i < hi.size(); ++i) {
    if (hi[i].second < min_v) {
      min_v = hi[i].second;
      min_k = hi[i].first;
    }

    double t = (D - hi[i].first)/hi[i].second;
    if (t > max_t) {
      min_v2 = hi[i].second;
      min_k2 = hi[i].first;
      max_t = t;
    }
  }


  double t_max = max((D - min_k)/min_v, max_t);
  printf("Case #%d: %.14f\n", t, D/t_max);
}


int main() {
  int TC;
  cin >> TC;
  Rn(t, TC)
    solveCase(t + 1);
}

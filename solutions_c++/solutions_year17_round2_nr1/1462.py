#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>

using namespace std;

double doit() {
  
  int D, N;
  cin >> D >> N;
  vector<pair<double, double> > v(N);
  for (int i = 0; i < N; ++i) {
    cin >> v[i].first >> v[i].second;
  }
  double timeEnd = 0;
  
  for (auto e : v) {
    double dist = D - e.first;
    double tt = dist/e.second;
    timeEnd = max(timeEnd, tt);
  }

  return D/timeEnd;
}

int main() {

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: %.9f\n", t, doit());
  }

}

#include <bits/stdc++.h>
#define MAX 2000

using namespace std;
typedef pair<double,double> ii;

double tt[MAX];

int main() {
  int t;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; ++cas) {
    vector<ii> horse;
    double d, k, s;
    int n;
    scanf("%lf %d", &d, &n);
    for (int i = 0; i < n; ++i) {
      scanf("%lf %lf", &k, &s);
      horse.push_back(make_pair(k, s));
    }

    sort(horse.begin(), horse.end());
    tt[n - 1] = (d - horse[n - 1].first) / horse[n - 1].second;
    if (n > 1)
      for (int i = n - 2; i >= 0; --i)
        tt[i] = max(tt[i + 1], (d - horse[i].first) / horse[i].second);

    printf("Case #%d: %.6lf\n", cas, d / tt[0]); 
  }

  return 0;
}

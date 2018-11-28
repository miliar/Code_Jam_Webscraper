#include <bits/stdc++.h> 

using namespace std;

const int N = 1010;

int t, cs, n;
long double d, tym[N];
pair <long double, long double> p[N];

int main (int argc, char const *argv[]) {
  scanf("%d", &t); while (t--) {
    scanf("%Lf %d", &d, &n);
    for (int i = 1; i <= n; ++i) {
      scanf("%Lf %Lf", &p[i].first, &p[i].second);
    }
    sort(p + 1, p + n + 1);
    tym[n + 1] = 0.0;
    long double maxi = -1e18;
    for (int i = n; i; --i) {
      tym[i] = (d - p[i].first)/p[i].second;
      tym[i] = max(tym[i], tym[i + 1]);
      maxi = max(maxi, tym[i]);
    } 
    long double v = d/maxi;
    printf("Case #%d: %0.12f\n", ++cs, (double) v);
  }
  return 0;
}


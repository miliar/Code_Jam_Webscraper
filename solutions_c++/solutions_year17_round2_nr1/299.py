#include <bits/stdc++.h>

#define MOD 1000000007
#define EPS 10e-8

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

int k[1005], s[1005];

int main()
{
  int t, T;
  scanf("%d", &T);

  for (t = 1; t <= T; t++)
  {
    int d, n;
    scanf("%d %d", &d, &n);
    for (int i = 0; i < n; i++)
      scanf("%d %d", &k[i], &s[i]);

    double tmp = -1;
    for (int i = 0; i < n; i++)
      tmp = max(tmp, (1.0 * d - k[i]) / s[i]);

    double lo = 0, hi = 10e17 + 10;
    for (int iter = 0; iter < 25000; iter++)
    {
      double med = (lo + hi) / 2;
      double mt = d / med;

      if (mt >= tmp)
        lo = med;
      else
        hi = med;
    }

    double ans = (lo + hi) / 2;
    printf("Case #%d: %0.8lf\n", t, ans);
  }
  
  return 0;
}

/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sun 30 Apr 2017 17:41:18
 *
 */
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <cctype>
#include <cmath>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>
#define sqr(x) ((x)*(x))
#ifdef _WIN32
#define lld "%I64d"
#else
#define lld "%lld"
#endif

const int INF = 0x3f3f3f3f;
const long long INFLL = 0x3f3f3f3f3f3f3f3fll;
const double PI = acos(-1.0);
const double eps = 1e-10;

typedef long long LL;
typedef int itn;

const int maxn = 1000;
const int maxm = 0;

double p[maxn];

double calc(double m, int n, double u)
{
  for (int i = 0; i < n; i++)
  {
    if (p[i] < m)
    {
      u -= (m - p[i]);
    }
  }

  return u;
}

void apply(double m, int n)
{
  for (int i = 0; i < n; i++)
  {
    if (p[i] < m)
    {
      p[i] = m;
    }
  }
}

int main()
{
#ifdef FCBRUCE
  //freopen("/Users/fcbruce/code/t", "r", stdin);
#endif // FCBRUCE

  int T_T, __ = 0;
  scanf("%d", &T_T);

  while (T_T--)
  {
    int n, k;
    scanf("%d%d", &n, &k);
    double u;
    scanf("%lf", &u);
    for (int i = 0; i < n; i++) scanf("%lf", p + i);
    
    double l = 0, r = 1;
    while (fabs(r - l) > 1e-10)
    {
      double mid = (r + l) / 2.0;
      // double mid2 = (l + mid) / 2.0;
      
      if (calc(mid, n, u) < 0) 
      {
        r = mid;
      }
      else
      {
        l = mid;
      }
    }

    //printf("%lf\n", l);
    apply(l, n);
    double P = 1;
    for (int i = 0; i < n; i++)
    {
      P *= p[i];
    }
    printf("Case #%d: %.9f\n", ++__, P);
  }




  return 0;
}

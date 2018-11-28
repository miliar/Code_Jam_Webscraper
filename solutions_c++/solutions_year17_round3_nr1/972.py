/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sun 30 Apr 2017 17:04:46
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

const int maxn = 1007;
const int maxm = 0;

struct Cake
{
  long long r, h;
  void read()
  {
    scanf(lld lld, &r, &h);
  }
  bool operator < (const Cake &rhs) const
  {
    return r * h > rhs.r * rhs.h;
  }
  double r2()
  {
    return sqr(r) * PI;
  }
  double hr()
  {
    return 2 * r * h * PI;
  }
}cake[maxn];

int n, k;
double select(int id, int k)
{
  double area = cake[id].r2() + cake[id].hr();
  k--;
  for (int i = 0; i < n && k > 0; i++) if (id != i)
  {
    if (cake[i].r <= cake[id].r)
    {
      area += cake[i].hr();
      k--;
    }
  }
  if (k == 0) return area;
  else return 0;
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
    scanf("%d%d", &n, &k);

    for (int i = 0; i < n; i++) cake[i].read();

    std::sort(cake, cake + n);

    double max = 0;
    for (int i = 0; i < n; i++)
      max = std::max(max, select(i, k));

    printf("Case #%d: %.8f\n", ++__, max);
  }




  return 0;
}

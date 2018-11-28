/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sun 23 Apr 2017 01:35:41
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

const int maxn = 107;
const int maxm = 0;

int n;

int e[maxn], s[maxn];
int g[maxn][maxn];

double vis[maxn];

struct node
{
  int pos;
  double time;
  int e, s;
  bool operator < (const node &rhs) const
  {
    return time > rhs.time;
  }
};

double go(int s, int t)
{
  std::priority_queue<node> q;
  for (int i = s; i <= t; i++) vis[i] = 1e20;
  q.push({s, 0.0, e[s], ::s[s]});

  while (!q.empty())
  {
    node x = q.top();
    q.pop();
    //printf("%d %f\n", x.pos, x.time);
    if (x.pos == t) return x.time;

    for (int i = 0; i < n; i++) if (g[x.pos][i] > 0)
    {
      int d = g[x.pos][i];
      if (x.e >= d)
      {
        node xx = x;
        xx.pos = i;
        xx.e -= d;
        xx.time += ((double) d) / xx.s;
        q.push(xx);
      }

      node xx = x;
      xx.pos = i;
      xx.e = e[x.pos];
      xx.s = ::s[x.pos];
      if (xx.e >= d)
      {
        xx.e -= d;
        xx.time += ((double) d) / xx.s;
        q.push(xx);
      }
    }
  }
}

int main()
{
#ifdef FCBRUCE
  //freopen("/home/fcbruce/code/t", "r", stdin);
#endif // FCBRUCE

  int T_T, __ = 0;
  scanf("%d", &T_T);

  while (T_T--)
  {
    int q;
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; i++)
    {
      scanf("%d%d", e + i, s + i);
    }
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) scanf("%d", &g[i][j]);
    int u, v;
    scanf("%d%d", &u, &v);
    u--;
    v--;
    printf("Case #%d: %.7f\n", ++__, go(u, v));
  }




  return 0;
}

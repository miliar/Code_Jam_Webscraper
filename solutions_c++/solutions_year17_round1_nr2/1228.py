/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sat 15 Apr 2017 10:22:27
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

const int maxn = 32768;
const int maxm = 0;

struct pack
{
  int l, r;
  int id;
  bool operator < (const pack &rhs) const
  {
    return l == rhs.l ? r < rhs.r : l < rhs.l;
  }
}ps[maxn];

struct event
{
  int v, id, time, pos;
  bool operator < (const event &rhs) const
  {
    return time == rhs.time ? v > rhs.v : time < rhs.time;
  }
}es[maxn];

bool vis[maxn];
int cnt[64];
int need[64];

int n, p;

std::priority_queue<std::pair<int, int>> qs[64];

inline bool check()
{
  for (int i = 0; i < n; i++)
    if (cnt[i] == 0) return false;
  return true;
}

void inline drop(int i)
{
  while (!qs[i].empty())
  {
    auto e = qs[i].top();
    qs[i].pop();
    if (vis[e.second]) continue;
    vis[e.second] = true;
    cnt[i]--;
    break;
  }
}


inline void drop()
{
  for (int i = 0; i < n ;i++)
  {
    drop(i);
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
    scanf("%d %d", &n, &p);
    for (int i = 0; i < n; i++) scanf("%d", need + i);

    int m = 0;
    int nes = 0;
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < p; j++)
      {
        int g = 0;
        scanf("%d", &g);
        int min = ceil(g / (1.1 * need[i]));
        int max = floor(g / (0.9 * need[i]));
        //printf("%d %d %d\n", g, min, max);
        if (min > max) continue;
        pack p = {min, max, i};
        ps[m++] = p;
        es[nes++] = {1, i, min, m - 1};
        es[nes++] = {-1, i, max, m - 1};
      }
    }

    std::sort(es, es + nes);

    for (int i = 0; i < n; i++) while (!qs[i].empty()) qs[i].pop();

    memset(vis, 0, sizeof vis);
    memset(cnt, 0, sizeof cnt);
    int res = 0;
    for (int i = 0; i < nes; i++) 
    {
      event &e = es[i];
      if (vis[e.pos]) continue;
      //printf("%d %d\n", e.id, e.v);

      if (e.v > 0)
      {
        pack &p = ps[e.pos];
        qs[e.id].push({p.r, e.pos});
        cnt[e.id]++;
      }
      else
      {
        vis[e.pos] = true;
        cnt[e.id]--;
      }

      if (check())
      {
        res++;
        drop();
      }
    }

    printf("Case #%d: %d\n", ++__, res);

    

    
  }




  return 0;
}

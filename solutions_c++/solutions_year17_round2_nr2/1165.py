/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sun 23 Apr 2017 00:22:41
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

const int maxn = 0;
const int maxm = 0;

int col[6];
char cs[8] = "ROYGBV";
int n;

int cnt_app;

bool only_one()
{
  if (cnt_app == 1)
  {
    if (n == 1)
    {
      for (int i = 0; i < 6; i++) if (col[i]) putchar(cs[i]);
      puts("");
    }
    else
    {
      puts("IMPOSSIBLE");
    }
    return true;
  }
  return false;
}

bool only_bo()
{
  if (cnt_app == 2 && col[1] > 0 && col[4] > 0)
  {
    if (col[4] == col[1])
    {
      for (int i = 0; i < col[1]; i++) { putchar('B'); putchar('O'); }
      puts("");
    }
    else
      puts("IMPOSSIBLE");
    return true;
  }
  return false;
}

bool only_rg()
{
  if (cnt_app == 2 && col[0] > 0 && col[3] > 0)
  {
    if (col[0] == col[3])
    {
      for (int i = 0; i < col[0]; i++) { putchar('R'); putchar('G'); }
      puts("");
    }
    else
      puts("IMPOSSIBLE");
    return true;
  }
  return false;
}

bool only_yv()
{
  if (cnt_app == 2 && col[2] > 0 && col[5] > 0)
  {
    if (col[2] == col[5])
    {
      for (int i = 0; i < col[2]; i++) { putchar('Y'); putchar('V'); }
      puts("");
    }
    else
      puts("IMPOSSIBLE");
    return true;
  }
  return false;
}

void prt(int b, int r, int y, int o, int g, int v, char B, char R, char Y, char O, char G, char V)
{
  for (int i = 0; i < o; i++) { putchar(B); putchar(O); } 
  if (o && b) { putchar(B); b--; }
  for (int i = 0; i < g; i++) { putchar(R); putchar(G); } 
  if (g && r) { putchar(R); r--; }
  for (int i = 0; i < v; i++) { putchar(Y); putchar(V); } 
  if (v && y) { putchar(Y); y--; }

  while (b || r || y)
  {
    if (b >= r && b >= y)
    {
      putchar(B);
      b--;
      if (r || y)
      {
        if (r >= y) { putchar(R); r--; }
        else { putchar(Y); y--; }
      }
    }
    else if (r >= b && r >= y)
    {
      putchar(R);
      r--;
      if (b || y)
      {
        if (b >= y) { putchar(B); b--; }
        else { putchar(Y); y--; }
      }
    }
    else
    {
      putchar(Y);
      y--;
      if (r || b)
      {
        if (r > b) { putchar(R); r--; }
        else { putchar(B); b--; }
      }
    }
  }

  puts("");
}

bool ok()
{
  int r = col[0];
  int o = col[1];
  int y = col[2];
  int g = col[3];
  int b = col[4];
  int v = col[5];

  b -= o;
  r -= g;
  y -= v;

  if (o > 0 && b < 1 ||  g > 0 && r < 1 || v > 0 &&  y < 1) return false;

  int total = b + r + y;
  b <<= 1;
  r <<= 1;
  y <<= 1;
  if (b > total || r > total || y > total) return false;
  b >>= 1;
  r >>= 1;
  y >>= 1;

  if (b >= r && b >= y)
  {
    if (r >= y) 
      prt(b, r, y, o, g, v, 'B', 'R', 'Y', 'O', 'G', 'V');
    else
      prt(b, y, r, o, v, g, 'B', 'Y', 'R', 'O', 'V', 'G');
  } 
  else if (r >= b && r >= y)
  {
    if (b >= y)
      prt(r, b, y, g, o, v, 'R', 'B', 'Y', 'G', 'O', 'V');
    else
      prt(r, y, b, g, v, o, 'R', 'Y', 'B', 'G', 'V', 'O');
  }
  else
  {
    if (b >= r)
      prt(y, b, r, v, o, g, 'Y', 'B', 'R', 'V', 'O', 'G');
    else
      prt(y, r, b, v, g, o, 'Y', 'R', 'B', 'V', 'G', 'O');
  }

  return true;
}

void solve()
{
  cnt_app = 0;
  for (int i = 0; i < 6; i++) if (col[i] > 0) cnt_app++;
  if (only_one()) return ;

  if (only_bo()) return ;
  if (only_rg()) return ;
  if (only_yv()) return ;

  if (ok()) return ;

  puts("IMPOSSIBLE");

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
    scanf("%d", &n);
    for (int i = 0; i < 6; i++) scanf("%d", col + i);
    printf("Case #%d: ", ++__);
    solve();
  }




  return 0;
}

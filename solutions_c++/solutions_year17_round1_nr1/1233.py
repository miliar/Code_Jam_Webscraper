/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sat 15 Apr 2017 09:08:06
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

const int maxn = 32;
const int maxm = 0;

char g[maxn][maxn];
int n, m;
bool vis[256];
std::queue<char> q;

void print_all(int n, char c)
{
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (g[i][j] == '?') g[i][j] = c;
}

void print_r(int n, int m, char c)
{
  for (int i = 0; i <= n; i++)
    for (int j = 0; j <= m; j++)
      if (g[i][j] == '?') g[i][j] = c;
}

void prt()
{
  puts("----");
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
      putchar(g[i][j]);
    puts("");
  }
  puts("----");
}

void prt_r(int x, int y)
{
  char c = g[x][y];
  for (int i = y + 1; i < m && g[x][i] == '?'; i++) g[x][i] = c;
  for (int i = y - 1; i > -1 && g[x][i] == '?'; i--) g[x][i] = c;
}

void prt_c(int x, int y)
{
  char c = g[x][y];
  for (int i = x + 1; i < n && g[i][y] == '?'; i++) g[i][y] = c;
  for (int i = x - 1; i > -1 && g[i][y] == '?'; i--) g[i][y] = c;
}

int main()
{
#ifdef FCBRUCE
#endif // FCBRUCE

  int T_T, __ = 0;
  scanf("%d", &T_T);

  while (T_T--)
  {
    scanf("%d%d", &n, &m);
    memset(g, 0, sizeof g);
    for (int i = 0; i < n; i++) scanf("%s", g[i]);

    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        prt_r(i, j);

    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        prt_c(i, j);

    if (g[0][0] == '?')
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) g[i][j] = 'A';


    printf("Case #%d: \n", ++__);
    for (int i = 0; i < n; i++) 
    {
      for (int j = 0; j < m; j++)
        putchar(g[i][j]);
      puts("");
    }

  }






  return 0;
}

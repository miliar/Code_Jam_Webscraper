/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sun 30 Apr 2017 17:57:04
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

const int maxn = 4096;
const int maxm = 0;

int care[maxn];

bool start(int i)
{
  return care[i] == 0 && (i && care[i - 1] != 0);
}

bool end(int i, int tag)
{
  return care[i] == 0 && (care[i + 1] == tag);
}

bool found_min(int &t, int tag)
{
  int len = INF;
  int l  = 0 , r = INF;
  int cl, cr;
  int sl;
  for (int i = 0; i < 2880; i++)
  {
    if (start(i)) {
      cl = i;
      sl = i == 0 ? tag : care[i - 1];
    }
    if (end(i, tag) && sl == tag) 
    {
      cr = i + 1;
      if (cr - cl < len)
      {
        len = cr - cl;
        l = cl;
        r = cr;
      }

      if (i >= 1440) break;
    }
  }

     printf("%d %d\n", t, len);
  if (len == INF || t < len) return false;
    // printf("[%d, %d)\n", l, r);
  for (int i = l; i < r; i++) care[i] = tag;
  t -= len;
  return true;
}

int main()
{
#ifdef FCBRUCE
  // freopen("/Users/fcbruce/code/t", "r", stdin);
#endif // FCBRUCE

  int T_T, __ = 0;
  scanf("%d", &T_T);

  while (T_T--)
  {
    memset(care, 0, sizeof care);
    int n, m;
    scanf("%d%d", &n, &m);
    int tn = 720, tm = 720;
    for (int i = 0; i < n; i++)
    {
      int l, r;
      scanf("%d%d", &l, &r);
      tn -= r - l;
      for (int j = l; j < r; j++) care[j + 1440] = care[j] = -1;
    }
    for (int i = 0; i < m; i++)
    {
      int l, r;
      scanf("%d%d", &l, &r);
      tm -= r - l;
      for (int j = l; j < r; j++) care[j + 1440] = care[j] = 1;
    }

    while (found_min(tn, -1)) ;
    while (found_min(tm, 1)) ;

    int first = 0;
    int first_i = 0;
    for (int i = first_i; i < first_i + 1440; i++) if (care[i]) 
    {
      first = care[i];
      first_i = i;
      break;
    }

    int cnt = 0;
    for (int i = first_i; i < first_i + 1440; i++)
      if (i && care[i] && care[i] == -care[i - 1]) cnt ++;

    // printf("%d\n", cnt);
    int last = 0;
    for (int i = first_i; i < first_i + 1440; i++)
    {
      if (care[i] == 0)
      {
      }
      else
      {
        if (care[i - 1] == 0)
        {
          if (care[i] == last) cnt += 2;
          else if (last) cnt++;
          // printf(" %d  %d\n", i - first_i, cnt);
        }
        last = care[i];
      }
    }

    /*
    printf("%d\n", cnt);
    for (int i = first_i; i < first_i + 1440; i++) printf("%d", care[i]);
    printf("\n");
    */
    if (care[first_i + 1439] == 0)
    {
      if (first != last) cnt++;
      else cnt += 2;
    }

    if (care[0] && care[1439] && care[0] != care[1439]) cnt++;
    

    printf("Case #%d: %d\n", ++__, cnt);
  }




  return 0;
}

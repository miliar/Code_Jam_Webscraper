#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug
//#define TRACE(x)

using namespace std;

typedef long long llint;

const int MAXN = 1010;

int a[MAXN][MAXN];

int n, c, m;

bool check(int x, int& prom) {
  prom = 0;

  int fr = 0;
  REP(j, n) {
    int sum_col = 0;
    REP(i, c) sum_col += a[i][j];

    if (sum_col <= x) {
      fr += x - sum_col;
    } else {
      prom += sum_col - x;
      fr -= sum_col - x;
      if (fr < 0) return false;
    }
  }
  
  return true;
}

void solve(int tc) {
  memset(a, 0, sizeof(a));
  scanf("%d %d %d",&n,&c,&m);
  REP(i, m) {
    int p, b;
    scanf("%d %d",&p,&b);
    --p;
    --b;
    a[b][p]++;
  }

  int min_rides = 0;
  REP(i, c) {
    int sum_row = 0;
    REP(j, n) sum_row += a[i][j];
    min_rides = max(min_rides, sum_row);
  }

  int lo = min_rides, hi = m, res1 = -1, res2 = -1;

  while (lo <= hi) {
    int mid = (lo + hi) / 2;
    int prom = -1;
      
    if (check(mid, prom)) {
      res1 = mid;
      res2 = prom;
      hi = mid - 1;
    } else
      lo = mid + 1;
  }

  printf("Case #%d: %d %d\n",tc,res1,res2);
}

int main(void) {
  int t;
  scanf("%d",&t);
  REP(it, t)
    solve(it+1);
  
  return 0;
}

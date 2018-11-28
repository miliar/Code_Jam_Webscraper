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

const int MAXN = 110;

int t, n, p, a[MAXN], cnt[MAXN];

int solve() {
  memset(cnt, 0, sizeof(cnt));
  
  scanf("%d %d",&n,&p);
  REP(i, n) {
    scanf("%d",&a[i]);
    ++cnt[a[i] % p];
  }

  int ret = 0;

  if (p == 2) {
    ret += cnt[0];
    ret += (cnt[1] + 1) / 2;
  } else if (p == 3) {
    int k = min(cnt[1], cnt[2]);
    ret += k;
    cnt[1] -= k;
    cnt[2] -= k;
    ret += (cnt[1] + 2) / 3;
    ret += (cnt[2] + 2) / 3;
    ret += cnt[0];
  } else {
    ret = -1;
  }
  return ret;
}

int main(void) {
  scanf("%d",&t);
  REP(it, t) {
    printf("Case #%d: %d\n",it+1,solve());
  }
  
  return 0;
}

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

bool inc(llint x) {
  llint prv = 10;
  while (x > 0) {
    if (x % 10 > prv) return false;
    prv = x % 10;
    x /= 10;
  }
  return true;
}

int main(void) {
  int t;
  scanf("%d",&t);
  REP(it, t) {
    llint y;
    scanf("%lld",&y);
    int k = 0;
    while (!inc(y)) {
      ++k;
      y = (y - 9) / 10;
    }
    printf("Case #%d: ",it+1);
    if (y > 0)
      printf("%lld",y);
    REP(i, k) printf("9");
    printf("\n");
  }
  return 0;
}

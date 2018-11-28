#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug
//#define TRACE(x)

using namespace std;
using llint = long long;
using pii = pair<llint, llint>;

map<llint, llint> p;

pii solve(llint n, llint k) {
  p.clear();
  p[n] = 1;

  while (k > 0) {
    auto it = p.end();
    --it;
    llint m = it->first;
    llint cnt = it->second;
    p.erase(it);

    if (cnt >= k) {
      return {m/2, (m-1)/2};
    } else {
      k -= cnt;
      p[m/2] += cnt;
      p[(m-1)/2] += cnt;
    }
  }

  return {0,0};
}

int main(void) {
  int t;
  scanf("%d",&t);
  REP(it, t) {
    llint n, k;
    scanf("%lld %lld",&n,&k);
    pii sol = solve(n,k);
    printf("Case #%d: %lld %lld\n",it+1,sol.first,sol.second);
  }
  return 0;
}

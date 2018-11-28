#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>

#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)

// #define TRACE(x)
// #define debug(...)

using namespace std;

typedef long long llint;

struct seg {
  int len, pos;
  bool operator < (const seg &b) const {
    if (len != b.len) return len > b.len;
    return pos < b.pos;
  }
};

void solve(void) {
  int n, k;
  scanf("%d%d", &n, &k);

  set<seg> s;
  s.insert({n, 0});

  int ls, rs;
  
  REP (i, k) {
    assert(!s.empty());
    seg best = *s.begin();
    s.erase(s.begin());

    ls = (best.len - 1) / 2;
    rs = best.len / 2;

    int pos = best.pos + ls;
    
    if (ls > 0)
      s.insert({ls, best.pos});
    if (rs > 0)
      s.insert({rs, pos+1});
  }

  printf("%d %d\n", max(ls, rs), min(ls, rs));
}

int main(void) {
  int t;
  scanf("%d", &t);

  REP (i, t) {
    printf("Case #%d: ", i+1);
    solve();
  }
  
  return 0;
}

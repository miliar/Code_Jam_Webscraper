#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <map>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

using namespace std;

pair<llint, llint> breakit(llint n) {
  return make_pair((n-1)/2, n/2); // min, max
}

map<llint, llint> mem;

llint go(llint n, llint stop) {
  if (n < stop) return 0;
  if (mem.find(n) != mem.end()) return mem[n];

  llint ans = 0;
  auto p = breakit(n);
  ans = 1 + go(p.first, stop) + go(p.second, stop);

  mem[n] = ans;
  return ans;
}

llint f(llint n, llint stop) {
  mem.clear();
  return go(n, stop);
}

int main(void) {
  int ntc; cin >> ntc;
  REP(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    llint n, k; cin >> n >> k;
    llint lo = 1, hi = n;
    
    while (lo < hi) {
      llint mid = (lo + hi + 1) / 2;
      if (f(n, mid) >= k)
        lo = mid;
      else
        hi = mid - 1;
    }
    
    //    TRACE(lo _ hi);
    auto p = breakit(lo);
    cout << p.second << " " << p.first << endl;
  }
  return 0;
}

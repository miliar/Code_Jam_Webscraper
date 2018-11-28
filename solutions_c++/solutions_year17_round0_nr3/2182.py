#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;
using LL = long long;
using pll = pair<LL, LL>;

pll dv(LL x) {
  assert(x >= 1);
  --x;
  LL a = x / 2;
  LL b = x - a;
  if (a < b)
    swap(a, b);
  return pll(a, b);
}

pll solve(LL n, LL k) {
  map<LL, LL> c;
  c[n]++;
  pll ls;
  while (k > 0) {
    auto it = c.end();
    --it;

    LL cnt = it->second;
    pll t = dv(it->first);
    ls = t;
    k -= cnt;
    c.erase(it);
    c[t.first] += cnt;
    c[t.second] += cnt;
  }

  return ls;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    LL n, k;
    cin >> n >> k;
    pll a = solve(n, k);
    cout << a.first << " " << a.second << endl;
  }
}

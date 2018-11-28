#include <bits/stdc++.h>

using namespace std;

#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

using ll = long long;
using ld = long double;

constexpr int nax = 1000 * 1000 + 105;
constexpr int infty = 1000 * 1000 * 1000 + 5;
constexpr int mod = 1000 * 1000 * 1000 + 7;

pair<ll, ll> przyp() {
  ll n, k;
  scanf("%lld%lld", &n, &k);
  map<ll, ll, greater<ll>> segments;
  segments[n] = 1;
  while (true) {
    auto it = segments.begin();
    n = it->first;
    const ll cnt = it->second;
    segments.erase(it);
    if (k <= cnt) {
      return make_pair(n / 2, (n - 1) / 2);
    }
    k -= cnt;
    segments[(n - 1) / 2] += cnt;
    segments[n / 2] += cnt;
  }
  assert(false);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    pair<ll, ll> result = przyp();
    printf("Case #%d: %lld %lld\n", i, result.first, result.second);
  }
  return 0;
}

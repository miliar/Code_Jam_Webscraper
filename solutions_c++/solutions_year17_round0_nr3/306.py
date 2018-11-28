#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

ll solve(ll n, ll k) {
  map<ll, ll, greater<ll>> freq{{n, 1LL}};
  for (;;) {
    assert(!freq.empty());
    ll sum = accumulate(ALL(freq), 0LL, [] (const ll sum, const pair<ll, ll> &it) {
      return sum + it.se;
    });
    debug {
      for (auto it : freq) {
        printf("(%lld, %lld) ", it.fi, it.se);
      }
      puts("");
    }
    if (k <= sum) {
      auto it = begin(freq);
      if (k <= it->se) {
        return it->fi;
      } else {
        assert(SZ(freq) == 2);
        return (++it)->fi;
      }
    }
    k -= sum;
    map<ll, ll, greater<ll>> nfreq;
    for (auto it : freq) {
      if ((it.fi - 1) / 2 > 0) {
        nfreq[(it.fi - 1) / 2] += it.se;
      }
      if (it.fi / 2 > 0) {
        nfreq[it.fi / 2] += it.se;
      }
    }
    freq = nfreq;
  }
  assert(false);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    ll n, k;
    cin >> n >> k;
    ll space = solve(n, k);
    static int caseNo = 1;
    printf("Case #%d: %lld %lld\n", caseNo++, space / 2, (space - 1) / 2);
  }
  return 0;
}


#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int main() {
  int T;
  cin >> T;
  REP (t, T) {
    ll N, K;
    cin >> N >> K;

    map<ll, ll> gaps;
    gaps[N] = 1;

    ll g = -1;
    while (K > 0) {
      g = gaps.rbegin()->first;
      ll f = gaps[g];
      gaps.erase(g);

      ll a = (g - 1) / 2;
      ll b = (a + a == g - 1) ? a : (a + 1);
      if (a != 0) gaps[a] = gaps[a] + f;
      if (b != 0) gaps[b] = gaps[b] + f;

      K -= f;
    }

    ll a = (g - 1) / 2;
    ll b = (a + a == g - 1) ? a : (a + 1);

    cout << "Case #" << t << ": " << max(a, b) << " " << min(a, b) << endl;
  }
  return 0;
}

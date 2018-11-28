#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PB push_back
#define MP make_pair

int main() {
  int ntest;
  cin >> ntest;

  FOR (test, 1, ntest) {
    cout << "Case #" << test << ": ";
    ll n, k;
    cin >> n >> k;

    map<ll, ll> cnt;

    cnt[n] = 1;

    ll res = -1;

    while (1) {
      auto it = cnt.end();
      it--;

      ll len = it->first;
      ll num = it->second;

      ll use = min(num, k);

      cnt[len / 2] += use;
      cnt[len - 1 - len / 2] += use;

      cnt[len] -= use;
      if (use == num) cnt.erase(cnt.find(len));

      k -= use;

      if (k == 0) {
        res = len;
        break;
      }
    }

    cout << (res / 2) << " " << (res - 1 - res / 2) << endl;
  }
}


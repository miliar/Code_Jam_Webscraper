#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define all(a) (a).begin(), (a).end()
#define fi first
#define pb(x) push_back(x)
#define se second
#define sz(a) ((int)(a.size()))

#define MAX 52

ll n, p;

typedef pair<ll, ll> pii;

ll r[MAX];
ll q[MAX][MAX];

vector<pii> v[MAX];
int nxt[MAX];

int match[MAX];

int main() {
  ios ::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> n >> p;
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> q[i][j];
      }
    }

    ll ans = 0;

    for (int i = 0; i < n; ++i) {
      v[i].clear();

      for (int j = 0; j < p; ++j) {
        ll b = (10 * q[i][j] + (11 * r[i] - 1)) / (11 * r[i]);
        ll e = (10 * q[i][j]) / (9 * r[i]);


        if (b <= e) {
          //printf("Generating (%lld, %lld) i = %d\n", b, e, i);
          v[i].pb(pii(b, e));
        }
      }
    }

    memset(nxt, 0, sizeof(nxt));

    for (int cxx = 0; cxx < p; cxx++) {
      ll mni = -1;

      for (int i = 0; i < n; ++i) {
        sort(all(v[i]), [](auto &a, auto &b) { return a.se < b.se; });

        if (0 == sz(v[i]))
          goto showresult;
        else {
          if (mni == -1 || v[i][0] < v[mni][0]) {
            mni = i;
          }
        }
      }

      bool usable = true;
      ll val = v[mni][nxt[mni]].se;
      for (int i = 0; i < n; ++i) {
        bool ok = false;
        for (int j = 0; j < sz(v[i]); ++j) {
          auto &p1 = v[i][j];
          if (p1.fi <= val && val <= p1.se) {
            match[i] = j;
            ok = true;
            break;
          }
        }

        if (!ok) {
          usable = false;
          break;
        }
      }

      if (usable) {
        ++ans;
        for (int i = 0; i < n; ++i) {
          swap(v[i][match[i]], v[i][sz(v[i]) - 1]);
          v[i].pop_back();
        }
      } else {
        swap(v[mni][0], v[mni][sz(v[mni]) - 1]);
        v[mni].pop_back();
      }
    }

  showresult:
    printf("Case #%d: %lld\n", cn, ans);
  }
  return 0;
}

#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define cl(x, v) memset((x), (v), sizeof(x))

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef long double ld;

typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const ld EPS = 1e-8l, PI = acos(-1.);
const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const int N = 1e2+5;

int t, n, p, r[N], q[N][N], pt[N];

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    printf("Case #%d: ", tt);
    cl(pt,0);

    scanf("%d%d", &n, &p);
    for (int i = 0; i < n; ++i) scanf("%d", &r[i]);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) scanf("%d", &q[i][j]);
      sort(q[i], q[i]+p);
    }

    int ans = 0;

    for (; pt[0] < p; pt[0]++) {
      ld x = floor(q[0][pt[0]]/(0.9*r[0])+EPS);
      ld y = ceil(q[0][pt[0]]/(1.1*r[0])-EPS);
      //db(pt[0]);
      //db(x _ y _ q[0][pt[0]]);
      if (x < y) continue;

      int ok = 1;
      for (int i = 1; i < n; ++i) {
        ld a, b;
        for (; pt[i] < p; pt[i]++) {
          a = floor(q[i][pt[i]]/(r[i]*0.9l)+EPS);
          b = ceil(q[i][pt[i]]/(r[i]*1.1l)-EPS);
          if (a < y or a < b) continue;
          break;
        }
        //db(a _ b _ q[i][pt[i]]);
        if (pt[i] >= p or b > x) { ok = 0; break; }
        pt[i]++;
      }

      ans += ok;
    }

    printf("%d\n", ans);
  }
  return 0;
}

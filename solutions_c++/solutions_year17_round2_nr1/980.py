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

const ld EPS = 1e-9, PI = acos(-1.);
const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const int N = 1e5+5;

int t, n, d, k[N];
double s[N];
double ans;

int main() {
  scanf("%d", &t);
  for(int tt = 1; tt<=t; tt++) {
    scanf("%d%d", &d, &n);
    for(int i=0; i<n; i++) scanf("%d%lf", &k[i], &s[i]);

    ans = max(((double) d*s[0]) / (d-k[0]), s[0]);
    for(int i=0; i<n; i++) {
      double x = max(((double) d*s[i]) / (d-k[i]), s[i]);
      ans = min(ans, x);
    }
    printf("Case #%d: %.7lf\n", tt, ans);
  }
  return 0;
}

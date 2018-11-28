// author: gary
#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int (i)=a;(i)<=(b);++i)
#define REP(i,n) FOR(i,0,(n-1))
#define ALL(x) (x).begin(), x.end()
#define SZ(x) ( (int) (x).size() )
#define dbg(x) cerr << #x << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
template<typename T> inline bool cmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool cmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long ll;
typedef pair<int, int> pii;

const int INF = 1e9;
const int N = 1e6 + 10;

ll n, k;

int used[N];

int go(int i, int d) {
  int x = i;
  while(!used[x])
    x += d;
  return abs(x - i);
}

bool cmp(pii a, pii b) {
  int fa = min(a.fi, a.se);
  int fb = min(b.fi, b.se);
  if(fa != fb)
    return fa < fb;
  fa = max(a.fi, a.se);
  fb = max(b.fi, b.se);
  if(fa != fb)
    return fa < fb;
  return false; // assuming a has lower index than b
}

int choose() {
  pii q = mp(0, 0);
  int j = 0;
  for(int i = 1; i <= n; i++) {
    pii p = mp(go(i, -1), go(i, +1));
    if(cmp(q, p)) {
      q = p;
      j = i;
    }
  }
  return j;
}

int main() {
  int tt;
  scanf("%d", &tt);
  for(int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    scanf("%lld%lld", &n, &k);
    memset(used, 0, sizeof used);
    used[0] = used[n+1] = 1;
    int x;
    pii p;
    for(int i = 1; i <= k; i++) {
      x = choose();
      p = mp(go(x, -1), go(x, +1));
      used[x] = 1;
    }
    printf("%d %d\n", max(p.fi, p.se) - 1, min(p.fi, p.se) - 1);
  }
  return 0;
}

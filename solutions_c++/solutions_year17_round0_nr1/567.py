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
const int N = 1e3+5;

int t, k, n;
char s[N];

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    scanf(" %s %d", s, &k);
    n = strlen(s);

    int ans = 0;
    int i = 0;
    while (s[i]) {
      while (s[i] == '+') i++;

      if (i == n) { break; }
      if (i > n-k) { ans = -1; break; }

      for (int j = i; j < i+k; ++j)
        s[j] = s[j]=='+'?'-':'+';
      ans++;
    }

    printf("Case #%d: ", tt);
    if (ans<0) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
    fflush(stdout);
  }
  return 0;
}

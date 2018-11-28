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

int t, n;
char s[20];

void solve(int p) {
  if (p == n-1) return;
  if (p < 0) return;

  if (s[p] > s[p+1]) {
    s[p] = s[p]-1;
    for (int i = p+1; i < n; ++i) s[i] = '9';
    solve(p-1);
  }

  solve(p+1);
}

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    scanf("%s", s);
    n = strlen(s);

    solve(0);
    int i = 0;
    while (s[i] == '0') i++;
    printf("Case #%d: %s\n", tt, s+i);
    fflush(stdout);
  }

  return 0;
}

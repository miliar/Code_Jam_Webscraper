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

int t, r, c;
char g[30][30];

int main() {
  scanf("%d", &t);
  for (int tt=1; tt <= t; ++tt) {
    printf("Case #%d:\n", tt);
    scanf("%d%d", &r, &c);

    for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) scanf(" %c", &g[i][j]);

    for (int i = 0; i < r; ++i) {
      char x = '?';
      for (int j = 0; j < c; ++j) {
        if (g[i][j] == '?') g[i][j] = x;
        else x = g[i][j];
      }
    }

    for (int i = 0; i < r; ++i) {
      char x = '?';
      for (int j = c-1; j >= 0; --j) {
        if (g[i][j] == '?') g[i][j] = x;
        else x = g[i][j];
      }
    }

    for (int j = 0; j < c; ++j) {
      char x = '?';
      for (int i = 0; i < r; ++i) {
        if (g[i][j] == '?') g[i][j] = x;
        else x = g[i][j];
      }
    }

    for (int j = 0; j < c; ++j) {
      char x = '?';
      for (int i = r-1; i >= 0; --i) {
        if (g[i][j] == '?') g[i][j] = x;
        else x = g[i][j];
      }
    }

    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) printf("%c", g[i][j]);
      printf("\n");
    }
  }

  return 0;
}

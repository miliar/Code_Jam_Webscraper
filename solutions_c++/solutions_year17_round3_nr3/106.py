#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()

#ifdef LOCAL
#define eprint(x) cerr << #x << " = " << x << endl
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprint(x)
#define eprintf(...)
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const int N = 50;
const int K = 200;

ld p[N];

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int n, k;
    ld u;
    cin >> n >> k >> u;
    for (int i = 0; i < n; i++)
      cin >> p[i];
    ld l = 0, r = 1;
    for (int i = 0; i < K; i++) {
      ld m = (l + r) / 2;
      ld sum = 0;
      for (int j = 0; j < n; j++)
        if (p[j] < m)
          sum += m - p[j];
      if (sum <= u)
        l = m;
      else
        r = m;
    }
    ld ans = 1;
    for (int i = 0; i < n; i++)
      ans *= (p[i] < l ? l : p[i]);
    printf("%.10f\n", (double) ans);
  }
#ifdef LOCAL
  eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  return 0;
}
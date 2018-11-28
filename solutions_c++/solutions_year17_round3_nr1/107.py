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

const ld PI = 3.141592653589793238462643;
const int N = 1000;

ld r[N], h[N];

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
    cin >> n >> k;
    vector< pair<ld, ld> > v;
    for (int i = 0; i < n; i++) {
      cin >> r[i] >> h[i];
      v.pb(mp(r[i], h[i]));
    }
    sort(all(v));
    multiset<ld> st;
    ld ans = 0, sum = 0;
    for (int i = 0; i < k - 1; i++) {
      ld val = v[i].ft * v[i].sd;
      sum += val;
      st.insert(val);
    }
    for (int i = k - 1; i < n; i++) {
      ld val = v[i].ft * v[i].sd;
      ans = max(PI * (v[i].ft * v[i].ft + 2 * (sum + val)), ans);
      ld mn = *st.begin();
      if (val > mn) {
        st.erase(st.begin());
        st.insert(val);
        sum += val - mn;
      }
    }
    printf("%.10f\n", (double) ans);
  }
#ifdef LOCAL
  eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  return 0;
}
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef long double ld;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;
//typedef long long int;

int d[1000005];

int solve(const vi & c) {
  int p = c.size();
  int M = 1;
  for (int i = 1; i < c.size(); ++i) M *= c[i] + 1;
  memset(d, 0, sizeof(d));
  for (int mask = 0; mask < M; ++mask) {
    vi x(p-1);
    int m = mask;
    int rem = 0;
    for (int i = 1; i < p; ++i) {
      x[i-1] = m % (c[i] + 1);
      rem += i * x[i-1];
      m /= c[i] + 1;
    }
    rem = (p - rem%p) % p;
//    for (int i = 0; i < p-1; ++i) cerr << x[i] << ' '; cerr << d[mask] << ' ' << rem << endl;
    for (int i = 1; i < p; ++i) if (x[i-1] < c[i]) {
      ++x[i-1];
      int nmask = 0;
      for (int j = p-1; j >= 1; --j) {
        nmask = nmask * (c[j] + 1) + x[j-1];
      }
      assert(nmask < M && nmask > mask);
      d[nmask] = max(d[nmask], d[mask] + (rem == 0 ? 1 : 0));
      --x[i-1];
    }
  }
//  cerr << c[0] << ' ' << d[M-1] << endl;
  return c[0] + d[M-1];
}

int solve2(const vi & c) {
  int p = c.size();
  if (p == 2) {
    return c[0] + (c[1] + 1) / 2;
  }
  if (p == 3) {
    int d = min(c[1], c[2]);
    return c[0] + d + (max(c[1], c[2]) - d + 2) / 3;
  }
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n, p;
    cin >> n >> p;
//    assert(p <= 3 && p >= 2);
    vi a(n), c(p);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
      c[a[i]%p]++;
    }
//    for (int i = 0; i < p; ++i) cerr << c[i] << ' '; cerr << endl;
//    cerr << solve(c) << ' ' << solve2(c) << endl; 
    int res = solve(c);
    if (p <= 3) assert(res == solve2(c));
    assert(res <= n);
    cout << res << endl;
  }
  return 0;
}

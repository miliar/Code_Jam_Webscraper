#include <bits/stdc++.h>
using namespace std;

int i, n, d, k[1005], s[1005];
long double st, dr, pivot, rs;

bool check(long double vit) {
  if(vit < 1e-9) return 0;
  long double t = d / vit;
  for(int i = 1; i <= n; ++i)
    if(d > (long double)k[i] + t * s[i]) return 0;

  return 1;
}

int main() {
  ifstream cin("test1.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  int test, tests;
  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> d >> n;
    for(i = 1; i <= n; ++i) cin >> k[i] >> s[i];

    st = 0; dr = 1e18; rs = 0;
    for(int iter = 0; iter <= 169; ++iter) {
      pivot = (st + dr) / 2;

      if(check(pivot)) rs = pivot, st = pivot;
      else dr = pivot;
    }

    cout << setprecision(6) << fixed << rs << '\n';
  }

  return 0;
}
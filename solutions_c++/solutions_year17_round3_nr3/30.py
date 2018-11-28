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

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n,k;
    cin >> n >> k;
    double u;
    scanf("%lf", &u);
    vd p(n);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &p[i]);
    }
    sort(p.begin(), p.end());
    p.push_back(1);
    for (int i = 0; i < n && u >= 0; ++i) {
      double d = p[i+1] - p[i];
      double add = min(d, u / (i + 1));
      u -= add * (i + 1);
      for (int j = 0; j <= i; ++j) p[j] += add;
    }
    double res = 1;
    for (int i = 0; i < n; ++i) res *= p[i];
    printf("%.10lf\n", res);
  }
  return 0;
}

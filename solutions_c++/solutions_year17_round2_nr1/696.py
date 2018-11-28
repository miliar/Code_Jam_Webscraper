#include<bits/stdc++.h>
using namespace std;
const double EPS = 1e-6;
double d;
int n;

double k[1005], s[1005];

bool check() {
  for ( int i = 0 ; i < n ; i++) {
    if ( fabs(k[i]-d) > EPS ) return true;
  }
  return false;
}

void solve() {
  double mx = 0;
  int u;
  for ( int i = 0 ; i < n ; i++ ) {
    if ( (d-k[i])/s[i] > mx ) {
      mx = (d-k[i])/s[i];
      u = i;
    }
  }

  printf("%.8lf\n", d/mx);

}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T, kase = 1;
  cin >> T;
  while (T--) {
    cin >> d >> n;
    for ( int i = 0 ; i < n ; i++ ) cin >> k[i] >> s[i];
      printf("Case #%d: ", kase++);
    solve();
  }

}

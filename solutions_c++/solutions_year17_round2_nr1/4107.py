#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;

int D, N, ans;
pair<double, double> H[1001];

void solve() {
  cin >> D >> N;
  for (int i = 0; i < N; i++) {
    cin >> H[i].first >> H[i].second;
  }
  sort(H, H+N);

  double acc_t = 0;

  for (int i = N-1; i >= 0; i--) {
    double di = H[i].first;
    double vi = H[i].second;
    double dj = D;
    double vj = 0;

    if (i < N-1) {
      dj = H[i+1].first;
      vj = H[i+1].second;
    }
    double t = (D-di)/vi;

    if (t > acc_t) {
      acc_t = t;
    } 
    else if (vi > vj) {
      t = (dj-di)/(vi-vj);
      acc_t  = max(t, acc_t);
    } else {
      acc_t = max(acc_t, (D-di)/vi);
    }
  }
  cout << fixed << setprecision(6) << D/acc_t << endl;
}

int main() { _
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cout << "Case #" << tt << ": ";
    solve();
  }
  return 0;
}

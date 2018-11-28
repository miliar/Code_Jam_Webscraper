#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
pair<int, int> a[1001];
int main()
{
  freopen("in", "r", stdin);
  int T;
  cin >> T;
  for (int t =1 ; t <= T; ++t) {
    int D, N;
    cin >> D >> N;
    float _mn = 0.0;
    for (int n = 0; n < N; ++n) {
      cin >> a[n].first >> a[n].second;
      float tn = ((float)(D-a[n].first))/a[n].second;
      _mn = max(_mn, tn);
    }

    float ans = ((float)D/_mn);
    printf ("Case #%d: %.6f\n", t, ans);
    // cout << "Case #" << t << ": " << setprecision(6) << ans << endl;
  }
};


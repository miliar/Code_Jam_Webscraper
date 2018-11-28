#include <bits/stdc++.h>

using namespace std;

const int infi = 2147483646;
const int null = -2147483646;

int main(){
  freopen("large.in","r",stdin);
  freopen("out.out","w",stdout);

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);

    // solution
    int D, N;
    cin >> D >> N;

    vector<vector<int>> horses(N, vector<int>(2));

    for (int l = 0; l < N; l++) {
      int K, S;
      cin >> K >> S;

      horses[l][0] = K;
      horses[l][1] = S;
    }

    double mx = 0.0;

    for (auto h : horses) {
      double k = h[0] + 0.0;
      double s = h[1] + 0.0;
      double t2 = (D - k) / s;
      mx = max(t2,mx);
    }

    double ans = D / mx;

    // output
    printf("%0.6lf\n", ans);
  }
}

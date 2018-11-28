#include <bits/stdc++.h>
using namespace std;

typedef long long Long;

const double PI = acos(-1.0);;

int N, K;
Long dp[1000 + 10][1000 + 10];
pair<Long,Long> dt[1000 + 10];
Long R[1000 + 10], H[1000 + 10];

Long calc() {
   memset(dp, 0, sizeof(dp));
   for(int i = 0; i < N; i++) {
      tie(R[i], H[i]) = dt[i];
   }
   dp[0][0] = 0;
   dp[0][1] = 2*R[0]*H[0];
   for(int i = 1; i < N; i++) {
      for(int k = 0; k <= i+1; k++) {
         if(k > 0 && dp[i-1][k-1] != -1) dp[i][k] = dp[i-1][k-1] + 2*R[i]*H[i];
         if(k <= i && dp[i-1][k] != -1) dp[i][k] = max(dp[i][k], dp[i-1][k]);
         // cerr << "dp[" << i << "][" << k << "] = " << dp[i][k] << "\n";
      }
   }
   Long mx = 0;
   if(K == 1) mx = R[0]*R[0] + dp[0][1];
   for(int i = 1; i < N; i++) {
      mx = max(mx, R[i]*R[i] + 2*R[i]*H[i] + dp[i-1][K-1]);
      // cerr << R[i] << " " << H[i] << " " << dp[i-1][K-1] << "\n";
   }
   return mx;
}

int main() {
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      scanf("%d%d", &N, &K);
      for(int i = 0; i < N; i++) {
         scanf("%lld%lld", &dt[i].first, &dt[i].second);
      }
      sort(dt, dt + N);
      printf("Case #%d: %.9lf\n", cs, PI * calc());
   }
}

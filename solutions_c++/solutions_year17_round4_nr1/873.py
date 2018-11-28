#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define N 101

int dp[N][N][N];

int Solve(){
  int n, n1 = 0, n2 = 0, n3 = 0, ans = 0, m;

  cin >> n >> m;
  while(n--){
    int g;
    cin >> g;
    g %= m;
    ans += (g == 0);
    n1 += (g == 1);
    n2 += (g == 2);
    n3 += (g == 3);
  }

  for(int i = 0; i <= n1; i++){
    for(int j = 0; j <= n2; j++){
      for(int k = 0; k <= n3; k++){
        dp[i][j][k] = 0;

        if(i > 0){
          int s = ((i - 1) * 1 + j * 2 + k * 3) % m;
          dp[i][j][k] = max(dp[i][j][k], (s == 0) + dp[i - 1][j][k]);
        }

        if(j > 0){
          int s = (i * 1 + (j - 1) * 2 + k * 3) % m;
          dp[i][j][k] = max(dp[i][j][k], (s == 0) + dp[i][j - 1][k]);
        }

        if(k > 0){
          int s = (i * 1 + j * 2 + (k - 1) * 3) % m;
          dp[i][j][k] = max(dp[i][j][k], (s == 0) + dp[i][j][k - 1]);
        }
      }
    }
  }

  ans += dp[n1][n2][n3];

  return ans;
}

int main(){
  int t;

  cin >> t;
  for(int k = 1; k <= t; k++)
    printf("Case #%d: %d\n", k, Solve());

  return 0;
}

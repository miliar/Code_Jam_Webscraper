#include <bits/stdc++.h>
using namespace std;
int T, N, M, Q;
pair< long long , long long > rh[1005];
long long dp[1005][1005], ans;
void ini(void){
  memset( dp, 0, sizeof(dp) );
  cin >> N >> M;
  ans = 0;
  for( int i = 1; i <= N; i++){
    cin >> rh[i].first >> rh[i].second;
  }
  sort(rh + 1, rh + N + 1, greater<pair<long long , long long > >());
}

void sol(void){
  for( int i = 1; i <= N; i++){
    dp[i][1] = max( dp[i - 1][1], rh[i].first * rh[i].first + 2ll * rh[i].first * rh[i].second);
    ans = max( ans, dp[i][1] );
    for( int j = 2; j <= i && j <= M; j++){
      dp[i][j] = max( dp[i - 1][j], dp[i - 1][j - 1] + 2ll * rh[i].first * rh[i].second);
      ans = max( ans, dp[i][j] );
    }
  }
  cout << fixed << setprecision(9) << (long double)ans * acos(-1) << endl; 
}

int main(void){
  int t;
  cin >> T;
  for(t = 1; t <= T; t++){
    ini();
    cout<<"Case #"<<t<<": ";
    sol();
  }
}

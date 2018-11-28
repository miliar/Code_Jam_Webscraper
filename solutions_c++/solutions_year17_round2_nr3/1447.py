#include <bits/stdc++.h>
using namespace std;
int main(){
  freopen("C-small-attempt0.in","r",stdin);
  freopen("out.out","w",stdout);
  int t;
  int cas =0;
  cin >> t;
  while(t--){
    int n, q;
    cin >> n >> q;
    vector<pair<double, double> >v(n);
    for(double i = 0; i < n; i++){
      cin >> v[i].first >> v[i].second;
    }
    double ans = 0;
    vector<vector<double> >dis(n,vector<double>(n));
    for(double i = 0; i < n; i++)
      for(double j = 0; j < n; j++)
        cin >> dis[i][j];
    double dp[105];
    for(int j = 0; j <100;j++)
      dp[j] = 1e18;
    double x,y ;
    cin >> x >> y;
    dp[0] = 0;
    double pos[105];
    pos[0] = 0;
    for(int i = 1; i <n; i++)
      pos[i] = pos[i-1] + dis[i-1][i];
    for(int i = 1; i < n; i++){
      for(int k = 0; k < i; k++){
        if(pos[i] - pos[k] <= v[k].first){
          double x = pos[i] - pos[k];
          //cout << x / (v[k].second) << endl;
          dp[i] = min(dp[i],(dp[k] + ((x)/(double)v[k].second)));
         }
      }
    }
    cout << "Case #" << ++cas << ": " << fixed << setprecision(6) << dp[n-1] << '\n';

  }
  return 0;
}

#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#define FOR(i, n) for(int i = 0; i < n; i++)
#define SOL(x) cout << "Case #" << tc << ": " << (x) << "\n"
#define PI (3.14159265358)

using namespace std;

int n, k;
vector<vector<double> > dp;
vector<pair<int, int> > pk;

double solve(int an, int ak){
  if(ak <= 0 || an >= n){
    return 0;
  }
  if(dp[an][ak] < 0){
    double dis = 2 * PI * pk[an].first * pk[an].second;
    if(ak == k){
      dis += PI * pk[an].first * pk[an].first;
    }
    dp[an][ak] = max(solve(an+1, ak), solve(an+1, ak-1) + dis);
  }
  return dp[an][ak];
}

int main(){
  cout << setprecision(10) << fixed;
  int tcn; cin >> tcn;
  for(int tc = 1; tc <= tcn; tc++){
    dp = vector<vector<double> > (1007, vector<double> (1007, -1));
    cin >> n >> k;
    pk = vector<pair<int, int> > (n);
    FOR(i, n){
      cin >> pk[i].first >> pk[i].second;
    }
    sort(pk.rbegin(), pk.rend());
    double sol = solve(0, k);
    SOL(sol);
  }
}

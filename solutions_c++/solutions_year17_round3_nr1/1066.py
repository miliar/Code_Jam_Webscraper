#include <bits/stdc++.h>
#define PI 3.141592653589793238462
using namespace std;
pair<int,int> arr[1004];
double dp[1004][1004];
bool vis[1004][1004];
int n,k;
double solve(int i,int j){
    if(j == 1)
        return PI*arr[i].first*arr[i].second*2.0;
    if(vis[i][j])
        return dp[i][j];
    vis[i][j] = true;
    double ret = -1e10;
    double tmp = PI*arr[i].first*arr[i].second*2.0;
    for(int i2 = i+1 ; i2 < n ; i2++){
        ret = max(ret, solve(i2, j-1)+tmp);
    }
    return dp[i][j] = ret;
}
int main() {
  freopen("inp.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T;
  cout << fixed << setprecision(20);
  cin >> T;
  for(int t = 1 ; t <= T ; t ++){
    memset(vis,0, sizeof vis);
    cout << "Case #"<<t<<": ";
    cin >> n >> k;
    for(int i = 0 ; i < n ; i ++){
        cin >> arr[i].first >> arr[i].second;
    }
    sort(arr, arr+n);
    reverse(arr, arr+n);
    double ans = 0;
    for(int j = 0 ; j < n ; j ++){
        ans = max(ans,solve(j, k)+PI*arr[j].first*arr[j].first);
        //cout << j << " "<<solve(j, k)+PI*arr[j].first*arr[j].first<<endl;
    }
    cout << ans;
    cout << endl;
  }
  return 0;
}

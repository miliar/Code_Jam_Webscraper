#include <bits/stdc++.h>
using namespace std;
const long double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;
long double dp[1005][1005];
bool vis[1005][1005];
pair<long double, long double>a[1005];
int n, k;
long double solve(int idx1, int idx2){
  if(idx1 == n)
    return (idx2 == k?0.0 : -1e15);
  long double &ret = dp[idx1][idx2];
  if(vis[idx1][idx2])
    return ret;
  vis[idx1][idx2] = 1;
  ret = -1e15;
  long double cur1 = pi * a[idx1].first * a[idx1].first;
  long double cur2 = (2 * pi * a[idx1].second * a[idx1].first);

  if(!idx2)
    ret = max(ret,cur1 + cur2 + solve(idx1 + 1, idx2 + 1));
  else
    ret = max(ret,cur2 + solve(idx1 + 1, idx2 + 1));
  ret = max(ret, solve(idx1 + 1, idx2));
  return ret;
}
int main(){
  freopen("A-large (1).in", "r", stdin);
  freopen("out.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int test = 1; test <= t; test++){
    memset(dp,0.0,sizeof dp);
    memset(vis, 0, sizeof vis);
    scanf("%d%d", &n, &k);
    for(int i = 0; i < n; i++)
      cin >> a[i].first >> a[i].second;
    sort(a, a + n);
    reverse(a, a + n);
    printf("Case #%d: ",test);
    cout << fixed << setprecision(6) << solve(0,0) << '\n';
  }
}

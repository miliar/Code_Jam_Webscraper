#include <bits/stdc++.h>

using namespace std;

int n, k, cs, id[1010], vis[1010][1010], T;
double r[1010], h[1010], dp[1010][1010], PI = acos(-1);

bool cmp(int i, int j){
  return r[i] > r[j];
}

double solve(int i = 0, int t = 0){
  if(t == k)
    return 0;
  if(i == n)
    return -1e12;
  if(vis[i][t])
    return dp[i][t];
  int ind = id[i];
  vis[i][t] = 1;
  double &ret = dp[i][t];
  dp[i][t] = solve(i + 1, t);
  double x = solve(i + 1, t + 1) + 2 * h[ind] * PI * r[ind] + (!t * PI * r[ind] * r[ind]);
  return dp[i][t] = max(dp[i][t], x);
}

int main()
{
  freopen("A-large (2).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++){
      scanf("%lf %lf", r + i, h + i);
      id[i] = i;
    }
    sort(id, id + n, cmp);
    memset(vis, 0, sizeof vis);
    printf("Case #%d: %.9f\n", ++cs, solve());
  }
  return 0;
}

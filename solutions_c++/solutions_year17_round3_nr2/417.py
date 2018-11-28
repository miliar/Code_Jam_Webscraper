#include <bits/stdc++.h>

using namespace std;

int n = 1440, cs, T, Ac, Aj, f[1500], s, e, dp[1500][750][2][2];

int solve(int i = 0, int t = 0, int p = 0, int first = 0){
  if(i == n){
    if(t != 720)
      return 1e6;
    return p != first;
  }
  if(t > 720)
    return 1e6;
  int &ret = dp[i][t][p][first];
  if(~ret)
    return ret;
  ret = 1e6;
  if(f[i] != 2)
    ret = min(ret, solve(i + 1, t + 1, 0, i ? first : 0) + (p && i));
  if(f[i] != 1)
    ret = min(ret, solve(i + 1, t, 1, i ? first : 1) + (!p && i));
  return ret;
}

int main()
{
  freopen("B-large (2).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &Ac, &Aj);
    memset(f, 0, sizeof f);
    memset(dp, -1, sizeof dp);
    for(int i=0; i<Ac; i++){
      scanf("%d %d", &s, &e);
      for(int a=s; a<e; a++)
        f[a] = 1;
    }
    for(int i=0; i<Aj; i++){
      scanf("%d %d", &s, &e);
      for(int a=s; a<e; a++)
        f[a] = 2;
    }
    printf("Case #%d: %d\n", ++cs, solve());
  }
  return 0;
}

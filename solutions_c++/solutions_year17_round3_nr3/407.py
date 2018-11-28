#include <bits/stdc++.h>

using namespace std;

int n, T, k, vis[50][500000], u, cs;
double dp[50][500000];
int p[50];
/*
double solve(int i = 0, int r = u){
  if(i == n)
    return 1;
  double &ret = dp[i][r];
  if(vis[i][r])
    return ret;
  ret = solve(i + 1, r) * p[i];
  int s = 0, e = min((int)(10000 - p[i] * 10000 + 1e-6), r);
  int x = 30;
  while(x--){
    int g = s + (s - e) / 3;
    int h = g + (s - e) / 3;
    double G = solve(i, r - g) * (p[i] + g / 10000.0);
    double H = solve(i, r - h) * (p[i] + h / 10000.0);
    if(G < H)
      s = g;
    else
      e = h;
  }
  for(int g=s; g<=e; g++)
    ret =  max(ret, solve(i, r - g) * (p[i] + g / 10000.0));
  return ret;
}
*/
bool ok(int mid){
  int ret = 0;
  for(int i=0; i<n; i++){
    ret += max(0, mid - p[i]);
    if(ret > u)
      return 0;
  }
  return 1;
}

int main()
{
  freopen("C-small-1-attempt1.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &n, &k);
    int a, b;
    memset(vis, 0, sizeof vis);
    scanf("%d.%d", &a, &b);
    u = a * 10000 + b;
    for(int i=0; i<n; i++){
      scanf("%d.%d", &a, &b);
      p[i] = a * 10000 + b;
    }
    int s = 0, e = 100000;
    while(s < e){
      int mid = (s + e + 1) >> 1;
      if(ok(mid))
        s = mid;
      else
        e = mid - 1;
    }
    double ans = 1;
    for(int i=0; i<n; i++){
      u -= max(0, s - p[i]);
      p[i] = max(p[i], s);
    }
    sort(p, p + n);
    for(int i=0; i<u; i++)
      ++p[i];
    for(int i=0; i<n; i++)
      ans *= p[i] / 10000.0;
    printf("Case #%d: %lf\n", ++cs, ans);
  }
  return 0;
}

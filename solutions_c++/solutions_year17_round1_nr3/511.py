#include <bits/stdc++.h>

using namespace std;

int hD, ans, b, d;
const int N = 102;
int dp[N][N][N][N];

void dfs(int hd, int ad, int hk, int ak, int value) {
  if (ad > N - 1) ad = N - 1;
  if (ak > N - 1) ak = N - 1;
  if (dp[hd][ad][hk][ak] != -1 && dp[hd][ad][hk][ak] <= value || value >= ans) {
    return;
  }
  dp[hd][ad][hk][ak] = value;
  //cerr << hd << " " << ad << " " << hk << " " << ak << " " << value << endl;
  if (ad >= hk) {
    ans = min(ans, dp[hd][ad][hk][ak] + 1);
  }
  else if (hd - ak > 0) {
    dfs(hd - ak, ad, hk - ad, ak, value + 1);
  }
  
  if (hd - ak > 0) {
    dfs(hd - ak, ad + b, hk, ak, value + 1);    
  }
  if (hD - ak > 0) {
    dfs(hD - ak, ad, hk, ak, value + 1); 
  }
  if (hd - max(ak - d, 0) > 0) {
    dfs(hd - max(ak - d, 0), ad, hk, max(0, ak - d), value + 1);
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    ans = int(1e9);
    int ad, hk, ak;
    cin >> hD >> ad >> hk >> ak >> b >> d;
    memset(dp, -1, sizeof(dp));
    dfs(hD, ad, hk, ak, 0);
    cout << "Case #" << i + 1 << ": " << (ans == int(1e9) ? "IMPOSSIBLE" : to_string(ans)) << endl;
  }
}
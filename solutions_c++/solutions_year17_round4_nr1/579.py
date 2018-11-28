#include <bits/stdc++.h>

using namespace std;

using ll = long long;


map<pair<vector<int>, int>, int> memo;

int p;

int g(vector<int> c, int r);

int f(vector<int> c, int r) {
  pair<vector<int>, int> q(c, r);
  if (not memo.count(q)) {
    memo[q] = g(c, r);
  }
  return memo[q];
}

int g(vector<int> c, int r) {
  int ans = 0;
  for (int i = 0; i < p; i++) {
    if (c[i] <= 0) continue;

    vector<int> nc(c);
    nc[i]--;
    int nr = (r - i + p) % p;
    int sub = f(nc, nr);
    if (r == 0) sub++;
    ans = max(ans, sub);
  }

  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n;
    cin >> n >> p;
    vector<int> c(p);
    for (int i = 0; i < n; i++) {
      int gi;
      cin >> gi;
      c[gi % p]++;
    }
    int ans = f(c, 0);
    cout << "Case #" << tc << ": " << ans << endl;
  }

}

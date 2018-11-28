#include <cstring>

#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

int memo[101][101][101];

int turn[6][3] = {
  {4, 0, 0},
  {0, 0, 4},
  {0, 2, 0},
  {2, 1, 0},
  {0, 1, 2},
  {1, 0, 1}
};

int solve(int a, int b, int c) {
  if(memo[a][b][c] != -1){
    return memo[a][b][c];
  }
  int res = 0;
  for(int i = 0; i < 6; ++i){
    if(a < turn[i][0] || b < turn[i][1] || c < turn[i][2]){
      continue;
    }
    int tmp = solve(a - turn[i][0], b - turn[i][1], c - turn[i][2]) + 1;
    res = max(res, tmp);
  }
  return memo[a][b][c] = res;
}

void solve() {
  memset(memo, -1, sizeof(memo));
  memo[0][0][0] = 0;
  int n, p;
  cin >> n >> p;
  vector<int> g(n);
  copy_n(istream_iterator<int>(cin), n, g.begin());
  vector<int> cnt(p, 0);
  for(int& val: g){
    cnt[val % p] += 1;
  }
  int ans = cnt[0];
  if(p == 2){
    ans += (cnt[1] + 1) / 2;
  }else if(p == 3){
    const int a = min(cnt[1], cnt[2]);
    const int b = max(cnt[1], cnt[2]) - a;
    ans += a + (b + 2) / 3;
  }else{
    ans += solve(cnt[1], cnt[2], cnt[3]);
  }
  cout << ans << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}

#include <bits/stdc++.h>

using namespace std;

pair<long long, long long> solver() {
  map<long long, long long> M;
  long long n, k;
  cin >> n >> k;
  M[n] = 1;
  while (1) {
    auto x = M.rbegin();
    long long val = x->first;
    long long cnt = x->second;
    if (cnt >= k) {
      val--;
      return make_pair((val + 1) >> 1, val >> 1);
    } else {
      k -= cnt;
      auto it = M.find(val);
      M.erase(val);
      val--;
      M[val >> 1] += cnt;
      M[(val + 1) >> 1] += cnt;
    }
  }
  exit(1);
}

int main() {
//  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
  ios_base::sync_with_stdio(0);
  int tc;
  cin >> tc;
  for (int test = 1; test <= tc; test++) {
    pair<long long, long long> res = solver();
    cout << "Case #" << test << ": " << res.first << " " << res.second << endl;
  }
  return 0;
}

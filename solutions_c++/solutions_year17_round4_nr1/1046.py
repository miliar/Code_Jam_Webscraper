#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const double pi = 3.141592653589793;


int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,p;
    cin >> n >> p;
    vector<int> a;
    a.resize(n);
    vector<int> mod(4, 0);
    for (auto& x : a) {
      cin >> x;
      mod[x%p] ++;
    }
    int ans = 0;
    ans += mod[0];
    mod[0] = 0;
    map<vector<int>, int> d;
    d[mod] = ans;
    queue<vector<int>> q;
    q.push(mod);
    auto update = [&](auto dd, int value) {
      if (d.count(dd) == 0 || d[dd] < value) {
        d[dd] = value;
        q.push(dd);
      }
    };
    while(!q.empty()) {
      mod = q.front();
      q.pop();
      int dd = d[mod];
      if (mod[0] == 0) {
        dd++;
      }
      for (int i = 1; i < p; ++i) {
        if (mod[i] > 0) {
          auto mm = mod;
          mm[i]--;
          mm[0] = (mod[0] + i) % p;
          update(mm, dd);
        }
      }
    }

    ans = 0;
    for (int i = 0; i < p; ++i) {
      ans = max(ans, d[vector<int>{i,0,0,0}]);
    }
    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}

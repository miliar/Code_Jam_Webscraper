#include <bits/stdc++.h>

using namespace std;

map<long long, long long> mp;

pair<long long, long long> calc(long long n, long long k) {
  if (k == 1) {
    return make_pair(n >> 1, (n - 1) >> 1);
  }
  mp.clear();
  mp[n] = 1;
  k -= 1;
  for (;;) {
    mp[(n - 1) >> 1] += mp[n];
    mp[n >> 1] += mp[n] + mp[n + 1];
    mp[(n + 1) >> 1] += mp[n + 1];
    n = (n - 1) >> 1;
    for (long long x = n + 1; x >= n; --x) {
      if (k > mp[x]) {
        k -= mp[x];
      } else {
        return make_pair(x >> 1, (x - 1) >> 1);
      }
    }
  }
}

int main() {
  long long test, n, k;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> n >> k;
    cout << "Case #" << ca << ": " << calc(n, k).first << " " << calc(n, k).second << endl;
  }
  return 0;
}

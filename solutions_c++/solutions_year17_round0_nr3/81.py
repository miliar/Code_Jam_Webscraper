#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>

using namespace std;

map<pair<int64_t, int64_t>, pair<int64_t, int64_t>> m;

pair<int64_t, int64_t> f(int64_t n, int64_t k) {
  auto nk = make_pair(n, k);
  auto it = m.find(nk);
  if (it != m.end()) return it->second;
  int64_t nl = (n-1)/2, nr = n - 1 - nl;
  int64_t kl = (k-1)/2, kr = k - 1 - kl;
  // cout << ">> " << nl << ", " << nr << ", " << kl << ", " << kr << endl;
  if (k == 1) {
    return m[nk] = make_pair(nr, nl);
  }
  if (kl < kr) return m[nk] = f(nr, kr);
  /*if (nl < nr)*/ return m[nk] = f(nl, kl);
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    m = map<pair<int64_t, int64_t>, pair<int64_t, int64_t>>();
    int64_t n, k; cin >> n >> k;
    auto res = f(n, k);
    cout << "Case #" << cas << ": " << res.first << " " << res.second << endl;
  }
  return 0;
}

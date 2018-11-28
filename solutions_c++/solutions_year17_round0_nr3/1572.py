#include <bits/stdc++.h>
using namespace std;

int T;
long long N, K;
map<long long, map<pair<long long, long long>, long long>> p;

void calc(long long val) {
  if (p.count(val)) {
    return;
  }

  if (val == 0) {
    return;
  }

  if (val == 1) {
    ++p[val][make_pair(0LL, 0LL)];
    return;
  }

  long long mid = (val + 1) / 2;
  ++p[val][make_pair(mid - 1, val - mid)];
  calc(mid - 1);
  calc(val - mid);

  const auto& q = p[mid - 1];
  for (const auto& z : q) {
    p[val][z.first] += z.second;
  }

  const auto& qq = p[val - mid];
  for (const auto& z : qq) {
    p[val][z.first] += z.second;
  }
}

pair<long long, long long> solve() {
  p.clear();

  cin >> N >> K;
  calc(N);

  /*for (const auto& num : p) {
    cout << num.first << endl;
    for (const auto& num2 : num.second) {
      cout << num2.first.first << " " << num2.first.second << " " << num2.second
          << endl;
    }
    cout << endl;
  }*/

  auto& q = p[N];
  for (auto i = q.rbegin(); i != q.rend(); ++i) {
    const auto& z = *i;
    if (z.second >= K) {
      return z.first;
    }
    K -= z.second;
  }
  assert(false);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    pair<long long, long long> res = solve();
    cout << "Case #" << test << ": " << res.second << " " << res.first << endl;
  }
}

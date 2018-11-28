#include <bits/stdc++.h>

using namespace std;

const long long INF = (long long)1e18 + 10;

void setdd(long long n, set<long long> &st) {
  if (n == 0) return;
  long long a = (n - 1) / 2, b = n - 1 - a;
  st.insert(a);
  st.insert(b);
  if (!(a & 1)) setdd(a, st);
  else setdd(b, st);
}

pair<long long, long long> solve(long long n, long long k) {
  set<long long> st;
  st.insert(n);
  setdd(n, st);
  vector<long long> vv;
  for (auto i : st) vv.push_back(i);
  int z = vv.size();
  vector<long long> cnt(z, 0);
  cnt[z - 1] = 1;
  long long nw = 0;
  int top = z - 1;
  while (1) {
    for (; top >= 0; --top) {
      if (cnt[top] > 0) break;
    }
    long long t = cnt[top];
    if (nw + t >= k) {
      long long a = (vv[top] - 1) / 2, b = vv[top] - 1 - a;
      return {b, a};
    }
    nw += t;
    long long a = (vv[top] - 1) / 2, b = vv[top] - 1 - a;
    cnt[lower_bound(vv.begin(), vv.end(), a) - vv.begin()] += cnt[top];
    cnt[lower_bound(vv.begin(), vv.end(), b) - vv.begin()] += cnt[top];
    cnt[top] = 0;
  }
  return {-1, -1};
}

int main() {
  int t;
  scanf("%d", &t);
  long long n, k;
  for (int _ = 1; _ <= t; ++_) {
    scanf("%lld%lld", &n, &k);
    printf("Case #%d: ", _);
    auto p = solve(n, k);
    printf("%lld %lld\n", p.first, p.second);
  }
  return 0;
}

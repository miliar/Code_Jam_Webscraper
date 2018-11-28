#include <iostream>
#include <vector>
#include <algorithm>

#include <inttypes.h>

using namespace std;

#define PI 3.14159265358979323846

double solve(const vector<pair<int64_t, int64_t> >& RH, int K) {
  int pos = 0;
  int64_t best = 0;
  while ((pos + K) <= RH.size()) {
    int64_t score = RH[(K + pos - 1)].first * RH[(K + pos - 1)].first;
    vector<int64_t> H; H.reserve(pos + K - 1);
    for (int i = 0; i < pos + K - 1; ++i) H.push_back(RH[i].first * RH[i].second);
    sort(H.begin(), H.end(), [](const int64_t& a, const int64_t& b) { return a <= b; });
    for (int i = 1, j = pos + K - 2; i < K; ++i, --j) score += (2 * H[j]);
    score += (2 * RH[(K + pos - 1)].first * RH[(K + pos - 1)].second);
    if (score > best) best = score; ++pos;
  }
  return PI * best;
}

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, K; cin >> N >> K;
    vector<pair<int64_t, int64_t> > RH(N, make_pair(0, 0));
    for (int j = 0; j < N; ++j) cin >> RH[j].first >> RH[j].second;
    sort(RH.begin(), RH.end(), [](const pair<int64_t, int64_t>& p, const pair<int64_t, int64_t>& q) { return p.first <= q.first; });
    printf("Case #%d: %.12f\n", i, solve(RH, K));
  }
  return 0;
}

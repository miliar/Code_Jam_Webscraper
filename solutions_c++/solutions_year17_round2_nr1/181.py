#include <bits/stdc++.h>
using namespace std;

int T;
long long D, N;
vector<pair<long long, long long>> v;

double solve() {
  v.clear();

  cin >> D >> N;
  v.resize(N);
  for (int i = 0; i < N; ++i) {
    cin >> v[i].first >> v[i].second;
  }

  sort(v.begin(), v.end());
  double max_time = 0;
  for (int i = 0; i < N; ++i) {
    max_time = max(max_time, (D - v[i].first) * 1.0 / v[i].second);
  }
  return D / max_time;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: %.10lf\n", test, solve());
  }
}

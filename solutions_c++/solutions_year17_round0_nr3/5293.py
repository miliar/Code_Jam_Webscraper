#include <string>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

static const int MX = 1000005;

int T, N, K;

struct Interval {
  int lhs, rhs;
  Interval(const int& l,
           const int& r) : lhs(l), rhs(r) {}
};

bool operator<(const Interval& a, const Interval& b) {
  int alen = a.rhs - a.lhs + 1;
  int blen = b.rhs - b.lhs + 1;
  if (alen != blen) {
    return alen < blen;
  }
  return a.lhs > b.lhs;
}

pair<int, int> solve() {
  priority_queue<Interval> q;
  q.push(Interval(1, N));
  int minLR, maxLR;
  for (int i = 0; i < K; ++i) {
    Interval s = q.top();
    q.pop();
    int mid = (s.lhs + s.rhs) / 2;
    minLR = min(mid - s.lhs, s.rhs - mid);
    maxLR = max(mid - s.lhs, s.rhs - mid);
    if (s.lhs == s.rhs) {
      continue;
    }
    q.push(Interval(s.lhs, mid-1));
    q.push(Interval(mid+1, s.rhs));
  }
  return make_pair(maxLR, minLR);
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    pair<int, int> sol = solve();
    cout << "Case #" << t << ": " << sol.first << " " << sol.second << endl;
  }
  return 0;
}
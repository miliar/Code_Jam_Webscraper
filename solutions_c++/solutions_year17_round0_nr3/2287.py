#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

void solve_slow(ll N, ll K) {
  priority_queue<tuple<int,int,int>> bestq;
  bestq.emplace(N, 0, -(N+1));
  int resMax = -1, resMin = -1;
  for (int i = 0; i < K; ++i) {
    int len, l, r;
    tie(len, l, r) = bestq.top();
    bestq.pop();
    l = -l;
    r = -r;
    int m = (l + r) / 2;
    if (m - l - 1 > 0) {
      bestq.emplace(m - l - 1, -l, -m);
    }
    if (r - m - 1 > 0) {
      bestq.emplace(r - m - 1, -m, -r);
    }
    if (i == K - 1) {
      resMax = r - m - 1;
      resMin = m - l - 1;
    }
  }
  assert(resMax != -1 && resMin != -1);
  cout << resMax << " " << resMin << "\n";
}

void solve_fast(ll N, ll K) {
  map<ll,ll> cnt;
  priority_queue<ll> lenq;
  cnt[N] = 1;
  lenq.push(N);
  while (K > cnt[lenq.top()]) {
    ll len = lenq.top();
    lenq.pop();
    K -= cnt[len];
    ll d1 = (len - 1) / 2;
    ll d2 = len / 2;
    if (d1 > 0) {
      if (!cnt.count(d1)) {
        lenq.push(d1);
      }
      cnt[d1] += cnt[len];
    }
    if (d2 > 0) {
      if (!cnt.count(d2)) {
        lenq.push(d2);
      }
      cnt[d2] += cnt[len];
    }
  }
  ll len = lenq.top();
  ll resMax = len / 2;
  ll resMin = (len - 1) / 2;
  cout << resMax << " " << resMin << "\n";
}

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  ll N, K;
  cin >> N >> K;
  solve_fast(N, K);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}

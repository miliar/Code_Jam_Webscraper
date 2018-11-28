#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

bool final_state(int p, const vi &st) {
  FOR(i, 0, p) {
    if (st[i] > 0) return false;
  }
  return true;
}

struct StHash
{
  std::size_t operator()(const vi& st) const {
    size_t result = 0;
    FOR(i, 0, sz(st)) result = (result << 8) | st[i];
    return result;
  }
};

void solve_testcase(int testcase) {
  cout << "Case #" << testcase << ": ";
  int n, p;
  cin >> n >> p;
  vi init(p + 1);
  FOR(i, 0, n) {
    int x;
    cin >> x;
    init[x % p] += 1;
  }
  unordered_map<vi,int,StHash> best;
  init[p] = 0;
  queue<vi> q;
  q.push(init);
  int res = 0;
  int iter = 0;
  while (!q.empty()) {
    iter += 1;
    vi st = q.front();
    q.pop();
    if (final_state(p, st)) {
      res = max(res, best[st]);
      continue;
    }
    int t = best[st];
    if (st[p] == 0) {
      t += 1;
    }
    FOR(i, 0, p) {
      if (st[i] > 0) {
        vi next = st;
        next[i] -= 1;
        next[p] = (next[p] + i) % p;
        if (!best.count(next)) {
          q.push(next);
        }
        best[next] = max(best[next], t);
      }
    }
  }
  cout << res << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve_testcase(testcase);
  }

  return 0;
}

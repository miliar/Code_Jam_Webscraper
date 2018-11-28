#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#ifdef DEBUG
#define dbg(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define dbg(fmt, args...)
#endif
#define REPS(i, s, n) for(int (i) = (s); (i) < (int)(n); ++(i))
#define REPRS(i, e, n) for(int (i) = (int)(n) - 1; (i) >= e; --(i))
#define REPR(i, n) REPRS(i, 0, n)
#define REP(i, n) REPS(i, 0, n)
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mp make_pair
#define x first
#define y second
#define INFI 1234567890
#define INFL 1234567890123456789LL
typedef double dbl;
typedef long double ldbl;
typedef long long ll;

using namespace std;


pair<int, int> solve(int n, int k) {
  set<pair<int, int>> intervals = {mp(n, -1)};
  for (int i = 0; i < k - 1; ++i) {
    auto c = *intervals.rbegin();
    intervals.erase(c);
    int current = c.x - 1;
    intervals.insert(mp(current / 2, i * 2));
    intervals.insert(mp(current - current / 2, i * 2 + 1));
  }
  int last = max(intervals.rbegin()->x - 1, 0);
  // cerr << last << endl;
  return {last - last / 2, last / 2};
}

pair<int, int> solve_stupid(int n, int k) {
  vector<bool> stalls(n, false);
  pair<int, int> local_answer(-1, -1);
  int ans_i = -1;
  for (int l = 0; l < k; ++l) {
    local_answer = mp(-1, -1);
    ans_i = -1;
    for (int i = 0; i < n; ++i) {
      if (!stalls[i]) {
        int l_i, r_i;
        for (l_i = i - 1; l_i >= 0 && !stalls[l_i]; --l_i);
        for (r_i = i + 1; r_i < n && !stalls[r_i]; ++r_i);
        int l = i - l_i - 1;
        int r = r_i - i - 1;
        assert(l >= 0);
        assert(r >= 0);
        auto v = mp(min(l, r), max(l, r));
        if (local_answer < v) {
          local_answer = v;
          ans_i = i;
        }
      }
    }
    assert(ans_i != -1);
    stalls[ans_i] = 1;
  }
  return mp(local_answer.y, local_answer.x);
}


int main() {
  // freopen("C.in", "r", stdin);
  // freopen("C.out", "w", stdout);
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("C-small-2-attempt0.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cerr << "test#" << t << endl;
    int n, k;
    cin >> n >> k;
    auto answer = solve(n, k);
    cout << "Case #" << t << ": " << answer.x << " " << answer.y << endl;
  }
  return 0;
}

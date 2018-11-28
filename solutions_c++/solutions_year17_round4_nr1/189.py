#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = max(a, b); }

template<typename T> T inf;
template<> constexpr int inf<int> = 1e9;
template<> constexpr ll inf<ll> = 1e18;
template<> constexpr ld inf<ld> = 1e30;

struct yes_no : numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

void output(const int value) {
  static int case_num = 0;
  printf("Case #%d: %d\n", ++case_num, value);
}

int N, P;
map<array<int,4>,int> memo;

int dfs(array<int,4> &key, int eat) {
  if (memo.count(key)) return memo[key];
  int res = 0;
  REP(i,4) {
    if (key[i] > 0) {
      --key[i];
      chmax(res, dfs(key, (eat + i) % P) + (eat == 0));
      ++key[i];
    }
  }
  // for (int i: key) cout << i << " ";
  // cout << res << endl;
  return memo[key] = res;
}

int main() {
  locale loc(locale(), new yes_no);
  cout << boolalpha;
  cout.imbue(loc);
  int Q_num;
  scanf("%d", &Q_num);
  while (Q_num--) {
    memo.clear();
    scanf("%d%d", &N, &P);
    array<int,4> count;
    REP(i,4) count[i] = 0;
    REP(i,N) {
      int G;
      scanf("%d", &G);
      count[G % P] += 1;
    }
    int res = dfs(count, 0);
    output(res);
  }
  return 0;
}


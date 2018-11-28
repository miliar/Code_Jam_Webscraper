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

void output(const int seats, const int value) {
  static int case_num = 0;
  printf("Case #%d: %d %d\n", ++case_num, seats, value);
}

int main() {
  locale loc(locale(), new yes_no);
  cout << boolalpha;
  cout.imbue(loc);
  int Q_num;
  scanf("%d", &Q_num);
  while (Q_num--) {
    int N, M, C;
    scanf("%d%d%d", &N, &M, &C);
    vector<int> cnt(N);
    vector<int> cnt2(M);
    REP(i,C) {
      int P, B;
      scanf("%d%d", &P, &B);
      cnt[P - 1]++;
      cnt2[B - 1]++;
    }
    int seats = 0;
    int sum = 0;
    REP(i,N) {
      sum += cnt[i];
      chmax(seats, (sum + i) / (i + 1));
    }
    chmax(seats, *max_element(ALL(cnt2)));
    int res = 0;
    REP(i,N) res += max(0, cnt[i] - seats);
    // cout << seats << endl;
    output(seats, res);
  }
  return 0;
}


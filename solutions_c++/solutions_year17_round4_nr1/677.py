#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

typedef long long int64;

#define DPRINT(x) cerr << __LINE__ << ": " << #x << " = " << x << endl;

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v);

template <class T>
ostream& operator <<(ostream& os, const vector<T>& v) {
    os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if (ii != v.begin()) os << " ";
        os << *ii;
    }
    os << "]";
    return os;
}

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v) {
    os << "(" << v.first << " " << v.second << ")";
    return os;
}

struct State {
  int start, cnt[4];
  State() : start(0) {
    for (int i = 0; i < 4; i++)
      cnt[i] = 0;
  }

  inline bool is_final(int P) {
    for (int i = 0; i < P; i++)
      if (cnt[i] != 0)
        return false;
    return true;
  }
};

struct StateHash {
  size_t operator()(const State& s) const {
    size_t res = s.start;
    for (int i = 0; i < 4; i++)
      res = (res << 7) | s.cnt[i];
    return res;
  }
};

inline bool operator==(const State& a, const State& b) {
  if (a.start != b.start)
    return false;
  for (int i = 0; i < 4; i++)
    if (a.cnt[i] != b.cnt[i])
      return false;
  return true;
}

unordered_map<State, int, StateHash> memo;

struct Test {
  int P;
  State s0;
  int ans;

  int go(State s) {
    if (s.is_final(P))
      return 0;
    if (memo.count(s))
      return memo[s];

    int base = (s.start == 0 ? 1 : 0);
    int cur = -1;
    for (int i = 0; i < P; i++) {
      if (s.cnt[i] == 0) continue;
      State s1 = s;
      s1.cnt[i]--;
      s1.start = (s.start + i) % P;
      cur = max(cur, base + go(s1));
    }

    memo[s] = cur;
    return cur;
  }

  void read() {
    int N;
    scanf("%d %d", &N, &P);
    for (int i = 0; i < N; i++) {
      int x;
      scanf("%d", &x);
      s0.cnt[x % P]++;
    }
  }

  void solve() {
    memo.clear();
    ans = go(s0);
  }

  void print(int num_test) {
    printf("Case #%d: %d\n", num_test, ans);
  }
};


int main() {
  // freopen("input.txt", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);

  int T;
  scanf("%d", &T);
  vector<Test> tests(T);
  for (int i = 0; i < T; i++)
    tests[i].read();

  #pragma omp parallel for
  for (int i = 0; i < T; i++) {
    clock_t start = clock();
    tests[i].solve();
    fprintf(stderr, "Solved test %d in %.3fs\n", i+1, float(clock() - start) / CLOCKS_PER_SEC);
  }

  for (int i = 0; i < T; i++)
    tests[i].print(i+1);

  return 0;
}

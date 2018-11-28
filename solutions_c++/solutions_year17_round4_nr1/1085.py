#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
typedef long long ll;

long long rdtsc() {
  long long tmp;
  asm("rdtsc" : "=A"(tmp));
  return tmp;
}

inline int myrand() {
#ifdef _WIN32
  return abs((rand() << 15) ^ rand());
#else
  return rand();
#endif
}

inline int rnd(int x) {
  return myrand() % x;
}

#ifdef LOCAL
#define LLD "%lld"
#else
#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#endif

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stdout)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define TASK "text"

void precalc() {
}

const int maxp = 5;

int n, p;
int cnt[maxp];

bool read() {
  if (scanf("%d%d", &n, &p) < 2) {
    return false;
  }
  memset(cnt, 0, sizeof(cnt));
  for (int i = 0; i < n; ++i) {
    int a;
    scanf("%d", &a);
    ++cnt[a % p];
  }
  return true;
}

vector<int> dp;

int cur[maxp];

int getNum() {
  int num = 0;
  for (int q = p - 1; q >= 0; --q) {
    num *= cnt[q] + 1;
    num += cur[q];
  }
  return num;
}

void solve() {
  int all = 1;
  for (int i = 0; i < p; ++i) {
    all *= cnt[i] + 1;
  }

  dp.resize(all);
  for (int i = 0; i < all; ++i) {
    dp[i] = 0;
  }

  for (int i = all - 1; i >= 0; --i) {
    int r = 0;
    for (int j = i, q = 0; q < p; ++q) {
      cur[q] = j % (cnt[q] + 1);
      j /= cnt[q] + 1;
      
      r = (r + (cnt[q] - cur[q]) * q) % p;
    }

    int ndp = dp[i];
    if (r == 0) {
      ++ndp;
    }

    for (int q = 0; q < p; ++q) {
      if (cur[q] > 0) {
        --cur[q];

        int nxt = getNum();
        dp[nxt] = max(dp[nxt], ndp);

        ++cur[q];
      }
    }
  }

  printf("%d\n", dp[0]);
}

int main() {
  srand(rdtsc());
  precalc();
#ifdef LOCAL 
  assert(freopen(TASK".out", "w", stdout));
  assert(freopen(TASK".in", "r", stdin));
#endif

  int T;
  scanf("%d", &T);

  for (int tn = 0; tn < T; ++tn) {
    assert(read());
    printf("Case #%d: ", tn + 1);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}



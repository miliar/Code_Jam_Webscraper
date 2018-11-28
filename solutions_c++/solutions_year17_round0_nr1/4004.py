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

const int maxn = 1010;

int n, k;
char s[maxn];

bool read() {
  if (scanf("%s%d", s, &k) < 2) {
    return false;
  }
  n = strlen(s);
  return true;
}

void solve() {
  int res = 0;
  for (int i = 0; i < n - k + 1; ++i) {
    if (s[i] == '-') {
      ++res;
      for (int j = 0; j < k; ++j) {
        s[i + j] = (s[i + j] == '+' ? '-' : '+');
      }
    }
  }

  for (int i = 0; i < n; ++i) {
    if (s[i] == '-') {
      printf("IMPOSSIBLE\n");
      return;
    }
  }

  printf("%d\n", res);
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



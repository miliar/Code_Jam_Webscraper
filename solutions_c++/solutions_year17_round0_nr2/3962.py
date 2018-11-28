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

const int maxn = 20;

int n;
char s[maxn];

bool read() {
  if (scanf("%s", s) < 1) {
    return false;
  }
  n = strlen(s);
  return true;
}

char ans[maxn];

void solve() {
  ll k;
  assert(sscanf(s, LLD, &k) == 1);
  for (int i = 0; i < n; ++i) {
    if (i > 0 && s[i] < s[i - 1]) {
      break;
    }
    if (i == n - 1) {
      memcpy(ans, s, sizeof(s));
      break;
    }
    if (s[i] > 0 && (i == 0 || s[i] > s[i - 1])) {
      memcpy(ans, s, sizeof(s));
      ans[i]--;
      memset(ans + i + 1, '9', sizeof(char) * (n - i - 1));
    }
  }

  ll res;
  assert(sscanf(ans, LLD, &res) == 1);
  printf(LLD "\n", res);
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



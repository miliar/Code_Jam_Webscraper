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

ll n, k;

bool read() {
  if (scanf(LLD LLD, &n, &k) < 2) {
    return false;
  }
  return true;
}

void solve() {
  map<ll, ll> cnt;
  cnt[n] = 1;

  for (int i = 0; ; ) {
    assert(sz(cnt));
    auto it = cnt.end();
    --it;
    ll m = it->first, w = it->second;
    cnt.erase(it);
    if (i + w >= k) {
      printf(LLD " " LLD "\n", m / 2, (m - 1) / 2);
      return;
    }
    
    cnt[m / 2] += w;
    cnt[(m - 1) / 2] += w;
    i += w;
  }
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



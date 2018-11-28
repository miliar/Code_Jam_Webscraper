#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

#define sz(x) ((int) (x).size())
#define TASK "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1);

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

void precalc() {
}

long long n, k;

int read() {
  if (scanf("%lld%lld", &n, &k) < 2) {
    return false;
  }
  k--;
  return true;
}

void solve() {
  map<long long, long long, greater<long long> > mp;
  mp[n] = 1;
  while (true) {
    long long len = mp.begin()->first, cnt = mp.begin()->second;
    mp.erase(mp.begin());
    if (k < cnt) {
      printf("%lld %lld\n", len / 2, (len - 1) / 2);
      return;
    }
    k -= cnt;
    mp[len / 2] += cnt;
    mp[(len - 1) / 2] += cnt;
  }
  assert(false);
}

int main() {
  precalc();
#ifdef DEBUG
  assert(freopen(TASK ".in", "r", stdin));
  assert(freopen(TASK ".out", "w", stdout));
#endif
  int t;
  scanf("%d", &t);
  t = 0;
  while (read()) {
    t++;
    printf("Case #%d: ", t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}

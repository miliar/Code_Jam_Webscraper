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

const int k = 6;
const char chs[k + 1] = "RYBGVO";
int n;
int a[k];

int read() {
  if (scanf("%d", &n) < 1) {
    return false;
  }
  scanf("%d%d%d%d%d%d", &a[0], &a[5], &a[1], &a[3], &a[2], &a[4]);
  return true;
}

string get() {
  /*for (int i = 0; i < k; i++) {
    eprintf("%d ", a[i]);
  }
  eprintf("\n");*/
  string ans;
  if (n <= 2) {
    for (int i = 0; i < k; i++) {
      if (a[i] >= 2) {
        assert(a[i] == 2);
        return ans;
      }
      if (a[i]) {
        ans += chs[i];
      }
    }
    return ans;
  }
  for (int i = 0; i < 3; i++) {
    if (a[3 + i]) {
      if (a[i] < 2) {
        return ans;
      }
      a[i]--;
      a[3 + i]--;
      n -= 2;
      ans = get();
      if (ans.empty()) {
        return ans;
      }
      for (int j = 0; j < sz(ans); j++) {
        if (ans[j] == chs[i]) {
          ans.insert(ans.begin() + j, chs[3 + i]);
          ans.insert(ans.begin() + j, chs[i]);
          return ans;
        }
      }
      assert(false);
    }
  }
  int lst = -1;
  int p[3] = {0, 1, 2};
  for (int i = 0; i < 3; i++) {
    for (int j = i + 1; j < 3; j++) {
      if (a[p[j]] > a[p[i]]) {
        swap(p[i], p[j]);
      }
    }
  }
  while (n) {
    int take = -1;
    for (int i = 0; i < 3; i++) {
      int id = p[i];
      if (id == lst) {
        continue;
      }
      if (take == -1 || a[id] > a[take]) {
        take = id;
      }
    }
    assert(take != -1);
    if (!a[take]) {
      ans.clear();
      return ans;
    }
    ans += chs[take];
    a[take]--;
    n--;
    lst = take;
  }
  if (ans[0] == ans[sz(ans) - 1]) {
    ans.clear();
  }
  return ans;
}

void solve() {
  string ans = get();
  if (ans.empty()) {
    printf("IMPOSSIBLE\n");
    return;
  }
  printf("%s\n", ans.c_str());
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

#include <bits/stdc++.h>

using namespace std;

const int N = 30;

struct Limits {
  int l, r, u, d;
  Limits() {
    l = N;
    r = -N;
    u = N;
    d = -N;
  }
};

int main() {
//  freopen("input.in", "r", stdin);
  freopen("A-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    int n, m;
    scanf("%d %d", &n, &m);
    set<char> chars;
    char s[N][N];
    Limits limits[256];
    for (int i = 0; i < n; ++i) {
      scanf("%s", s[i]);
      for (int j = 0; j < m; ++j) {
        if (isalpha(s[i][j])) {
          chars.insert(s[i][j]);
        }
        limits[s[i][j]].l = min(limits[s[i][j]].l, j);
        limits[s[i][j]].r = max(limits[s[i][j]].r, j);
        limits[s[i][j]].u = min(limits[s[i][j]].u, i);
        limits[s[i][j]].d = max(limits[s[i][j]].d, i);
      }
    }
    for (char c : chars) {
      bool done = false;
      while (limits[c].r < m && !done) {
        ++limits[c].r;
        for (int i = limits[c].u; i <= limits[c].d; ++i) {
          if (s[i][limits[c].r] != '?') {
            --limits[c].r;
            done = true;
            break;
          }
        }
      }
      for (int i = limits[c].u; i <= limits[c].d; ++i) {
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          s[i][j] = c;
        }
      }
    }
    for (char c : chars) {
      bool done = false;
      while (limits[c].l > 0 && !done) {
        --limits[c].l;
        for (int i = limits[c].u; i <= limits[c].d; ++i) {
          if (s[i][limits[c].l] != '?') {
            ++limits[c].l;
            done = true;
            break;
          }
        }
      }
      for (int i = limits[c].u; i <= limits[c].d; ++i) {
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          s[i][j] = c;
        }
      }
    }
    for (char c : chars) {
      bool done = false;
      while (limits[c].d < n && !done) {
        ++limits[c].d;
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          if (s[limits[c].d][j] != '?') {
            --limits[c].d;
            done = true;
            break;
          }
        }
      }
      for (int i = limits[c].u; i <= limits[c].d; ++i) {
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          s[i][j] = c;
        }
      }
    }
    for (char c : chars) {
      bool done = false;
      while (limits[c].u > 0 && !done) {
        --limits[c].u;
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          if (s[limits[c].u][j] != '?') {
            ++limits[c].u;
            done = true;
            break;
          }
        }
      }
      for (int i = limits[c].u; i <= limits[c].d; ++i) {
        for (int j = limits[c].l; j <= limits[c].r; ++j) {
          s[i][j] = c;
        }
      }
    }
    printf("Case #%d:\n", tst++);
    for (int i = 0; i < n; ++i) {
      puts(s[i]);
    }
  }
}

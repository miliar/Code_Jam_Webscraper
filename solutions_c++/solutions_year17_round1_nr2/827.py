#include <bits/stdc++.h>
using namespace std;

int T, N, P, R[100], Q[100][100], c[100], m;

struct ab { int a, b; } h[100][100];
bool cmp(ab s, ab t) { return s.b == t.b ? s.a > t.a : s.b > t.b; }

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &N, &P);
    for (int i = 0; i < N; i++) {
      scanf("%d", &R[i]);
    }
    set<int> s;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        scanf("%d", &Q[i][j]);
        h[i][j].a = ceil(Q[i][j]/1.1/R[i]);
        h[i][j].b = floor(Q[i][j]/0.9/R[i]);
        if (h[i][j].a > h[i][j].b) {
          h[i][j].a = h[i][j].b = 0;
        } else {
          s.insert(h[i][j].a);
          s.insert(h[i][j].b);
        }
      }
      // sort(h[i], h[i]+P, cmp);
    }
    m = 0;
    bool f;
    for (set<int>::reverse_iterator it = s.rbegin(); it != s.rend(); it++) {
      if (*it == 0) break;
      
      f = 1;
      while (f) {
        for (int i = 0; i < N && f; i++) {
          c[i] = -1;
          for (int j = 0; j < P; j++) {
            if (h[i][j].a <= *it && *it <= h[i][j].b) {
              if (c[i] >= 0) {
                if (h[i][j].a > h[i][c[i]].a) {
                  c[i] = j;
                }
              } else {
                c[i] = j;
              }
            }
          }
          if (c[i] == -1) f = 0;
        }
        if (f) {
          for (int i = 0; i < N; i++) {
            h[i][c[i]].a = h[i][c[i]].b = 0;
          }
          m++;
        }
      }
    }
    printf("Case #%d: %d\n", t, m);
  }
  return 0;
}


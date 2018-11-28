#include <bits/stdc++.h>
using namespace std;

int T, N, K;
const double PI = 3.1415926535897932384626;
struct p { int R, H; } P[1003];
bool cmpR(p s, p t) { return s.R > t.R; }
bool cmpH(p s, p t) { return 1.0*s.R*s.H > 1.0*t.R*t.H; }

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; i++) {
      scanf("%d%d", &P[i].R, &P[i].H);
    }
    double m = 0.0, a;
    sort(P, P+N, cmpR);
    for (int i = 0; i < N; i++) {
      a = PI*P[i].R*P[i].R + 2*PI*P[i].R*P[i].H;
      vector<p> Q(P+i+1, P+N);
      sort(Q.begin(), Q.end(), cmpH);
      for (int j = 0; j < min(K-1, (int)Q.size()); j++) {
        a += 2*PI*Q[j].R*Q[j].H;
      }
      m = max(m, a);
    }
    printf("Case #%d: %.9f\n", t, m);
  }
  return 0;
}


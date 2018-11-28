#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1007;

struct Ticket {
  int p, c;
} t[MAXN];
int T, n, c, m, num[MAXN];

bool cmp(const Ticket& t0, const Ticket& t1) {
  if (t0.c == t1.c) return t0.p < t1.p;
  return t0.c < t1.c;
}

void solve() {
  sort(t, t + m, cmp);
  int tt, r = max(1, num[0]);
  for (int i = 1; i < MAXN; i ++) {
    num[i] += num[i - 1];
    tt = (num[i] + i - 1) / i;
    if (tt > r) r = tt;
  }
  tt = 1;
  for (int i = 1; i < m; i ++)
    if (t[i].c == t[i - 1].c) {
      tt ++;
      if (tt > r) r = tt;
    } else {
      tt = 1;
    }

  tt = 0;
  for (int i = MAXN - 1; i >= 1; i --) {
    num[i] -= num[i - 1];
    tt += max(0, num[i] - r);
  }
  printf("%d %d", r, tt);
}

int main()
{
   scanf("%d", &T);
   for (int cou = 1; cou <= T; cou ++) {
     scanf("%d%d%d", &n, &c, &m);
     for (int i = 0; i < MAXN; i ++) num[i] = 0;
     for (int i = 0; i < m; i ++) {
       scanf("%d%d", &t[i].p, &t[i].c);
       num[t[i].p] ++;
     }
     printf("Case #%d: ", cou);
     solve();
     printf("\n");
   }
}

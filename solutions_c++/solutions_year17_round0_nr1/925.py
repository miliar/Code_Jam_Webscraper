#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 1; i <= n; i++)
#define REP(i, n) for(int i = 0; i < n; i++)
#define MP make_pair
#define FI first
#define SE second
#define VI vector<int>
#define CLR(x) memset(x, 0, sizeof(x))
#define SZ(x) (x.size())
#ifdef QWERTIER
#define err(x) cerr<<x<<endl;
#else
#define err(x)
#endif

#define N 1010
int T;
char s[N];
int n, k;
void change(char &c) {
  if (c == '+')
    c = '-';
  else
    c = '+';
}
int main() {
#ifdef QWERTIER
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  scanf("%d", &T);
  FOR (kase, T) {
    scanf("%s%d", s, &k);
    printf("Case #%d: ", kase);
    n = strlen(s);
    int ans = 0;
    REP (i, n-k+1) {
      if (s[i] == '-') {
        for (int j = 0; j < k; j++) {
          change(s[i+j]);
        }
        ans++;
      }
    }
    int flag = 0;
    REP (i, n) {
      if (s[i] == '-') {
        flag = 1;
      }
    }
    if (flag)
      puts("Impossible");
    else
      printf("%d\n", ans);
  }
  return 0;
}

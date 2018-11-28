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

#define N 100
char s[N];
int main() {
#ifdef QWERTIER
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  //freopen("in.txt", "r", stdin);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    scanf("%s", s);
    printf("Case #%d: ", kase);
    int n = strlen(s);
    int flag = true;
    int first_pos = true;
    for (int i = 0; i < n; i++) {
      if (flag) {
        for (int j = i+1; j < n; j++) {
          if (s[j] < s[i]) {
            flag = false;
          } else if (s[j] > s[i]) {
            break;
          }
        }
        if (flag) {
          putchar(s[i]);
          first_pos = false;
        } else {
          if (s[i] != '1' || !first_pos)
            putchar(s[i]-1);
        }
      } else {
        putchar('9');
      }
    }
    putchar('\n');
  }
  return 0;
}

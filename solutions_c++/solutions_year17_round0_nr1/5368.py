#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)

typedef long long ll;

const int S = 1000;
int tt, kk;
char s[S+1];
int ss[S];

int main() {
  scanf("%d ", &tt);
  REP(t,tt) {
    scanf("%s%d ", s, &kk);
    memset(ss, 0, sizeof(ss));
    int l = (int)strlen(s);
    REP(i,l) ss[i] = s[i]=='+' ? 0 : 1;
    int res = 0;
    REP(i,l-kk+1) if (ss[i]) {
      FOR(j,i,i+kk) ss[j] = (ss[j]+1)&1;
      res++;
    }
    int ok = 1;
    REP(i,l) if (ss[i]) ok = 0;
    printf("Case #%d: ", t+1);
    if (ok)
      printf("%d\n", res);
    else
      puts("IMPOSSIBLE");
  }
  return 0;
}


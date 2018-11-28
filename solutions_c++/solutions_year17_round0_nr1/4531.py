#include <cstdio>
#include <utility>
#include <queue>

using namespace std;

char s[1001]; int se[1001];

int main() {
  int t, ls, k; scanf("%d", &t);
  for(int cas = 1; cas <= t; ++cas) {
    scanf(" %s", s);
    scanf("%d", &k);
    for(ls = 0; s[ls]; ++ls)
      se[ls] = (s[ls]=='+')?1:0;
    int ans = 0;
    for(int j = 0; j <= ls-k; ++j)
      if(!se[j]) {
        ++ans;
        for(int i = 0; i < k; ++i)
          se[j+i] = 1-se[j+i];
      }
    bool t = true;
    for(int i = ls-k; i < ls && t; ++i)
      if(se[i] == 0)
        t = false;
    printf("Case #%d: ", cas);
    if(t) printf("%d\n", ans);
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}
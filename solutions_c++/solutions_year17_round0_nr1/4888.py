#include <bits/stdc++.h>
using namespace std;

int T, C = 1, k;
char S[1010];

int main() {
	freopen("../in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", C++);
    scanf("%s %d", S, &k);
    int l = strlen(S), ans = 0;
    for(int i = 0; i + k <= l; i++) {
      if(S[i] == '+') continue;
      ++ans;
      for(int j = 0; j < k; j++)
        S[i + j] = S[i + j] == '+' ? '-' : '+';
    }
    int f = 0;
    for(int i = 0; i < l; i++) 
      f |= (S[i] == '-');
    if(f) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
}

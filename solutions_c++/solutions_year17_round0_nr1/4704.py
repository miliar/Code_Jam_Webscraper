#include <bits/stdc++.h>

using namespace std;

char s[1005];

int main() {
   int T, k;
   scanf("%d ", &T);
   for (int t = 1; t <= T; t++) {
      printf("Case #%d: ", t);
      scanf("%s %d ", s, &k);
      int n = strlen(s);
      for (int i = 0; i < n; i++)
         s[i] = (s[i] == '+') ? 1 : 0;
      int i, c = 0;
      for (i = 0; i <= n-k; i++)
         if (!s[i]) {
            for (int j = i; j < i + k; j++)
               s[j] ^= 1;
            c++;
         }
      for (i = n-k+1; i < n; i++)
         if (!s[i]) break;
      if (i != n) printf("IMPOSSIBLE\n");
      else printf("%d\n", c);
   }
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

char s[25];

int main() {
   int T;
   scanf("%d ", &T);
   for (int t = 1; t <= T; t++) {
      scanf("%s ", s);
      int n = strlen(s), i;
      while (1) {
         for (i = 1; i < n; i++)
            if (s[i] < s[i-1]) break;
         if (i == n) break;
         for (int j = i; j < n; j++) s[j] = '9';
         s[i-1]--;
      }
      for (i = 0; i < n; i++)
         if (s[i]!='0')
            break;
      printf("Case #%d: %s\n", t, s+i);
   }
	return 0;
}

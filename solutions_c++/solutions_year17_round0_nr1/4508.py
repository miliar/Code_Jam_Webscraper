#include<stdio.h>

int main() {
   int t, k, x, y, sn[1005], i, j, n;
   char s[1005];
   scanf("%d", &t);
   for (x = 1; x <= t; x++) {
      scanf(" %s %d", s, &k);
      for (n = 0; s[n]; n++) {
         sn[n] = s[n] == '-' ? -1 : 1;
      }
      y = 0;
      for (i = 0; i <= n-k; i++) {
         if (sn[i] < 0) {
            for (j = i; j < i+k; j++)
               sn[j] = -sn[j];
            y++;
         }
      }
      for (i = 0; i < n; i++) {
         if (sn[i] < 0) {
            y = -1;
            break;
         }
      }
      printf("Case #%d: ", x);
      if (y < 0) printf("IMPOSSIBLE\n");
      else printf("%d\n", y);
   }
   return 0;
}

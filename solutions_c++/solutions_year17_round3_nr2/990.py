#include <bits/stdc++.h>

using namespace std;

void solve(int testcase) {
   int c, j, x, y, x1, y1, x2, y2, sol = 0;
   scanf("%d%d", &c, &j);
   if (! (c <= 2 && j <= 2 && c+j <= 2) ) return;
   if ((c == 1 && j == 0) || (j == 1 && c == 0)) {
      scanf("%d%d", &x, &y);
      sol = 2;
      /*
      if (x == 0 || y == 1440) sol = 1;
      else sol = 2;
      */
   } else if (c == 2 || j == 2) {
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      if (y1 > x2) { swap(x1, x2); swap(y1, y2); }
      if (y2 - x1 <= 720 || y1 + 1440-x2 <= 720) {
         sol = 2;
         /*
         if (y2 <= 720 || 1440-x1 <= 720) sol = 1;
         else sol = 2;
         */
      } else sol = 4;
      //if (y1 + 1440-x2 <= 720) sol = 2;
      //else if ( (y1 <= 720 && y2-x2 <= 720-y1) || (1440-x2 <= 720 && y1-x1 <= 720-1440+x2)) sol = 3;
      //else sol = 4;
   } else {
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      sol = 2;
      //if (y1 > x2) { swap(x1, x2); swap(x2, y2); }
      //if (y1 <= 720 && 1440-x2 <= 720) sol = 1;
      //else if (y1 <= 720 || 1440-x2 <=720) sol = 2;
      //else sol = 3;
   }
   
   printf("Case #%d: %d\n", testcase, sol);
}

int main() {
   int T;
   scanf("%d", &T);
   for (int t = 1; t <= T; t++)
      solve(t);
	return 0;
}

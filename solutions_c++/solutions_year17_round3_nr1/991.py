#include <bits/stdc++.h>
#define MAX 1005
#define R first
#define H second
#define pi 3.14159265359
#define MP make_pair

using namespace std;

typedef pair<int, int> ii;
typedef pair<double, int> di;
int n, k;
ii p[MAX];
double h[MAX];

void solve(int testcase) {
   priority_queue< di, vector<di>, greater<di> > Q;

   scanf("%d%d", &n, &k);
   for (int i = 1; i <= n; i++)
      scanf("%d%d", &p[i].R, &p[i].H);
   sort(p+1, p+n+1);
 
   h[0] = 0;
   for (int i = 1; i <= n; i++)
      h[i] = 2*pi*p[i].R*p[i].H;

   double sol = 0, s = 0;
   for (int i = 1; i < k; i++) {
      Q.push( MP(h[i], i) );
      s += h[i];
   }
   for (int i = k; i <= n; i++) {
      sol = max(sol, pi*p[i].R*p[i].R + s + h[i]);
      Q.push( MP(h[i], i) );
      s += h[i];
      di t = Q.top(); Q.pop();
      s -= h[t.second];
   }


   /*
   for (int i = 0; i <= n; i++)
      for (int j = 0; j <= n; j++)
         dp[i][j] = -1e20;
   dp[0][0] = 0;
   for (int i = 1; i <= n; i++)
      for (int j = 1; j <= i; j++) {
         for (int z = j-1; z <= i-1; z++)
            dp[i][j] = max(dp[i][j], dp[z][j-1] + pi*(p[i].R - p[z].R)*(p[i].R - p[z].R) + 2*pi*p[i].R*p[i].H);
   }
   for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++)
         printf("%5.2lf ", dp[i][j]);
      printf("\n");
   }
   double sol = 0;
   for (int i = k; i <= n; i++)
      sol = max(sol, dp[i][k]);
   */
   printf("Case #%d: %.7lf\n", testcase, sol);
}

int main() {
   int T;
   scanf("%d", &T);
   for (int t = 1; t <= T; t++)
      solve(t);
	return 0;
}

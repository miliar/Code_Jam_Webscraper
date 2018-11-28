#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair< ii, ii > state;
#define MIN first.first
#define MAX first.second
#define I   second.first
#define J   second.second
#define MP  make_pair
#define P(A, B, C, D) MP( MP( (C), (D) ), MP( -(A), (B) ) )

int N, K;

ii solve() {
   priority_queue<state> Q;

   int i = 1, j = N, mn = (i+j)/2 - i, mx = j - (i+j)/2;
   Q.push( P(i, j, mn, mx) );
   for (int z = 0; z < K; z++) {
      state S = Q.top(); Q.pop();
      int i = -S.I, j = S.J, mn = S.MIN, mx = S.MAX;
      if (z == K-1) return MP(mx, mn);
      int i2 = i, j2 = (i+j)/2 - 1, mn2 = (i2+j2)/2 - i2, mx2 = j2 - (i2+j2)/2;
      Q.push( P(i2, j2, mn2, mx2) );
      i2 = (i+j)/2 + 1; j2 = j, mn2 = (i2+j2)/2 - i2, mx2 = j2 - (i2+j2)/2;
      Q.push( P(i2, j2, mn2, mx2) );
   }
   return MP(-1, -1);
}

int main() {
   int T;
   scanf("%d", &T);
   for (int t = 1; t <= T; t++) {
      scanf("%d%d", &N, &K);
      ii sol = solve();
      printf("Case #%d: %d %d\n", t, sol.first, sol.second);
   }
   return 0;
}

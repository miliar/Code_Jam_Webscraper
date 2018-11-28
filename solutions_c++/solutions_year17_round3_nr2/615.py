#include <bits/stdc++.h>
using namespace std;

const int MXT = 60 * 24;

const int INF = 10 * MXT;

const int MXH = MXT / 2;

bool cbusy[MXT + 10], jbusy[MXT + 10];
int start;
int dp[2][MXH + 10][MXH + 10];

void reset() {
   memset(cbusy, 0, sizeof(cbusy));
   memset(jbusy, 0, sizeof(jbusy));
   memset(dp, -1, sizeof(dp));
}

int calc(int isc, int ct, int jt) {
   // cerr << isc << " " << ct << " " << jt << "\n";
   if(ct > MXH || jt > MXH) return INF;
   if(isc && cbusy[ct+jt]) return INF;
   if(!isc && jbusy[ct+jt]) return INF;
   if(dp[isc][ct][jt] != -1) return dp[isc][ct][jt];
   const int t = ct + jt;
   if(t == MXT) {
      if(ct == jt) {
         if(isc == start) return dp[isc][ct][jt] = 0;
         else return dp[isc][ct][jt] = 1;
      }
      else return dp[isc][ct][jt] = INF;
   }
   dp[isc][ct][jt] = INF;
   if(isc) {
      if(!cbusy[t+1]) dp[1][ct][jt] = min(dp[1][ct][jt], calc(1, ct+1, jt));
      if(!jbusy[t+1]) dp[1][ct][jt] = min(dp[1][ct][jt], 1 + calc(0, ct, jt+1));
   } else {
      if(!jbusy[t+1]) dp[0][ct][jt] = min(dp[0][ct][jt], calc(0, ct, jt+1));
      if(!cbusy[t+1]) dp[0][ct][jt] = min(dp[0][ct][jt], 1 + calc(1, ct+1, jt));
   }
   return dp[isc][ct][jt];
}

int main() {
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      reset();
      int AC, AJ; scanf("%d%d", &AC, &AJ);
      for(int i = 0; i < AC; i++) {
         int l, r; scanf("%d%d", &l, &r);
         fill(cbusy + l, cbusy + r, true);
      }
      for(int i = 0; i < AJ; i++) {
         int l, r; scanf("%d%d", &l, &r);
         fill(jbusy + l, jbusy + r, true);
      }
      start = 0;
      int jf = calc(0, 0, 0);
      memset(dp, -1, sizeof(dp));
      start = 1;
      int cf = calc(1, 0, 0);
      printf("Case #%d: %d\n", cs, min(cf,jf));
   }
}

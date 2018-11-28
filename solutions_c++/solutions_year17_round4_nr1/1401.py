#include <cstdio>

#include <cstring>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

typedef long long llong;
typedef vector<int> VI;
typedef vector<VI> VVI;

const char INF = 120;
int tc, N, P;
int G[101];
char cache[4][101][101][101][101];
char memo[4][101][101][101][101];
char go(int n, int m, int m0, int m1, int m2, int m3) {
   if (n >= N) return 0;
   if (m0 < 0 || m1 < 0 || m2 < 0 || m3 < 0) return -INF;
   //if (n == 0)
   //   fprintf(stderr, "n=%d m=%d m0=%d m1=%d m2=%d m3=%d\n", n, m, m0, m1, m2, m3);
   char& res = memo[m][m0][m1][m2][m3];
   if (cache[m][m0][m1][m2][m3] == tc)
      return res;
   res = 0;
   char cur;
   if (m == 0) {
      // no leftovers
      cur = go(n+1, 0, m0-1, m1, m2, m3) + 1;
      res = max(res, cur);
      cur = go(n+1, ((-1)%P+P)%P, m0, m1-1, m2, m3) + 1;
      res = max(res, cur);
      cur = go(n+1, ((-2)%P+P)%P, m0, m1, m2-1, m3) + 1;
      res = max(res, cur);
      cur = go(n+1, ((-3)%P+P)%P, m0, m1, m2, m3-1) + 1;
      res = max(res, cur);
   }
   else {
      // there are leftovers
      cur = go(n+1, m, m0-1, m1, m2, m3);
      //if (n == 1) fprintf(stderr, "1 cur = %d\n", (int) cur);
      res = max(res, cur);
      cur = go(n+1, ((m-1)%P+P)%P, m0, m1-1, m2, m3);
      //if (n == 1) fprintf(stderr, "2 cur = %d\n", (int) cur);
      res = max(res, cur);
      cur = go(n+1, ((m-2)%P+P)%P, m0, m1, m2-1, m3);
      //if (n == 1) fprintf(stderr, "3 cur = %d\n", (int) cur);
      res = max(res, cur);
      cur = go(n+1, ((m-3)%P+P)%P, m0, m1, m2, m3-1);
      //if (n == 1) fprintf(stderr, "4 cur = %d\n", (int) cur);
      res = max(res, cur);
   }
   cache[m][m0][m1][m2][m3] = tc;
   return res;
}

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (tc = 1; tc <= TC; ++tc) {
      scanf("%d %d", &N, &P);
      int mods[4] = {0, 0, 0, 0};
      REP(i, N) {
         scanf("%d", G+i);
         G[i] %= P;
         int x = G[i];
         mods[x]++;
      }
      int res = go(0, 0, mods[0], mods[1], mods[2], mods[3]);
      printf("Case #%d: %d\n", tc, res);
   }
   return 0;
}

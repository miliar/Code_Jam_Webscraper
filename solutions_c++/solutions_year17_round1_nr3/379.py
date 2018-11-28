#include <cstdio>
#include <cstring>

#include <string>
#include <vector>
#include <algorithm>

#include <queue>

using namespace std;

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

typedef long long llong;
typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 0x3f3f3f3f;

struct State {
   short Hd, Ad, Hk, Ak;
};

int Hd, Ad, Hk, Ak, B, DB;
int D[101][101][101][101];
//State P[101][101][101][101];
//char MOVE[101][101][101][101];
int bfs() {
   queue<State> q;
   q.push({Hd, Ad, Hk, Ak});

   memset(D, 0x3f, sizeof(D));
   D[Hd][Ad][Hk][Ak] = 0;

   //P[Hd][Ad][Hk][Ak].Hd = -1;
   while (!q.empty()) {
      State cur = q.front();
      q.pop();

      //fprintf(stderr, "%d %d %d %d\n", cur.Hd, cur.Ad, cur.Hk, cur.Ak);

      int dist = D[cur.Hd][cur.Ad][cur.Hk][cur.Ak];

      if (cur.Hk <= 0) {
         /*
         fprintf(stderr, "PATH\n");
         for (State x = cur; x.Hd >= 0; x = P[x.Hd][x.Ad][x.Hk][x.Ak]) {
            fprintf(stderr, "%d %d %d %d %c\n", x.Hd, x.Ad, x.Hk, x.Ak,
                    MOVE[x.Hd][x.Ad][x.Hk][x.Ak]
            );
         }
         */
         return dist;
      }

      if (cur.Hd <= 0)
         continue;

      State nxt;

      // attack
      nxt = cur;
      nxt.Hk = max(nxt.Hk - cur.Ad, 0);
      //if (nxt.Hk < 0)
      //   return dist+1;
      if (nxt.Hk > 0)
         nxt.Hd = max(cur.Hd - cur.Ak, 0);
      if (D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] > dist+1) {
         D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = dist+1;
      //   P[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = cur;
      //   MOVE[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = 'A';
         q.push(nxt);
      }

      // cure
      nxt = cur;
      nxt.Hd = Hd;
      nxt.Hd = max(nxt.Hd - cur.Ak, 0);
      if (D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] > dist+1) {
         D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = dist+1;
      //   P[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = cur;
      //   MOVE[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = 'C';
         q.push(nxt);
      }

      // buff
      if (B > 0) {
         nxt = cur;
         nxt.Ad = min(cur.Ad + B, 100);
         nxt.Hd = max(cur.Hd - nxt.Ak, 0);
         if (D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] > dist+1) {
            D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = dist+1;
         //   P[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = cur;
         //   MOVE[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = 'B';
            q.push(nxt);
         }
      }
      
      // debuff
      if (DB > 0) {
         nxt = cur;
         nxt.Ak = max(cur.Ak - DB, 0);
         nxt.Hd = max(cur.Hd - nxt.Ak, 0);
         if (D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] > dist+1) {
            D[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = dist+1;
         // P[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = cur;
         // MOVE[nxt.Hd][nxt.Ad][nxt.Hk][nxt.Ak] = 'D';
            q.push(nxt);
         }
      }
   }

   return INF;
}

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   FOR(tc, 1, TC) {
      scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &DB);
      int res = bfs();
      if (res < INF)
         printf("Case #%d: %d\n", tc, res);
      else
         printf("Case #%d: IMPOSSIBLE\n", tc);

   }

   return 0;
}

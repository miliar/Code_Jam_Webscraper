#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ size()
#define mem(array, val) memset(array, val, sizeof(array))
#define Fr first
#define Sc second
#define si(a) scanf("%d", &a)
#define sl(a) scanf("%lld", &a)
#define sd(a) scanf("%lf", &a)
#define ss(a) scanf("%s", a)
#define debug(x) cout << #x << ": " << x << endl
#define Fast_IO ios_base::sync_with_stdio(0);cin.tie(0)

typedef long long Long;
typedef pair <int, int> Pii;
///<-------------------------------------------------END OF TEMPLATE-------------------------------------------------->

#define MAX 1005
// cnt[x][y] : number of tickets y'th customer has for x'th seat
int N, M, C, cnt[MAX][MAX];
int work[MAX];

int rides(int R) {
   mem(work, 0);
   int ret = 0;

   for(int s = N; s > 0; s--) {
      int ri = R;

      // put people in current seat
      for(int p = 1; p <= C; p++) {
         int tmp = min(cnt[s][p], ri);
         ri -= tmp;
         if(cnt[s][p] > tmp) {
            work[p] += (cnt[s][p] - tmp);
            assert(cnt[s][p] - tmp >= 0);
            ret += (cnt[s][p] - tmp);
         }
      }

      // put people from below seat and give promotion
      for(int p = 1; p <= C; p++) {
         int tmp = min(work[p], ri);
         ri -= tmp;
         work[p] -= tmp;
      }
   }

   for(int p = 1; p <= C; p++) if(work[p]) return -1;

   return ret;
}

int main() {
   freopen("B-large.in", "r", stdin);
   freopen("B-large-solve.out", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      si(N); si(C); si(M);

      mem(cnt, 0);
      for(int i = 0; i < M; i++) {
         int p, b;
         si(p); si(b);
         cnt[p][b]++;
      }

      int lo = 0, hi = M;
      for(int p = 1; p <= C; p++) {
         int t = 0;
         for(int s = 1; s <= N; s++) t += cnt[s][p];
         lo = max(lo, t-1);
      }
      while(lo+1 < hi) {
         int mid = (lo+hi) >> 1;
         int prom = rides(mid);
         if(prom == -1) lo = mid;
         else hi = mid;
      }
      printf("Case #%d: %d %d\n", ca++, hi, rides(hi));
   }

   return 0;
}

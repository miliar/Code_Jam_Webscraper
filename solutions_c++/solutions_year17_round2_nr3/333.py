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

#define MAX 105
#define INF 1000000000000000LL
int N, Q, E[MAX], S[MAX];
Long dist[MAX][MAX];
double go[MAX][MAX];

int main() {
   freopen("C-large.in", "r", stdin);
   freopen("C-large.out", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      si(N); si(Q);
      for(int i = 1; i <= N; i++) {
         si(E[i]); si(S[i]);
      }
      for(int i = 1; i <= N; i++) {
         for(int j = 1; j <= N; j++) {
            si(dist[i][j]);
            if(dist[i][j] == -1) dist[i][j] = INF;
         }
         dist[i][i] = 0;
      }

      for(int k = 1; k <= N; k++)
         for(int i = 1; i <= N; i++)
            for(int j = 1; j <= N; j++)
               dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

      for(int i = 1; i <= N; i++)
         for(int j = 1; j <= N; j++) {
            if(dist[i][j] <= E[i]) go[i][j] = double(dist[i][j]) / double(S[i]);
            else go[i][j] = INF;
         }

      for(int k = 1; k <= N; k++)
         for(int i = 1; i <= N; i++)
            for(int j = 1; j <= N; j++)
               go[i][j] = min(go[i][j], go[i][k] + go[k][j]);

      printf("Case #%d:", ca++);
      while(Q--) {
         int u, v;
         si(u); si(v);
         printf(" %.8lf", go[u][v]);
      }
      puts("");
   }

   return 0;
}

#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
//using namespace __gnu_pbds;

#define PB push_back
#define MP make_pair
#define SZ size()
#define MEM(array, val) memset(array, val, sizeof(array))
#define Fr first
#define Sc second
#define si(a) scanf("%d", &a)
#define sl(a) scanf("%I64d", &a)
#define sd(a) scanf("%lf", &a)
#define ss(a) scanf("%s", a)

typedef long long Long;
typedef pair <int, int> Pii;
///<-------------------------------------------------END OF TEMPLATE-------------------------------------------------->

#define MAX 5000
int N, K;
char S[MAX];

int main() {
   freopen("A-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      ss(S); si(K);
      N = strlen(S);

      int ans = 0;
      for(int i = 0; i <= N - K; i++) if(S[i] == '-') {
         for(int j = i; j < i+K; j++) {
            if(S[j] == '+') S[j] = '-';
            else S[j] = '+';
         }
         ans++;
      }
      for(int i = 0; i < N; i++) if(S[i] == '-') {
         ans = -1;
         break;
      }

      printf("Case #%d: ", ca++);
      if(ans == -1) puts("IMPOSSIBLE");
      else printf("%d\n", ans);
   }

   return 0;
}

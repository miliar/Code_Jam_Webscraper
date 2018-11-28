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

#define MAX 20
int N;
char S[MAX];

int main() {
   freopen("B-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      ss(S);
      N = strlen(S);

      int p = 0;
      for(int i = 1; i < N; i++) {
         if(S[i] < S[i-1]) {
            S[p] = S[p] - 1;
            while(++p < N) S[p] = '9';
         } else if(S[i] > S[i-1]) {
            p = i;
         }
      }
      Long ans;
      sscanf(S, "%lld", &ans);

      printf("Case #%d: %lld\n", ca++, ans);
   }

   return 0;
}

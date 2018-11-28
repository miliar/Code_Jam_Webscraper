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

int N, R, O, Y, G, B, V;

int main() {
   freopen("B-small-attempt1.in", "r", stdin);
   freopen("B-small.out", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      si(N); si(R); si(O); si(Y); si(G), si(B), si(V);
      vector <pair <int, char> > vec;
      vec.PB(MP(R, 'R'));
      vec.PB(MP(Y, 'Y'));
      vec.PB(MP(B, 'B'));
      sort(vec.begin(), vec.end());
      reverse(vec.begin(), vec.end());
      //for(int i = 0; i < 3; i++) printf("%d %c\n", vec[i].first, vec[i].second);

      printf("Case #%d: ", ca++);
      if(vec[1].Fr + vec[2].Fr < vec[0].Fr) {
         puts("IMPOSSIBLE");
         continue;
      }
      while(vec[0].Fr) {
         if(vec[1].Fr) {
            putchar(vec[1].Sc);
            if(vec[1].Fr + vec[2].Fr > vec[0].Fr) {
               putchar(vec[2].Sc);
               vec[2].Fr--;
            }
            vec[1].Fr--;
         }
         else {
            putchar(vec[2].Sc);
            vec[2].Fr--;
         }
         putchar(vec[0].Sc);
         vec[0].Fr--;
      }
      puts("");
   }

   return 0;
}
/*
1
7 3 0 0 3 1 0
*/

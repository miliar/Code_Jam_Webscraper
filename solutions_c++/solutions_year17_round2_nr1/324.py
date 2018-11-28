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

int main() {
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      int D, N;
      si(D); si(N);
      double mi = 0.0;
      for(int i = 0; i < N; i++) {
         int k, s;
         si(k); si(s);
         mi = max(mi, double(D-k) / double(s));
      }
      printf("Case #%d: %.8lf\n", ca++, double(D) / mi);
   }

   return 0;
}

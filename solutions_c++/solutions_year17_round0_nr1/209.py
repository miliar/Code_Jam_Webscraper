#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long

char str[2333] ;
bool F[2333] ;

int main (void) {
  int t ; cin >> t ; FOR(Cas,t) {
    printf("Case #%d: ",Cas);
    int k , len , cnt = 0 , x = 0;
    memset(F,0,sizeof(F));
    cin >> str >> k;
    len = strlen(str);
    REP(i,0,len-1) {
      x = x ^ F[i];
      if (x^(str[i]=='-')) {
        if (i <= len-k) {
          ++cnt;
          x^=1;
          F[i+k]^=1;
        }
        else {
          cnt = -1;
          break;
        }
      }
    }
    if (cnt == -1) cout << "IMPOSSIBLE" << endl;
    else cout << cnt << endl;
  }
  return 0;
}

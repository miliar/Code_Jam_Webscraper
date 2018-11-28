#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long


LL F[22][11] ;

int main (void) {
  F[0][9] = 1;
  FOR(i,18) {
    F[i][9] = 1;
    for (int j = 8 ; j >= 0 ; --j) {
      F[i][j] = F[i][j+1] + F[i-1][j];
    }
  }
  int t ; cin >> t ; FOR(Cas,t) {
    printf("Case #%d: ",Cas);
    LL n , ans = 0; cin >> n;
    LL tmp = 1;
    FOR(i,18) {
      if ((n / tmp) % 10 < (n / 10 / tmp) % 10) {
        ans = i;
        n -= tmp * 10;
      }
      tmp *= 10;
    }
    tmp = 1;
    FOR(i,ans) tmp *= 10;
    cout << (n/tmp+1)*tmp-1 << endl;
  }
  return 0;
}

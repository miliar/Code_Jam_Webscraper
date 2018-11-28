#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long

int Base[233] , Q[233][233] , cur[233] ;
int n , p;

int check0() {
  FOR(i,n)
      if (Q[i][cur[i]] < cur[0] * 0.9 * Base[i] - 1e-9) return i;
  FOR(i,n)
      if (Q[i][cur[i]] > cur[0] * 1.1 * Base[i] + 1e-9) return -i;
  return 0;
}

int check() {
  while (true) {
    int x = check0();
    if (x == 0) return 0;
    else if (x < 0) ++cur[0];
    else return x;
  }
}

int main (void) {
  int T ; cin >> T ; FOR(Cas, T) {
    printf("Case #%d: ",Cas);

    cin >> n >> p;
    FOR(i,n) scanf("%d",Base+i);
    FOR(i,n) FOR(j,p) scanf("%d",Q[i]+j);
    FOR(i,n) sort(Q[i]+1,Q[i]+1+p);
    FOR(i,n) cur[i] = 1;
    int ans = 0;
    bool flag = true;
    cur[0] = 0;
    while (flag) {
      int x = check();
      if (x == 0) {
        FOR(i,n) {
          if (++cur[i] > p) flag = false;
        }
        ++ans;
      }
      else if (++cur[x] > p) flag = false;
    }
    cout << ans << endl;
  }
  return 0;
}

#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long

char Map[233][233] ;

int main (void) {
  int T ; cin >> T ; FOR(Cas, T) {
    int r , c ; cin >> r >> c;
    FOR(i,r) scanf("%s",Map[i]+1);
    int s = 0;
    FOR(i,r) {
      bool flag = false;
      FOR(j,c) if (Map[i][j] != '?') flag = true;
      if (flag) {s = i; break;}
    }
    REP(i,s,r) {
      int last_clr = 1;
      while (last_clr <= c && Map[i][last_clr] == '?') ++last_clr;
      if (last_clr <= c) {
        FOR(j,c) {
          if (Map[i][j] == '?') Map[i][j] = Map[i][last_clr];
          else last_clr = j;
        }
      }
      else {
        FOR(j,c) Map[i][j] = Map[i-1][j];
      }
    }
    for (int i = s - 1 ; i ; --i) {
      FOR(j,c) Map[i][j] = Map[i+1][j];
    }
    printf("Case #%d:\n",Cas);
    FOR(i,r) printf("%s\n",Map[i]+1);
  }
  return 0;
}

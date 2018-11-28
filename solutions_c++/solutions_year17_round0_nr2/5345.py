#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)

typedef long long ll;

const int N = 18;
ll n;
int dn;
int d[N+1], res[N+1];

int main() {
  int tt;
  scanf("%d ", &tt);
  REP(t,tt) {
    scanf("%lld ", &n);
    dn = 0;
    REP(i,N+1) {
      if (n == 0LL) break;
      d[dn++] = (int)(n%10LL);
      n /= 10LL;
    }
    res[0] = d[0];
    FOR(i,1,dn) {
      if (d[i] > d[i-1])  {
        REP(j,i) res[j] = 9;  
        res[i] = --d[i];
      } else 
        res[i] = d[i];
    }
    printf("Case #%d: ", t+1);
    REP(i,dn) {
      if (i==0 && res[dn-1]==0) continue;
      printf("%d", res[dn-1-i]);
    }
    puts("");
  }
  return 0;
}


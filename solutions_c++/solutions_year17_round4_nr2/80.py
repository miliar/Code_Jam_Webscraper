#include <cstdio>
#include <string>
#include <cassert>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

const int N = 1100;
int _;
int n,c,m;
int p[N],b[N];
int ile[N],Ile;

int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d%d",&n,&c,&m);
    int F = 0, G = 0;
    REP(i,c) ile[i] = 0;
    REP(i,m) {
      scanf("%d%d",&p[i],&b[i]); --p[i], --b[i];
      ile[b[i]]++;
    }
    F = *max_element(ile, ile+c);
    Ile = 0;
    REP(i,n) {
      REP(j,m) if (p[j] == i) Ile++;
      F = max( F, (Ile+i) / (i+1) );
    }

    REP(i,n) {
      Ile = 0;
      REP(j,m) if (p[j] == i) Ile++;
      if (Ile > F) G += Ile - F;
    }


    printf("Case #%d: %d %d\n", t+1, F, G);
  }
}

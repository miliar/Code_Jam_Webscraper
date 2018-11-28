#include <cstdio>
#include <map>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

const int MX = 110, infty = 1000000000;
int _;
int hd_ini,ad,hk,ak,b,d;

map<int,int> memo;
queue<int> q;

void push(int T, int hd, int ad, int hk, int ak) {
  if (hk > 0 && T > 0) { hd = max(0, hd - ak); }
  int key = ((hd*MX + ad)*MX + hk)*MX + ak;
  if (memo.find(key) != memo.end()) return;
  memo[key] = T+1;
  q.push(key);
}

int rek(int hd, int ad, int hk, int ak) {
  memo.clear();
  q = queue<int>();

  push(0, hd, ad, hk, ak);
  while (!q.empty()) {
    int key = q.front(); q.pop();
    int T = memo[key];
    ak = key % MX; key /= MX;
    hk = key % MX; key /= MX;
    ad = key % MX; key /= MX;
    hd = key;
//printf("%d:  hd=%d ad=%d hk=%d ak=%d\n", T, hd, ad, hk, ak);
    if (hd <= 0) continue;
    if (hk <= 0) return T-1;
    // Attack
    push(T, hd, ad, max(0, hk - ad), ak);
    // Buff
    push(T, hd, min(MX-1, ad+b), hk, ak);
    // Cure
    push(T, hd_ini, ad, hk, ak);
    // Debuff
    push(T, hd, ad, hk, max(0, ak-d));
  }
  return infty;
}

int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d%d%d%d%d",&hd_ini,&ad,&hk,&ak,&b,&d);
    int w = rek(hd_ini, ad, hk, ak);
    printf("Case #%d: ", t+1);
    if (w == infty) puts("IMPOSSIBLE");
    else printf("%d\n", w);
  }
}

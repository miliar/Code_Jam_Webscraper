#include <cstdio>
#include <set>
#include <utility>
#include <queue>
using namespace std;

struct st{
  int hd, ad, hk, ak, t;
};

set<pair<int, int> > vs[101][101];
queue<st> q;

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int Hd, Ad, Hk, Ak, B, D;
    scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);

    while(!q.empty()) q.pop();
    for(int hd = 0; hd <= Hd; hd++){
      for(int hk = 0; hk <= Hk; hk++) vs[hd][hk].clear();
    }

    vs[Hd][Ad].insert({Hk, Ak});
    q.push({Hd, Ad, Hk, Ak, 0});

    int ans = -1;

    while(!q.empty()){
      st now = q.front(); q.pop();
      st nxt;

      // attack
      nxt = now; nxt.t++;
      nxt.hk -= nxt.ad;
      if(nxt.hk <= 0){ ans = nxt.t; break; }
      nxt.hd -= nxt.ak;
      if(nxt.hd > 0){
        if(vs[nxt.hd][nxt.hk].find({nxt.ad, nxt.ak}) == vs[nxt.hd][nxt.hk].end()){
          vs[nxt.hd][nxt.hk].insert({nxt.ad, nxt.ak});
          q.push(nxt);
        }
      }

      // buff
      nxt = now; nxt.t++;
      nxt.ad += B;
      nxt.hd -= nxt.ak;
      if(nxt.hd > 0){
        if(vs[nxt.hd][nxt.hk].find({nxt.ad, nxt.ak}) == vs[nxt.hd][nxt.hk].end()){
          vs[nxt.hd][nxt.hk].insert({nxt.ad, nxt.ak});
          q.push(nxt);
        }
      }

      // cure
      nxt = now; nxt.t++;
      nxt.hd = Hd;
      nxt.hd -= nxt.ak;
      if(nxt.hd > 0){
        if(vs[nxt.hd][nxt.hk].find({nxt.ad, nxt.ak}) == vs[nxt.hd][nxt.hk].end()){
          vs[nxt.hd][nxt.hk].insert({nxt.ad, nxt.ak});
          q.push(nxt);
        }
      }

      // debuff
      nxt = now; nxt.t++;
      nxt.ak -= D; if(nxt.ak < 0) nxt.ak = 0;
      nxt.hd -= nxt.ak;
      if(nxt.hd > 0){
        if(vs[nxt.hd][nxt.hk].find({nxt.ad, nxt.ak}) == vs[nxt.hd][nxt.hk].end()){
          vs[nxt.hd][nxt.hk].insert({nxt.ad, nxt.ak});
          q.push(nxt);
        }
      }
    }

    printf("Case #%d: ", tt);
    if(ans != -1) printf("%d\n", ans);
    else puts("IMPOSSIBLE");
  }
  return 0;
}

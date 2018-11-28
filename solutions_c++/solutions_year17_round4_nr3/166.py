#include <queue>
#include <cstring>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int memo[50][1 << 5][1 << 5][1 << 5];
int h, w;

char g[64][64];

int hasShoot(int y, int x) {
  return g[y][x] == '-' || g[y][x] == '|';
}

bool solve(int p, int f, int r, int t) {
  if(p == w) return r == 0;

  if(memo[p][f][r][t]) return false;
  memo[p][f][r][t] = 1;

  REP(i,1<<h){
    // 0: vertical
    // 1: horizontal

    REP(j,h) if(hasShoot(j, p)){
      if(i & (1 << j)) g[j][p] = '-';
      else g[j][p] = '|';
    }

    bool ok = true;

    REP(j,h) if((t & (1 << j)) != 0 && g[j][p] == '-') {
      ok = false;
    }

    REP(j,h) if((r & (1 << j)) != 0){
      if(g[j][p] == '|') ok = false;
      if(g[j][p] == '#') ok = false;
    }

    REP(j,h) if((f & (1 << j)) != 0){
      if(hasShoot(j, p)) ok = false;
    }

    vector<int> es(h);
    REP(j,h){
      if(g[j][p] == '|'){
	for(int k = j - 1; k >= 0 && g[k][p] != '#'; k--){
	  if(hasShoot(k, p)) ok = false;
	  if(g[k][p] == '.') es[k] = 1;
	}
	for(int k = j + 1; k < h && g[k][p] != '#'; k++){
	  if(hasShoot(k, p)) ok = false;
	  if(g[k][p] == '.') es[k] = 1;
	}
      }
      if(g[j][p] == '.'){
	if(f & (1 << j)) es[j] = 1;
      }
    }

    if(!ok) continue;

    int nextF = 0;
    int nextR = 0;
    int nextT = 0;

    REP(j,h){
      if(g[j][p] == '-') nextF |= 1 << j;
      if(g[j][p] == '.' && (f & (1 << j))) nextF |= 1 << j;
      if(r & (1 << j)){
	if(g[j][p] != '-') nextR |= 1 << j;
      }else{
	if(g[j][p] == '.' && !es[j]) nextR |= 1 << j;
      }
      if(hasShoot(j, p)) nextT |= 1 << j;
      if(g[j][p] == '.' && (t & (1 << j))) nextT |= 1 << j;
    }

    if(solve(p + 1, nextF, nextR, nextT)){
      return true;
    }
  }

  return false;
}

int main(){
  const int t = getInt();

  REP(cc,t){
    h = getInt();
    w = getInt();

    REP(i,h) scanf("%s", g[i]);
    REP(i,h) REP(j,w) if(g[i][j] == '-') g[i][j] = '|';

    memset(memo, 0, sizeof(memo));

    printf("Case #%d: ", cc + 1);
    if(solve(0, 0, 0, 0)){
      puts("POSSIBLE");
      REP(i,h) puts(g[i]);
    }else{
      puts("IMPOSSIBLE");
    }
  }

  return 0;
}











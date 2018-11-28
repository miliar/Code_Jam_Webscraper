#include <cstdio>
#include <string>
#include <cassert>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N = 60;
int _,rows,cols;
char b[N][N];
int n,posr[N*N],posc[N*N];
int canhoriz[N*N],canvert[N*N];
int tur[N][N];

const int DIR_R[] = {0,-1,0,1}, DIR_C[] = {1,0,-1,0};
const int MIR_0[] = {1,0,3,2}, MIR_1[] = {3,2,1,0};
int gr, gc;

int varnum;
int vara[N*N*2],varb[N*N*2];

int godir(int r, int c, int dir) {
  while (true) {
    int nr = r + DIR_R[dir], nc = c + DIR_C[dir];
    if (nr < 0 || nc < 0 || nr >= rows || nc >= cols) return -1;
    if (b[nr][nc]=='#') return -1;
    if (b[nr][nc]=='|' || b[nr][nc]=='-') { gr = nr; gc = nc; return dir; }
    if (b[nr][nc]=='/') dir = MIR_0[dir];
    if (b[nr][nc]=='\\') dir = MIR_1[dir];
    r = nr;
    c = nc;
  }
}



const int M = 2*N*N;
vector<int> adj[M];
int sat_ile, sat_vis[M], sat_sort[M], sat_val[M];

void sat_dfs_mark(int x) {
  sat_vis[x] = 1; sat_val[x] = 1;
  FORE(i,adj[x]) if (!sat_vis[*i]) sat_dfs_mark(*i);
}

void sat_dfs(int x) {
  sat_vis[x] = 1;
  FORE(i,adj[x^1]) if (!sat_vis[*i^1]) sat_dfs(*i^1);
  sat_sort[sat_ile++] = x;
}


int sat() {
  REP(i,2*n) adj[i].clear();
  REP(i,varnum) {
    adj[vara[i]^1].push_back(varb[i]);
    adj[varb[i]^1].push_back(vara[i]);
  }
  sat_ile = 0;
  REP(i,2*n) sat_vis[i] = sat_val[i] = 0;
  REP(i,2*n) if (!sat_vis[i]) sat_dfs(i);
  REP(i,2*n) sat_vis[i] = 0;
  for(int i=2*n-1;i>=0;--i) if (!sat_vis[sat_sort[i]] && !sat_vis[sat_sort[i]^1]) sat_dfs_mark(sat_sort[i]);
fprintf(stderr,"SAT");
REP(i,n) fprintf(stderr," %d|%d ",sat_val[2*i],sat_val[2*i+1]); fprintf(stderr,"\n");
  REP(i,2*n) if (sat_val[i] == sat_val[i^1]) return 0;
  return 1;
}



int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d ",&rows,&cols);
    REP(i,rows) gets(b[i]);
    n = 0;
    REP(r,rows) REP(c,cols) tur[r][c] = -1;
    REP(r,rows) REP(c,cols) if (b[r][c]=='|' || b[r][c]=='-') {
      posr[n] = r; posc[n] = c;
      canhoriz[n] = (godir(r, c, 0) == -1) && (godir(r, c, 2) == -1);
      canvert[n] = (godir(r, c, 1) == -1) && (godir(r, c, 3) == -1);
      tur[r][c] = n;
      ++n;
    }
    REP(i,n) if (!canhoriz[i] && !canvert[i]) goto impos;
REP(i,n) fprintf(stderr,"%d %d  %d %d\n", posr[i], posc[i], canhoriz[i], canvert[i]);

    varnum = 0;
    REP(r,rows) REP(c,cols) if (b[r][c] == '.') {
      int d[4];
      REP(i,4) d[i] = godir(r, c, i);
      int canh = d[0] != -1 || d[2] != -1, canv = d[3] != -1 || d[1] != -1;
      if (d[0] != -1 && d[2] != -1) canh = 0;
      if (d[1] != -1 && d[3] != -1) canv = 0;
      if (d[0] == -1 && d[2] == -1 && d[1] == -1 && d[3] == -1) { goto impos; }
      else if (canv && !canh) {
	if (d[1] == -1) { godir(r,c,3); if (d[3]%2==0) canvert[tur[gr][gc]]=0; else canhoriz[tur[gr][gc]]=0; }
	if (d[3] == -1) { godir(r,c,1); if (d[1]%2==0) canvert[tur[gr][gc]]=0; else canhoriz[tur[gr][gc]]=0; }
      } else if (canh && !canv) {
	if (d[2] == -1) { godir(r,c,0); if (d[0]%2==0) canvert[tur[gr][gc]]=0; else canhoriz[tur[gr][gc]]=0; }
	if (d[0] == -1) { godir(r,c,2); if (d[2]%2==0) canvert[tur[gr][gc]]=0; else canhoriz[tur[gr][gc]]=0; }
      } else if (canh && canv) {
	int var0, var1;
	if (d[1] == -1) { godir(r,c,3); if (d[3]%2==0) var0=2*tur[gr][gc]; else var0=2*tur[gr][gc]+1; }
	if (d[3] == -1) { godir(r,c,1); if (d[1]%2==0) var0=2*tur[gr][gc]; else var0=2*tur[gr][gc]+1; }
	if (d[0] == -1) { godir(r,c,2); if (d[2]%2==0) var1=2*tur[gr][gc]; else var1=2*tur[gr][gc]+1; }
	if (d[2] == -1) { godir(r,c,0); if (d[0]%2==0) var1=2*tur[gr][gc]; else var1=2*tur[gr][gc]+1; }
	vara[varnum] = var0, varb[varnum] = var1;
	++varnum;
      } else { goto impos; }
    }
    REP(i,n) if (!canhoriz[i] && !canvert[i]) goto impos;
    REP(i,n) if (!canhoriz[i]) { vara[varnum] = varb[varnum] = 2*i+1; ++varnum; }
    else if (!canvert[i]) { vara[varnum] = varb[varnum] = 2*i; ++varnum; }

REP(i,n) fprintf(stderr,"%d %d  %d %d\n", posr[i], posc[i], canhoriz[i], canvert[i]);
REP(i,varnum) fprintf(stderr, "%d OR %d\n", vara[i], varb[i]); fprintf(stderr,"\n");

    if (varnum > 0) {
      if (!sat()) goto impos;
      REP(i,n) if (sat_val[2*i]) { assert(canhoriz[i]); canvert[i] = 0; }
      else { assert(canvert[i]); canhoriz[i] = 0; }
    }

    REP(r,rows) REP(c,cols) if (tur[r][c] != -1) {
      int t = tur[r][c];
      if (canhoriz[t]) b[r][c] = '-'; else b[r][c] = '|';
    }

    printf("Case #%d: POSSIBLE\n", t+1);
    REP(r,rows) puts(b[r]);
    continue;
impos:
    printf("Case #%d: IMPOSSIBLE\n", t+1);
  }
}

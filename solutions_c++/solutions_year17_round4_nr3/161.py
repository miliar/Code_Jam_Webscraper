#include <string>
#include <cstring>
#include <cassert>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

const int N=100000;
vi implies[2*N]; //wymuszenia, 2*x to zmienna 2*x+1 to jej zaprzeczenie
int sat_val[2*N],sat_vis[2*N],sat_sort[2*N],sat_ile;

inline void sat_or(int a,int b){
  implies[a^1].PB(b);
  implies[b^1].PB(a);
}

void sat_dfs_mark(int x){
  sat_vis[x]=1; sat_val[x]=sat_val[x^1]==-1;
  FOREACH(it,implies[x]) if (!sat_vis[*it]) sat_dfs_mark(*it);
}

void sat_dfs(int x){
  sat_vis[x]=1;
  FOREACH(it,implies[x^1]) if (!sat_vis[*it^1]) sat_dfs(*it^1);
  sat_sort[sat_ile++]=x;
}

/*przekazujemy liczbe zmiennych*/
int sat2(int n){
  sat_ile=0;
  REP(i,2*n) sat_vis[i]=0,sat_val[i]=-1;
  REP(i,2*n) if (!sat_vis[i]) sat_dfs(i);
  REP(i,2*n) sat_vis[i]=0;
  FORD(i,2*n-1,0) if (!sat_vis[sat_sort[i]]) sat_dfs_mark(sat_sort[i]);
  REP(i,2*n) if (sat_val[i]) FOREACH(it,implies[i]) if (!sat_val[*it]) return 0;
  return 1;
}

/* //Begin of the code
int main(){
  int n=3;
  sat_or(2*0,2*1+1); //x_0 or !x_1
  sat_or(2*2+1,2*1); //!x_2 or x_1 
  printf("%d\n",sat2(n));
  REP(i,2*n) printf("%d ",sat_val[i]);
  printf("\n");
  return 0;
}*/

int YS, XS;
char tab[100][100];

bool jedz(int y, int x, int yd, int xd, vector<pii> &pola) {
    for (;;) {
        y += yd;
        x += xd;
        if (y<0 || y>=YS || x<0 || x>=XS || tab[y][x]=='#')
            return 1;
        if (tab[y][x]=='|' || tab[y][x]=='-')
            return 0;
        if (tab[y][x]=='.')
            pola.PB(MP(y, x));
        else {
            swap(yd, xd);
            if (tab[y][x]=='/') {
                y = -y;
                x = -x;
            }
        }
    }
}

vi atak[100][100];

void moge(const vector<pii> pola, int var) {
    FOREACH(it, pola)
        atak[it->first][it->second].PB(var);
}

vector<pii> gdzie;

bool licz() {
    REP(a, N)
        implies[a].clear();
    gdzie.clear();
    scanf("%d%d", &YS, &XS);
    REP(y, YS) REP(x, XS)
        atak[y][x].clear();
    REP(y, YS)
        scanf("%s", tab[y]);
    REP(y, YS) REP(x, XS)
        if (tab[y][x]=='-' || tab[y][x]=='|') {
            gdzie.PB(MP(y, x));
            vector<pii> pola_poz, pola_pion;
            bool ok_pion = jedz(y, x, 1, 0, pola_pion) && jedz(y, x, -1, 0, pola_pion);
            bool ok_poz = jedz(y, x, 0, 1, pola_poz) && jedz(y, x, 0, -1, pola_poz);
            if (!ok_poz && !ok_pion)
                return 0;
            if (ok_poz)
                moge(pola_poz, 2*(size(gdzie)-1));
            if (ok_pion)
                moge(pola_pion, 2*(size(gdzie)-1)+1);
        }
    REP(y, YS) REP(x, XS)
        if (tab[y][x]=='.') {
            if (size(atak[y][x])==0)
                return 0;
            if (size(atak[y][x])==1)
                sat_or(atak[y][x][0], atak[y][x][0]);
            else
                sat_or(atak[y][x][0], atak[y][x][1]);
            assert(size(atak[y][x])<=2);
        }
    bool ok = sat2(size(gdzie));
    if (!ok) return 0;
    REP(a, size(gdzie))
        tab[gdzie[a].first][gdzie[a].second] = sat_val[2*a] ? '-' : '|';
    return 1;            
}

void spr(int y, int x, int yd, int xd) {
    for (;;) {
        y += yd;
        x += xd;
        if (y<0 || y>=YS || x<0 || x>=XS || tab[y][x]=='#')
            return;
        assert(tab[y][x]!='|' && tab[y][x]!='-');
        tab[y][x] = ':';
    }
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        bool ok = licz();
        printf("Case #%d: %sPOSSIBLE\n", (tt+1), ok ? "" : "IM");
        if (ok) {
            REP(y, YS)
                printf("%s\n", tab[y]);
            REP(y, YS)
                REP(x, XS)
                    if (tab[y][x]=='|') {
                        spr(y, x, 1, 0);
                        spr(y, x, -1, 0);
                    }
                    else
                    if (tab[y][x]=='-') {
                        spr(y, x, 0, 1);
                        spr(y, x, 0, -1);
                    }
            REP(y, YS)
                REP(x, XS)
                    assert(tab[y][x]!='.');
        }
    }
}



#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <bitset>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <iostream>
#include <algorithm>
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define PER(i,a,b) for(int i=(a);i>=(b);i--)
#define RVC(i,S) for(int i=0;i<(S).size();i++)
#define RAL(i,u) for(int i=fr[u];i!=-1;i=e[i].next)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
     
template<class T> inline
void read(T& num) {
    bool start=false,neg=false;
    char c;
    num=0;
    while((c=getchar())!=EOF) {
        if(c=='-') start=neg=true;
        else if(c>='0' && c<='9') {
            start=true;
            num=num*10+c-'0';
        } else if(start) break;
    }
    if(neg) num=-num;
}
/*============ Header Template ============*/

int ai[105],ci[5];
int f[105][105][105][4];
int g[105][105][4];
int kase;

void solve() {
    int n,m;
    read(n);read(m);
    memset(ci,0,sizeof(ci));int tot=0;
    REP(i,1,n) read(ai[i]),ci[ai[i]%m]++,tot+=ai[i];
    tot%=m;
    int res=ci[0]+1;if(tot==0) res--;
    if(m==2) res+=ci[1]/2;
    else if(m==3) res+=g[ci[1]][ci[2]][tot];
    else if(m==4) res+=f[ci[1]][ci[2]][ci[3]][tot];
    printf("Case #%d: %d\n",++kase,res);
}

inline void chkmax(int& x,int v) {
    x=max(x,v);
}

void gen() {
    int nw;
    memset(f,0x80,sizeof(f));
    memset(g,0x80,sizeof(g));
    f[0][0][0][0]=0;
    REP(i,0,100) REP(j,0,100) REP(k,0,100) if(i+j+k) REP(c,0,3) {
        if(i) nw=(c+1)%4,chkmax(f[i][j][k][nw],f[i-1][j][k][c]+(nw==0));
        if(j) nw=(c+2)%4,chkmax(f[i][j][k][nw],f[i][j-1][k][c]+(nw==0));
        if(k) nw=(c+3)%4,chkmax(f[i][j][k][nw],f[i][j][k-1][c]+(nw==0));
    }
    g[0][0][0]=0;
    REP(i,0,100) REP(j,0,100) if(i+j) REP(c,0,2) {
        if(i) nw=(c+1)%3,chkmax(g[i][j][nw],g[i-1][j][c]+(nw==0));
        if(j) nw=(c+2)%3,chkmax(g[i][j][nw],g[i][j-1][c]+(nw==0));
    }
}

int main() {
    gen();
    int T;
    read(T);
    while(T--) solve();
    return 0;
}
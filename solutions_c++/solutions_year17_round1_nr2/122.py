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

namespace flow {
    struct edge {
        int next,to,cap;
    };

    const int maxn=10005;
    const int INF=(int)(1e9)+100;
    int fr[maxn];
    int ds[maxn];
    int ci[maxn];
    bool vi[maxn];
    edge e[maxn*50];
    int tote,s,t;

    inline void addone(int u,int v,int c) {
        ++tote;
        e[tote].next=fr[u];fr[u]=tote;e[tote].to=v;e[tote].cap=c;
    }

    inline void addedge(int u,int v,int c) {
        addone(u,v,c);addone(v,u,0);
    }

    int q[maxn*50],l,r;
    bool bfs() {
        memset(vi,0,sizeof(vi));
        memcpy(ci,fr,sizeof(fr));
        ds[s]=0;vi[s]=1;
        l=1;r=0;q[++r]=s;
        for(;l<=r;) {
            int x=q[l++];
            RAL(i,x) if(!vi[e[i].to] && e[i].cap>0) {
                ds[e[i].to]=ds[x]+1;
                vi[e[i].to]=1;q[++r]=e[i].to;
            }
        } return vi[t];
    }

    int dfs(int x,int a) {
        if(x==t || a==0) return a;
        int fl=0,f;
        for(int& i=ci[x];i!=-1;i=e[i].next) {
            if(ds[e[i].to]==ds[x]+1) {
                f=dfs(e[i].to,min(a,e[i].cap));
                e[i].cap-=f;e[i^1].cap+=f;
                fl+=f;a-=f;if(!a) break;
            }
        } return fl;
    }

    inline int dinic(int _s,int _t) {
        s=_s;t=_t;int fl=0;
        while(bfs()) fl+=dfs(s,INF);
        return fl;
    }

    inline void init() {
        memset(fr,-1,sizeof(fr));tote=-1;
    }

}

int ai[55];
int bi[55][55];
int ci[55][55];
int li[55][55];
int ri[55][55];

inline int chk(int l1,int r1,int l2,int r2) {
    if(l1>r1 || l2>r2) return 0;
    if(r1<l2 || r2<l1) return 0;return 1;
}

int kase;
void solve() {
    int n,m;
    read(n);read(m);
    REP(i,1,n) read(ai[i]);
    REP(i,1,n) REP(j,1,m) {
        int x;
        read(x);
        li[i][j]=(int)floor(x/1.1/ai[i]);
        ri[i][j]=(int)floor(x/0.9/ai[i]);
        li[i][j]=max(1,li[i][j]-3);ri[i][j]+=3;
        while(li[i][j]*11*ai[i]<x*10) li[i][j]++;
        while(ri[i][j]*9*ai[i]>x*10) ri[i][j]--;
    }
    flow::init();
    int idx=0;
    int s=++idx,t=++idx;
    REP(i,1,n) REP(j,1,m) bi[i][j]=++idx,ci[i][j]=++idx,flow::addedge(bi[i][j],ci[i][j],1);
    REP(i,1,m) if(li[1][i]<=ri[1][i]) flow::addedge(s,bi[1][i],1);
    REP(i,2,n) {
        REP(j,1,m) REP(k,1,m) if(chk(li[i-1][j],ri[i-1][j],li[i][k],ri[i][k])) flow::addedge(ci[i-1][j],bi[i][k],1);
    }
    REP(i,1,m) if(li[n][i]<=ri[n][i]) flow::addedge(ci[n][i],t,1);
    printf("Case #%d: %d\n",++kase,flow::dinic(s,t));
}

int main() {
    int T;
    read(T);
    while(T--) solve();
    return 0;
}
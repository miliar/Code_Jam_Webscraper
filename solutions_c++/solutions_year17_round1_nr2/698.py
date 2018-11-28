#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <string>
#include <complex>
#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)
#define lowbit(x) ((x)&(-x))
//#pragma comment(linker,"/STACK:1024000000,1024000000")
#define eps 1e-8
#define sqr(x) ((x)*(x))
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pdd;
typedef complex<double>cp;
template<class T>inline void rread(T&num){
    num=0;T f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9')num=num*10+ch-'0',ch=getchar();
    num*=f;
}
const ll inf = 1e18;
const int maxn = 1e3+10, mod = 1e9 + 7;
const int mod1 = 1e8+7,mod2 = 41;
const double pi = acos(-1);
ll gcd (ll a, ll b)
{return ( a ? gcd(b%a, a) : b );}
void exgcd(ll a,ll b,ll &d,ll& x,ll& y)
{
    if(!b){d=a;x=1;y=0;}
    else {exgcd(b,a%b,d,y,x);y-=x*(a/b);}
}
cp power(cp a, int n)
{cp p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
unsigned long long power(unsigned long long a, unsigned long long n)
{unsigned long long p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n)
{ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod)
{ll p = 1;while (n > 0) {if(n%2) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}
//head


const int MAXN = 6000000,MAXE = MAXN*10,INF = 0x3f3f3f3f;
int head[MAXN],ed[MAXE],nxt[MAXE],cap[MAXE],q;
int n;
void clr(){
    memset(head, 0, sizeof(head));
    q = 2;
}
void ade(int f,int t,int c){
    ed[q] = t;
    cap[q] = c;
    nxt[q] = head[f];
    head[f] = q++;
}
void nfade(int f,int t,int c){
    ade(f,t,c);
    ade(t,f,0);
}
bool vis[MAXN];
int dis[MAXN];
bool dinic_bfs(int start,int end){
    memset(vis, 0, sizeof(vis));
    queue<int> que;
    que.push(start);
    dis[start] = 0;
    vis[start] = true;
    while(!que.empty()){
        int u = que.front();
        que.pop();
        for(int i = head[u];i;i = nxt[i]){
            int v = ed[i];
            if (!vis[v] && cap[i]) {
                dis[v] = dis[u] + 1;
                vis[v] = true;
                que.push(v);
            }
        }
    }
    return vis[end];
}
int cur[MAXN];
int dinic_dfs(int u,int a,int start,int end){
    if (u == end || a == 0) {
        return a;
    }
    int flow = 0,f;
    for(int &i = cur[u];i;i = nxt[i]){
        int v =  ed[i];
        if(dis[u] + 1 == dis[v] &&(f = dinic_dfs(v, min(a,cap[i]), start, end)) > 0){
            flow += f;
            a -= f;
            cap[i] -= f;
            cap[i^1] += f;
            if (a == 0) {
                break;
            }
        }
    }
    return flow;
}
int dinic(int start,int end){
    int ret = 0;
    while (dinic_bfs(start, end)) {
        for(int i = 1; i <= n; i++){
            cur[i] = head[i];
        }
        ret += dinic_dfs(start, INF, start, end);
    }
    return ret;
}

int N,P;
map<int,pair<int,int> > ver[60];
int sig[60],qty[60][60];
int ss,tt;
int tot;
inline int normalpt(int r,int c){
    return P*(r-1)+c+2;
}
void buildgph(){
    clr();
    ss = 1,tt = 2;
    tot = N*P+2;
    for(int i = 1;i <= N; i++)
        ver[i].clear();
    for(int i = 1;i <= N; i++){
        for(int j = 1;j <= P; j++){
            int r = (int)(floor((double)qty[i][j]/0.9/(double)sig[i])+0.5);
            int l = (int)(ceil((double)qty[i][j]/1.1/(double)sig[i])+0.5);
            if(l > 0 && l <= r){
                for(int k = l;k <= r; k++){
                    if(!ver[i].count(k)){
                        ver[i][k] = make_pair(tot+1,tot+2);
                        tot += 2;
                    }
                    nfade(ver[i][k].first,normalpt(i,j),1);
                    nfade(normalpt(i,j),ver[i][k].second,1);
                }
            }
        }
        if(i == 1){
            //from source
            for(int j = 1;j <= P; j++){
                nfade(ss,normalpt(i, j),1);
            }
        }
        if(i > 1){
            //interconnections
            for(map<int,pair<int,int> > :: iterator it = ver[i].begin(); it != ver[i].end(); it++){
                if(ver[i-1].count(it->first)){
                    nfade(ver[i-1][it->first].second, it->second.first,INF);
                }
            }
        }
        if(i == N){
            //to sink
            for(map<int,pair<int,int> > ::iterator it = ver[i].begin(); it != ver[i].end(); it++){
                nfade(it->second.second,tt,INF);
            }
        }
    }
    n = tot;
}

int main(int argc, char *argv[]){


    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int kase;
    scanf(" %d",&kase);
    for(int d = 1;d <= kase ;d++){
        printf("Case #%d: ",d);
        scanf(" %d %d",&N,&P);
        for(int i = 1;i <= N; i++){
            scanf(" %d",&sig[i]);
        }
        for(int i = 1;i <= N; i++){
            for(int j = 1;j <= P; j++){
                scanf(" %d",&qty[i][j]);
            }
        }
        buildgph();
        int ans = dinic(ss,tt);
    printf("%d\n",ans);
    }

    return 0;
}

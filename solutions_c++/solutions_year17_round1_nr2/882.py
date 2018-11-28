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
#include <fstream>

using namespace std;


#define LL long long
#define N 500002
#define M 1000100
#define MP make_pair
#define Pi acos(-1.0)
//#pragma comment(linker,"/STACK:1024000000,1024000000")
#define ls (rt << 1)
#define rs (ls | 1)
#define md ((ll+rr)/2)
#define lson ll, md, ls
#define rson md+1, rr, rs
#define mod 1000000007
#define inf 0x3f3f3f3f
#define sqr(x) ((x)*(x))
#define eps 1e-6
#define uLL unsnvv long long
#define ui unsnvv long long
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
#define F(x) ((x)/3+((x)%3 == 1 ? 0 : tb))
#define G(x) ((x)<tb ? (x)*3+1 : ((x) - tb)*3+2)
#define lowbit(x) ((x)&(-x))
#define fi first
#define se second
#define pii pair<int,int>
#define pli pair<LL,int>
#define pb push_back
#define MP make_pair
LL gcd(LL x,LL y){
    while(y){
        LL t = x % y;
        x = y;
        y = t;
    }
    return x;
}

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }



struct dinic {
    int fst[N], nxt[M], vv[M], cap[M], flow[M], e;
    int d[N], cur[N];
    int s, t;
    
    void init() {
        memset(fst, -1, sizeof fst);
        e = 0;
    }
    void add(int u, int v, int c) {
        vv[e] = v, nxt[e] = fst[u], cap[e] = c, flow[e] = 0, fst[u] = e++;
        vv[e] = u, nxt[e] = fst[v], cap[e] = 0, flow[e] = 0, fst[v] = e++;
    }
    
    bool bfs() {
        memset(d, -1, sizeof d);
        d[s] = 0;
        queue<int> q;
        q.push(s);
        while(!q.empty()) {
            int u = q.front(); q.pop();
            for(int i = fst[u]; ~i; i = nxt[i]) {
                int v = vv[i];
                if(d[v] == -1 && cap[i] > flow[i]) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }
        return d[t] != -1;
    }
    int dfs(int u, int a) {
        if(u == t || a == 0) return a;
        int ret = 0, f;
        for(int &i = cur[u]; ~i; i = nxt[i]) {
            int v = vv[i];
            if(d[v] == d[u] + 1 && (f = dfs(v, min(a, cap[i] - flow[i]))) > 0) {
                a -= f;
                ret += f;
                flow[i] += f;
                flow[i^1] -= f;
                if(a == 0) break;
            }
        }
        return ret;
    }
    int gao(int s, int t) {
        this -> s = s, this -> t = t;
        
        int ret = 0;
        while(bfs()) {
            memcpy(cur, fst, sizeof fst);
            ret += dfs(s, inf);
        }
        return ret;
    }
}go;

int n,P;
int s[55],a[55][55];
int ss,tt;
int tot;
map<int,pii > id[55];

inline int fckn(int r,int c)
{
    return P*(r-1)+c+2;
}

void build(){
    go.init();
    ss = 1,tt = 2;
    
    tot = n*P+2;
    for(int i = 1;i <= n; i++)
    {
        id[i].clear();
    }
    
    for(int i = 1;i <= n; i++){
        for(int j = 1;j <= P; j++){
            int r = (int)(floor(a[i][j]/0.9/(double)s[i])+0.5);
            int l = (int)(ceil(a[i][j]/1.1/(double)s[i])+0.5);
            if(l > 0 && l <= r){
                for(int k = l;k <= r; k++)
                {
                    if(!id[i].count(k)){
                        id[i][k] = MP(tot+1,tot+2);
                        tot += 2;
                    }
                    go.add(id[i][k].first, fckn(i,j),1);
                    go.add(fckn(i,j),id[i][k].second,1);
                }
            }
        }
        if(i == 1)
        {
            
            for(int j = 1;j <= P; j++)
            {
                go.add(ss,fckn(i, j),1);
            }
        }
        if(i > 1){
            
            for(auto it = id[i].begin(); it != id[i].end(); it++){
                if(id[i-1].count(it->first)){
                    go.add(id[i-1][it->first].second, it->second.first,inf);
                }
            }
        }
        if(i == n){
            
            for(auto it = id[i].begin(); it != id[i].end(); it++){
                go.add(it->second.second,tt,inf);
            }
        }
    }
}

void solve(){
    build();
    int res = go.gao(ss,tt);
    printf("%d\n",res);
}

int main(){
    
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T, casi = 0;
    scanf("%d",&T);
    while(T--){
        
        scanf("%d %d",&n,&P);
        for(int i = 1;i <= n; i++)
        {
            scanf("%d",&s[i]);
        }
        
        
        for(int i = 1;i <= n; i++){
            for(int j = 1;j <= P; j++){
                scanf("%d",&a[i][j]);
            }
        }
        printf("Case #%d: ",++casi);
        solve();
    }
    
    
    return 0;
}

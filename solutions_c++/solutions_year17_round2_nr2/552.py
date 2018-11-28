//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;


//4-side
//int xx[] = {0,0,-1,1};
//int yy[] = {-1,1,0,0};
//6-side hexagonal
//int xx[] = {2,-2,1,1,-1,-1};
//int yy[] = {0,0,1,-1,1,-1};

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 100005
#define inf 100000000

const ll mod = 1000000007ll;

///V^2*E Complexity
///number of augment path * (V+E)
///Base doesn't matter

const int INF = 2000000000;
const int MAXN = 100;///total nodes
const int MAXM = 10000;///total edges

int N,edges;
int last[MAXN],prev[MAXM],head[MAXM];
int Cap[MAXM],Flow[MAXM];
int dist[MAXN];
int nextEdge[MAXN];///used for keeping track of next edge of ith node

queue<int> Q;

void init(int N) {
    edges=0;
    memset(last,-1,sizeof(int)*N);
}

//cap=capacity of edges , flow = initial flow
inline void addEdge(int u,int v,int cap,int flow) {
    if(cap == 0) return;
    head[edges]=v;
    prev[edges]=last[u];
    Cap[edges]=cap;
    Flow[edges]=flow;
    last[u]=edges++;

    head[edges]=u;
    prev[edges]=last[v];
    Cap[edges]=0;
    Flow[edges]=0;
    last[v]=edges++;
}

inline bool dinicBfs(int S,int E,int N) {
    int from=S,to,cap,flow;
    memset(dist,0,sizeof(int)*N);
    dist[from]=1;
    while(!Q.empty()) Q.pop();
    Q.push(from);
    while(!Q.empty()) {
        from=Q.front();
        Q.pop();
        for(int e=last[from]; e>=0; e=prev[e]) {
            to=head[e];
            cap=Cap[e];
            flow=Flow[e];
            if(!dist[to] && cap>flow) {
                dist[to]=dist[from]+1;
                Q.push(to);
                ///Important
                if(to==E) return true;
                ///Need to be sure
            }
        }
    }
    return (dist[E]!=0);
}

inline int dfs(int from,int minEdge,int E) {
    if(!minEdge) return 0;
    if(from==E) return minEdge;
    int to,e,cap,flow,ret;
    for(; nextEdge[from]>=0; nextEdge[from]=prev[e]) {
        e=nextEdge[from];
        to=head[e];
        cap=Cap[e];
        flow=Flow[e];
        if(dist[to]!=dist[from]+1) continue;
        ret=dfs(to,min(minEdge,cap-flow),E);
        if(ret) {
            Flow[e]+=ret;
            Flow[e^1]-=ret;
            return ret;
        }
    }
    return 0;
}

int dinicUpdate(int S,int E) {
    int flow=0;
    while(int minEdge = dfs(S,INF,E)) {
        if(minEdge==0) break;
        flow+=minEdge;
    }
    return flow;
}

int maxFlow(int S,int E,int N) {
    int totFlow=0;
    while(dinicBfs(S,E,N)) {
        for(int i=0; i<=N; i++) nextEdge[i]=last[i]; /// update last edge of ith node
        totFlow+=dinicUpdate(S,E);
    }
    return totFlow;
}

vector<int> adj[MX];

void func() {
    adj[1].push_back(5);
    adj[1].push_back(3);
    adj[1].push_back(4);

    adj[2].push_back(5);

    adj[3].push_back(1);
    adj[3].push_back(5);
    adj[3].push_back(6);

    adj[4].push_back(1);

    adj[5].push_back(1);
    adj[5].push_back(3);
    adj[5].push_back(2);

    adj[6].push_back(3);
}

int mat[10][10];
int save[10][10];
int arr[10];

vector<int> res;

void dfs(int u) {
    if(arr[u] == 0) return;
    arr[u]--;
    for(int i = 1; i <= 6; i++) {
        if(mat[u][i] == 0) continue;
        mat[u][i]--;
        dfs(i);
    }
    res.push_back(u);
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.in.out", "w", stdout);
    string test = "ROYGBV";
    func();
    int te, ti, n;
    scanf("%d", &ti);
    for(te = 1; te <= ti; te++) {
        scanf("%d", &n);
        for(int i = 1; i <= 6; i++) {
            scanf("%d", &arr[i]);
        }
        init(20);
        for(int i = 1; i <= 6; i++) {
            addEdge(0,i,arr[i],0);
            addEdge(6+i,16,arr[i],0);
        }
        memset(save,-1,sizeof save);
        for(int i = 1; i <= 6; i++) {
            for(int j = 0; j < adj[i].size(); j++) {
                save[i][adj[i][j]] = edges;
                addEdge(i,6+adj[i][j],n+n,0);
                //printf("%d %d\n", i, adj[i][j]);
            }
        }
        int flow = maxFlow(0,16,20);
        printf("Case #%d: ", te);
        if(flow<n) {
            puts("IMPOSSIBLE");
            continue;
        } else {
            memset(mat,0,sizeof mat);
            for(int i = 1; i <= 6; i++)
                for(int j = 1; j <= 6; j++) {
                    if(save[i][j] == -1) continue;
                    int e = save[i][j];
                    mat[i][j] = Flow[e];
                    //printf("%d %d %d\n", i, j, mat[i][j]);
                }
            int pos;
            for(pos = 1; pos <= 6; pos++) {
                if(arr[pos]) break;
            }
            res.clear();
            dfs(pos);
            for(int i = 0; i < res.size(); i++)
                printf("%c", test[res[i]-1]);
            puts("");
        }
    }
    return 0;
}



/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

const int MAXN = 7210;
const int MAXM = 1000010;
const int INF = 1000000000;
struct Edge
{
    int u, v, cap, cost;
    int next;
	Edge(){}
	Edge(int u,int v,int cap,int cost,int next):u(u),v(v),cap(cap),cost(cost),next(next){}
}edge[MAXM*3];

int NE;
int head[MAXN], dist[MAXN], pp[MAXN];
bool vis[MAXN];
void init(int n)
{
    NE = 0;
    fill(head,head+n+1,-1);
}
void addedge(int u, int v, int cap, int cost)
{
    edge[NE] = Edge(u,v,cap,cost,head[u]);
	head[u] = NE++;
    edge[NE] = Edge(v,u,0,-cost,head[v]);
    head[v] = NE++;
}
int qu[3000010];
inline bool Min(int &x,int y)
{
    if(y < x) {x = y;return true;}
    return false;
}
bool SPFA(int s, int t, int n)
{
    int i, u, v , tmp;
    int he = 0 , ta = 0;
    fill(vis,vis+n+1,false);
    fill(pp,pp+n+1,-1);
    fill(dist,dist+n+1,INF);
    vis[s] = true; dist[s] = 0;
    qu[++ta] = s;
    while(he!=ta)
    {
        u = qu[++he];  vis[u] = false;
        if(he >= 2500000) he = 0;
        for(i = head[u];~ i; i = edge[i].next)
        {
            v = edge[i].v;
			tmp = dist[u] + edge[i].cost;
            if(edge[i].cap &&  dist[v] > tmp)
            {
                dist[v] = tmp;
                pp[v] = i;
                if(!vis[v])
                {
                    qu[++ta] = v;
                    if(ta >= 2500000) ta = 0;
                    vis[v] = true;
                }
            }
        }
    }
    if(dist[t] == INF) return false;
    return true;
}
pair<int,int> MCMF(int s, int t, int n) // minCostMaxFlow
{
    int flow = 0;
    int i, minflow, mincost;
    mincost = 0;
   for(;SPFA(s, t, n);)
    {
        minflow = INF + 1;
        for(i = pp[t]; ~i ; i = pp[edge[i].u])
               Min( minflow , edge[i].cap);
        flow += minflow;
        for(i = pp[t]; ~i; i = pp[edge[i].u])
        {
            edge[i].cap -= minflow;
            edge[i^1].cap += minflow;
        }
        mincost += dist[t] * minflow;
    }
    return make_pair(flow,mincost);
}


pair < int, int > pp2[1001];
int cnt[1001];


int go(int m, int N, int C, int M){
    init(N + M + N + 5);
    for(int i = 1; i <= M; i++){
        addedge(0, i, 1, 0);
        addedge(i, M + pp2[i-1].xx, 1, 0);
        if(pp2[i-1].xx > 1) addedge(i, M + N + pp2[i-1].xx - 1, 1, 1);
    }
    for(int i = 1; i <= N; i++){
        addedge(M+i, N+N+M+1, m, 0);
        addedge(M+N+i, M+i, 10000, 0);
        if(i > 1) addedge(M+N+i, M+N+i-1, 10000, 0);
    }
    pair<int,int> p = MCMF(0, N+N+M+1, N+N+M+5);
    if(p.xx != M) return mod;
    return p.yy;
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int N, C, M; cin >> N >> C >> M;
        int mx = 0;
        set0(cnt);
        REP(i, M) {
            cin >> pp2[i].xx >> pp2[i].yy;
            cnt[pp2[i].yy]++;
            mx = max(mx, cnt[pp2[i].yy]);
        }

        int lo = mx, hi = M;
        while(lo < hi){
            int mid = (lo + hi) / 2;
            if(go(mid, N, C, M) == mod) lo = mid + 1;
            else hi = mid;
        }

        cout << "Case #" << ts << ": " << lo << " " << go(lo, N, C, M) << endl;
        cerr << "Case #" << ts << ": " << lo << " " << go(lo, N, C, M) << endl;
    }
}
/*
1
2 2 4
2 1
2 1
2 2
2 2
*/


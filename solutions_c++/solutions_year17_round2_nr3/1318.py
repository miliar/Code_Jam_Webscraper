//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <unordered_set>
#include <stack>
#include <list>
#include <sstream>
#include <iomanip>
#include <complex>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a))
#define INF 0x3f3f3f3f
#define lINF 0x3f3f3f3f3f3f3f3fll
#define dINF 1e30
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define mp make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define cp complex<double>
#define here printf("!!!!!!!!\n");
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
#define upmin(a,b) {if ((a)>(b)) (a)=(b);}
#define upmax(a,b) {if ((a)<(b)) (a)=(b);}
#define upmod(a,b) (a)=((a)%(b)+(b))%(b)
#define equ(a,b) (fabs(a-b)<eps)
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;

#define maxn 101000

lld n;
lld a[maxn], sum[maxn];
lld e[maxn], s[maxn];

struct node{
    int ver, next;
    double val;
}edge[maxn];

int adj[maxn], tot, vis[maxn];
double dis[maxn];
priority_queue<pair<double, int>>Q;

void addEdge(int u, int v, double val) {
    edge[tot].ver = v; edge[tot].val = val; edge[tot].next = adj[u]; adj[u] = tot++;
}

double dijkstra(int src, int des){                          
    int i, j, y, now;
    dis[1] = 0;
    for (int i = 2; i <= n; i++) dis[i] = dINF;
    mem(vis, 0);
    while (!Q.empty()) Q.pop();
    Q.push(mp(dis[src] = 0, src));
    while (!Q.empty()){
        now = Q.top().second; Q.pop();                   
        if (now == des) return dis[des];
        if (vis[now]) continue;                        
        double tem = dis[now];
        vis[now] = 1;                                    
        for (j = adj[now]; j != -1; j = edge[j].next)
        if (!vis[y = edge[j].ver] && dis[y]>tem + edge[j].val)
            Q.push(mp(-(dis[y] = tem + edge[j].val), y));
    }
    return -1;
}


int main() {
    int T, cas;
    freopen("C-small-attempt0.in", "r", stdin);
    //rin;
    pout;
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++) {
        lld tq, tu, tv;
        scanf("%lld%lld", &n, &tq);
        for (int i = 1; i <= n; i++) {
            scanf("%lld%lld", &e[i], &s[i]);
        }
        a[1] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                lld tem;
                scanf("%lld", &tem);
                if (j != i + 1) continue;
                a[j] = tem;
            }
        }
        sum[1] = 0;
        for (int i = 2; i <= n; i++) sum[i] = sum[i - 1] + a[i];
        scanf("%lld%lld", &tu, &tv);

        mem(adj, -1);
        tot = 0;
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                double distan = sum[j] - sum[i];
                if (distan <= e[i]) {
                    addEdge(i, j, distan / s[i]);
                }
            }
        }

        double ans = dijkstra(1, n);
        
        printf("Case #%d: %.9lf\n", cas, ans);
    }

    return 0;
}
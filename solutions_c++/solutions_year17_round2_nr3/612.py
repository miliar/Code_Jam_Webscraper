/*  ^^ ====== ^^ 
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <bitset>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 150
#define maxv 1000005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;

ll v[maxn], e[maxn];
ll dp[maxn], len[maxn][maxn];
int head[maxn], cnt;
int to[maxv], Next[maxv];
double cost[maxv], dp1[maxn];
bool vis[maxn];
int n, k;


void bfs(int s) {
    memset(dp, 0x3f, sizeof dp);
    memset(vis, 0, sizeof vis);
    dp[s] = 0;
    queue<int> q; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        vis[u] = 0;
        if (dp[u] > e[s]) continue;
        for (int v = 1; v <= n; v++) {
            if (len[u][v] != -1 && len[u][v] + dp[u] < dp[v]) {
                dp[v] = dp[u] + len[u][v];
                if (!vis[v]) {
                    vis[v] = 1;
                    q.push(v);
                }
            }
        }
    }
}

void add(int u, int v, double w) {
    cost[cnt] = w;
    to[cnt] = v;
    Next[cnt] = head[u];
    head[u] = cnt++;
}

void BFS(int s) {
    for (int i = 1; i <= n; i++) dp1[i] = 1e13;
    memset(vis, 0, sizeof vis);
    dp1[s] = 0;
    queue<int> q; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        vis[u] = 0;
        for (int i = head[u]; i != -1; i = Next[i]) {
            int v = to[i];
            if (cost[i] + dp1[u] < dp1[v]) {
                dp1[v] = dp1[u] + cost[i];
                if (!vis[v]) {
                    vis[v] = 1;
                    q.push(v);
                }
            }
        }
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out1.txt","w",stdout);
    int T, kase = 1;
    scanf("%d", &T);
    while (T--) {
        memset(head, -1, sizeof head);
        cnt = 0;
        printf("Case #%d:", kase++);
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++) scanf("%lld%lld", e + i, v + i);
        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= n; j++) 
                scanf("%lld", &len[i][j]);
        for (int i = 1; i <= n; i++) {
            bfs(i);
            for (int j = 1; j <= n; j++)
                if (dp[j] <= e[i]) add(i, j, dp[j] * 1.0 / v[i]);
        }
        for (int i = 0; i < k; i++) {
            int st, ed;
            scanf("%d%d", &st, &ed);
            BFS(st);
            printf(" %.7f", dp1[ed]);
        }
        puts("");
    }   

    return 0;
}
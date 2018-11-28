#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl

using namespace std;

typedef pair<int,int>II;
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}

const long double PI = 2*acos(0.0);
const long double eps = 1e-15;
const int infi = 1e9;
const LL Linfi = 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 100005

int n, p;
LL R[105], Q[105][105];
#define maxe 1000005
#define maxv 2005

struct Dinic {
    int n, s, t, E, adj[maxe], next[maxe], last[maxv], run[maxv], level[maxv],que[maxv];
    LL flow[maxe], cap[maxe];

    void init(int _n, int _s, int _t) {
        n = _n; s = _s; t = _t; E = 0;
        FOR(i, 0, n) last[i] = -1;
    }

    void add(int u, int v, LL c1, LL c2) {
        adj[E] = v; flow[E] = 0; cap[E] = c1; next[E] = last[u]; last[u] = E++;
        adj[E] = u; flow[E] = 0; cap[E] = c2; next[E] = last[v]; last[v] = E++;
    }

    bool bfs() {
        FOR(i, 0, n) level[i] = -1;
        level[s] = 0;

        int qsize = 0;
        que[qsize++] = s;

        FO(i, 0,qsize) {
            for (int u = que[i], e = last[u]; e != -1; e = next[e]) {
                int v = adj[e];
                if (flow[e] < cap[e] && level[v] == -1) {
                    level[v] = level[u] + 1;
                    que[qsize++] = v;
                }
            }
        }

        return level[t] != -1;
    }

    LL dfs(int u, LL bot) {
        if (u == t) return bot;
        for (int &e = run[u]; e != -1; e = next[e]) {
            int v = adj[e];
            LL delta = 0;
            if (level[v] == level[u] + 1 && flow[e] < cap[e] && (delta = dfs(v, min(bot, cap[e] - flow[e] * 1ll))) > 0) {
                flow[e] += delta; flow[e ^ 1] -= delta;
                return delta;
            }
        }
        return 0;
    }

    LL maxflow() {
        LL total = 0;
        while (bfs()) {
            FOR(i, 0, n) run[i] = last[i];
            for (int delta = dfs(s, Linfi); delta > 0; delta = dfs(s, Linfi))
        total += delta;
        }
        return total;
    }
} dinic;
int st, en, u, v, c;

int check(int i, int j){
    LL a = 10*Q[1][i] / (11*R[1]);
    if((10*Q[1][i]) % (11*R[1])) a++;
    LL b = 10*Q[1][i] / (9*R[1]);

    LL c = 10*Q[2][j] / (11*R[2]);
    if((10*Q[2][j]) % (11*R[2])) c++;
    LL d = 10*Q[2][j] / (9*R[2]);

    //cout << aa << " " << bb << "  " << cc << " " << dd << endl;
    if(a > b) return 0;
    if(c > d) return 0;
    if(c <= a && a <= d) return 1;
    if(c <= b && b <= d) return 1;
    if(a <= c && c <= b) return 1;
    if(a <= d && d <= b) return 1;

    return 0;
}

void solve(){
    if(n == 1){
        int ans = 0;
        FOR(i,1,p){
            LL a = 10*Q[1][i] / (11*R[1]);
            if((10*Q[1][i]) % (11*R[1])) a++;
            LL b = 10*Q[1][i] / (9*R[1]);
            if(a <= b) ans++;

        }
        cout << ans << endl;
        return;
    }

    int st = 0, en = n*p+1;
    dinic.init(en+1, st, en);
    /// n = 2
    FOR(i,1,p) dinic.add(st,i,1,0);
    FOR(i,p+1,2*p) dinic.add(i,en,1,0);

    FOR(i,1,p) FOR(j,1,p) if(check(i,j)){
        dinic.add(i,j+p,1,0);
    }
    int ans = dinic.maxflow();
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n >> p;
        FOR(i,1,n) cin >> R[i];
        FOR(i,1,n) FOR(j,1,p) cin >> Q[i][j];
        cout << "Case #" << test << ": ";
        solve();
    }




    return 0;
}

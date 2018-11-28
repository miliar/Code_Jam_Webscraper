#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int n;

template<int MAXN>
struct dinic {

    struct edge {
        int c,f;
        int r() { return c-f; }
    };

    static const int INF = 1e9;

    int N,S,T;
    edge red[MAXN][MAXN];
    vi adjG[MAXN];

    void reset() {
        forn(u,N) forn(i,si(adjG[u])) {
            int v = adjG[u][i];
            red[u][v].f = 0;
        }
    }

    void initGraph(int n, int s, int t) {
        N = n; S = s; T = t;
        forn(u,N) {
            adjG[u].clear();
            forn(v,N) red[u][v] = (edge){0,0};
        }
    }

    void addEdge(int u, int v, int c) {
        if (!red[u][v].c && !red[v][u].c) { adjG[u].pb(v); adjG[v].pb(u); }
        red[u][v].c += c;
    }

    int dist[MAXN];
    bool dinic_bfs() {
        forn(u,N) dist[u] = INF;
        queue<int> q; q.push(S); dist[S] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            forn(i,si(adjG[u])) {
                int v = adjG[u][i];
                if (dist[v] < INF || red[u][v].r() == 0) continue;
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
        return dist[T] < INF;
    }

    int dinic_dfs(int u, int cap) {
        if (u == T) return cap;

        int res = 0;
        forn(i,si(adjG[u])) {
            int v = adjG[u][i];
            if (red[u][v].r() && dist[v] == dist[u] + 1) {
                int send = dinic_dfs(v,min(cap,red[u][v].r()));
                red[u][v].f += send; red[v][u].f -= send;
                res += send; cap -= send;
                if (cap == 0) break;
            }
        }
        if (res == 0) dist[u] = INF;
        return res;
    }

    int flow() {
        int res = 0;
        while (dinic_bfs()) res += dinic_dfs(S,INF);
        return res;
    }

    void match(int u, int v) {
        red[S][u].c = red[v][T].c = 0;
    }
};

const int N = 111;
string TYPES = ".+xo";
int board[N][N], nboard[N][N];

struct piece {
    char t; int i,j;
    void print() { cout << t << ' ' << i+1 << ' ' << j+1 << endl; }
};

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        int m;
        cin >> n >> m;
        memset(board, 0, sizeof board);
        while (m--) {
            char type; int i,j; cin >> type >> i >> j;
            board[i-1][j-1] = TYPES.find(type);
        }

        dinic<4*N> rooks, bishops;
        int rMatch = 0, bMatch = 0;
        {
            int nodes = 2*n + 2, S = nodes-2, T = nodes-1;
            rooks.initGraph(nodes,S,T);
            forn(i,n) rooks.addEdge(S,i,1);
            forn(j,n) rooks.addEdge(n+j,T,1);
            forn(i,n) forn(j,n) {
                if (board[i][j] & 2) {
                    rMatch++;
                    rooks.match(i, n+j);
                }
                else rooks.addEdge(i, n+j, 1);
            }
        }
        {
            int sz = 2*n-1;
            int nodes = 2*sz + 2, S = nodes-2, T = nodes-1;
            bishops.initGraph(nodes,S,T);

            forn(d1,sz) bishops.addEdge(S,d1,1);
            forn(d2,sz) bishops.addEdge(sz+d2,T,1);
            forn(i,n) forn(j,n) {
                int d1 = i+j, d2 = i-j + (n-1);
                if (board[i][j] & 1) {
                    bMatch++;
                    bishops.match(d1,sz+d2);
                }
                else bishops.addEdge(d1,sz+d2,1);
            }
        }
        rMatch += rooks.flow();
        bMatch += bishops.flow();

        cout << rMatch + bMatch;

        vector<piece> ans;
        forn(i,n) forn(j,n) {
            nboard[i][j] = board[i][j];
            if (rooks.red[i][n+j].f) nboard[i][j] |= 2;
            int d1 = i+j, d2 = i-j + (n-1), sz = 2*n-1;
            if (bishops.red[d1][sz+d2].f) nboard[i][j] |= 1;
            if (nboard[i][j] != board[i][j]) ans.pb((piece){TYPES[nboard[i][j]], i, j});
        }
        cout << ' ' << si(ans) << endl;
        for (auto &p : ans) p.print();

    }

    return 0;
}

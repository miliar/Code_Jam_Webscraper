// Grid DP + 2 SAT
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

/* #define debug printf */
#define debug(...)
typedef long long ll;
typedef pair<int, int> pii;

#define Q 52

int low[5004],vis[5004],scomp[5004],scompNum,I;
vector<int> adj[5004]; stack<int> verts;
void scc(int u) { low[u] = vis[u] = ++I; verts.push(u);
  for (int v : adj[u]) {
    if (!vis[v]) scc(v);
    if (scomp[v] == -1) low[u] = min(low[u], low[v]); }
  if (vis[u] <= low[u]) { int v;
    do { v=verts.top(); verts.pop(); scomp[v]=scompNum; } while (v != u);
    ++scompNum; }}
void get_scc(int n) { memset(vis,0,sizeof vis); memset(scomp,-1,sizeof scomp);
  scompNum=I=0; for (int i=0; i<n; ++i) if (!vis[i]) scc(i); }
bool truth[5004/2]; // 5004 must be at least 2 times the number of variables
// the clause a || b becomes !a => b and !b => a in the implication graph
void add_clause(int a, int b) { adj[a^1].push_back(b); adj[b^1].push_back(a); }
bool two_sat(int n) { get_scc(n);
  for (int i = 0; i < n; i += 2) { if (scomp[i] == scomp[i^1]) return false;
    truth[i/2] = (scomp[i] < scomp[i^1]); } return true; }

char G[2704];
bool v[2704];
int asgn[2704];
int mode[2704];

const int dirs[] = {1, -1, Q, -Q};
const int refl1[] = {3, 2, 1, 0};
const int refl2[] = {2, 3, 0, 1};

int trace(int n, int d) {
    /* debug("TRACE %d %d %d\n", n/Q, n%Q, d); */
    memset(v, 0, sizeof v);
    do {
        /* debug("trace %d %d %d\n", n/Q, n%Q, d); */
        n = n+dirs[d];
        if (v[n]) return 0;
        v[n] = true;
        if (G[n] == '/')
            d = refl1[d];
        else if (G[n] == '\\')
            d = refl2[d];
    } while (G[n] != '#' && G[n] != '-');
    if (G[n] == '#') return 0;
    return d < 2 ? asgn[n]^1 : asgn[n];
}

int ctrace(int n, int d) {
    int res = trace(n, d);
    /* debug("ctrace(%d %d %d) = %d (mode %d; %d)\n", n/Q, n%Q, d, res, mode[res & ~1],res&1); */
    if (!res) return 0;
    if (!mode[res & ~1]) return res;
    if (mode[res & ~1] != 1 + (res & 1)) return 0;
    return res;
}

void solve(int T) {
    memset(G, '#', sizeof G);
    memset(low, 0, sizeof low);
    memset(mode, 0, sizeof mode);
    memset(asgn, 0, sizeof asgn);
    while (verts.size()) verts.pop();
    int R; scanf("%d", &R);
    int C; scanf("%d", &C);
    int atop = 2;
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            scanf(" %c", &G[i*Q+j]);
            if (G[i*Q+j] == '|')
                G[i*Q+j] = '-';
        }
    }
    bool ok = true;
    for (int i = 0; i < 5004; i++) adj[i].clear();
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            int n = i*Q+j;
            if (G[n] == '-') {
                asgn[n] = atop; atop += 2;
            }
        }
    }
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            int n = i*Q+j;
            if (G[n] == '-') {
                if (trace(n, 0) || trace(n, 1)) {
                    adj[asgn[n]^1].push_back(asgn[n]);
                        mode[asgn[n]] += 1; debug("T%d = 1 (destruction)\n", asgn[n]);
                }

                if (trace(n, 2) || trace(n, 3)) {
                    adj[asgn[n]].push_back(asgn[n]^1);
                        mode[asgn[n]] += 2; debug("T%d = 0 (destruction)\n", asgn[n]);
                }
                if (mode[asgn[n]] == 3)
                    ok = false;
            }
        }
    }
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            int n = i*Q+j;
            if (G[n] == '.') {
                int th = ctrace(n, 0); if (!th) th = ctrace(n, 1);
                int tv = ctrace(n, 2); if (!tv) tv = ctrace(n, 3);
                if (th && tv) {
                    add_clause(th, tv);
                    debug("T%d = %d or T%d = %d\n", th & ~1, th & 1, tv & ~1, tv & 1);
                } else if (th || tv) {
                    int tt = max(th, tv);
                    adj[tt^1].push_back(tt);
                    debug("T%d = %d\n", tt & ~1, tt & 1);
                } else {
                    ok = false;
                    debug("No coverage at all\n");
                }
            }
        }
    }
    if (ok) ok = two_sat(5002);
    printf("Case #%d: ", T);
    printf(ok ? "POSSIBLE\n" : "IMPOSSIBLE\n");
    if (ok) {
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++) {
                int n = i*Q+j;
                if (G[n] == '-') {
                    printf("%c", truth[asgn[n]/2] ? '|' : '-');
                } else {
                    printf("%c", G[n]);
                }
            }
            printf("\n");
        }
    }
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}

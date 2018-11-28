// Enjoy your stay. Code by evima on 2017/04/08

#include <bits/stdc++.h>

#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

// BEGIN

struct bipartite_graph{
    int V;
    vector<vector<int>> G;
    vector<int> match;
    vector<bool> used;

    void init(int V){
        this->V = V;
        G.resize(V);
        match.resize(V);
        used.resize(V);
    }

    void add_edge(int u,int v){
        G[u].pb(v);
        G[v].pb(u);
    }

    bool dfs(int v){
        used[v] = 1;
        rep(i, sz(G[v])){
            int u = G[v][i], w = match[u];
            if(w < 0 || (!used[w] && dfs(w))){
                match[v] = u;
                match[u] = v;
                return 1;
            }
        }
        return 0;
    }

    int bipartite_matching(){
        int res = 0;
        fill(match.begin(), match.end(), -1);
        rep(v, V){
            if(match[v] < 0){
                fill(used.begin(), used.end(), false);
                if(dfs(v)) res++;
            }
        }
        return res;
    }
};

// END

int N, M, p[111][111], x[111][111];
int before[111][111], after[111][111];

void solve() {
    memset(p, 0, sizeof(p));
    memset(x, 0, sizeof(x));
    cin >> N >> M;
    int y = 0;
    rep(i, M){
        char t; int r, c;
        cin >> t >> r >> c;
        r--; c--;
        if(t == '+'){
            p[r][c] = 1;
            y++;
        }else if(t == 'x'){
            x[r][c] = 1;
            y++;
        }else{
            p[r][c] = x[r][c] = 1;
            y += 2;
        }
    }

    rep(i, N){
        rep(j, N){
            before[i][j] = after[i][j] = x[i][j] | p[i][j] << 1;
        }
    }

    rep(i, N){
        rep(j, N){
            if(x[i][j] == 0){
                int ok = 1;
                rep(jj, N){
                    if(x[i][jj] == 1){
                        ok = 0; break;
                    }
                }
                rep(ii, N){
                    if(x[ii][j] == 1){
                        ok = 0; break;
                    }
                }
                if(ok){
                    y++;
                    x[i][j] = 1;
                    after[i][j] |= 1;
                }
            }
        }
    }

    set<int> usedSum, usedDif;
    rep(i, N){
        rep(j, N){
            if(p[i][j] == 1){
                usedSum.insert(i+j);
                usedDif.insert(i-j);
            }
        }
    }

    bipartite_graph G[2];
    int lo[2];
    rep(i, 2){
        G[i].init(2*N);
        lo[i] = -N;
        if(-lo[i] % 2 != i){
            lo[i]++;
        }
    }
    rep(sum, 0, 2*N-1){
        if(usedSum.count(sum)) continue;
        rep(dif, -N+1, N){
            if((sum + dif) % 2) continue;
            int r = (sum + dif) / 2;
            int c = (sum - dif) / 2;
            if(!(0 <= r && r < N && 0 <= c && c < N)){
                continue;
            }
            if(usedDif.count(dif)) continue;
            int parity = sum % 2;
            G[parity].add_edge((sum - parity) / 2, N + (dif - lo[parity]) / 2);
        }
    }
    rep(p, 2){
        int mm = G[p].bipartite_matching();
        y += mm;
        rep(i, N){
            if(G[p].match[i] != -1){
                int sum = i * 2 + p;
                int dif = (G[p].match[i] - N) * 2 + lo[p];
                int r = (sum + dif) / 2;
                int c = (sum - dif) / 2;
                after[r][c] |= 2;
            }
        }
    }

    const char cs[5] = "!x+o";
    vector<pair<char,pair<int,int>>> ans;
    rep(i, N){
        rep(j, N){
            if(after[i][j] > before[i][j]){
                ans.eb(cs[after[i][j]], mp(i+1, j+1));
            }
        }
    }

    cout << y << " " << sz(ans) << endl;
    for(auto p: ans){
        cout << p.fir << " " << p.sec.fir << " " << p.sec.sec << endl;
    }
}


int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    rep(num, 1, T+1){
        cout << "Case #" << num << ": ";
        solve();
    }
}

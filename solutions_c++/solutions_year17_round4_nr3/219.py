#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

struct tsat {
    int n;
    vector < vector<int> > g, gt;
    vector<bool> used;
    vector<int> order, comp;
    vector<int> ass;

    void init(int _n) {
        n = _n;
        g.clear();
        gt.clear();
        used.clear();
        order.clear();
        comp.clear();
        g.resize(n);
        gt.resize(n);
    }

    void aor(int i, int j) {
        g[i^1].push_back(j);
        g[j^1].push_back(i);
        gt[i].push_back(j^1);
        gt[j].push_back(i^1);
    }

    void dfs1 (int v) {
        used[v] = true;
        for (size_t i=0; i<g[v].size(); ++i) {
            int to = g[v][i];
            if (!used[to])
                dfs1 (to);
        }
        order.push_back (v);
    }

    void dfs2 (int v, int cl) {
        comp[v] = cl;
        for (size_t i=0; i<gt[v].size(); ++i) {
            int to = gt[v][i];
            if (comp[to] == -1)
                dfs2 (to, cl);
        }
    }

    bool clc() {
        used.assign (n, false);
        for (int i=0; i<n; ++i)
            if (!used[i])
                dfs1 (i);

        comp.assign (n, -1);
        for (int i=0, j=0; i<n; ++i) {
            int v = order[n-i-1];
            if (comp[v] == -1)
                dfs2 (v, j++);
        }

        for (int i=0; i<n; ++i)
            if (comp[i] == comp[i^1]) {
                return false;
            }
        ass.resize(n);
        for (int i=0; i<n; ++i) {
            int ans = comp[i] > comp[i^1] ? i : i^1;
            ass[i] = ans;
        }
        return true;
    }
} ts;

int dy[] = {-1,0,1,0};
int dx[] = {0,1,0,-1};
int h, w;
char g[55][55];

int fsdr[] = {1,0,3,2};
int bsdr[] = {3,2,1,0};

tuple<int,int,int> clcnxt(int y, int x, int dr, bool cont=false) {
    if (y < 0 || y >= h || x < 0 || x >= w) return {-1,-1,-1};
    if (g[y][x] == '#') return {-1,-1,-1};
    int ndr;
    if (g[y][x] == '/') {
        ndr = fsdr[dr];
    } else if (g[y][x] == '\\') {
        ndr = bsdr[dr];
    } else if (cont) {
        ndr = dr;
    } else {
        return {y,x,dr};
    }
    int ny = y + dy[ndr];
    int nx = x + dx[ndr];
    return clcnxt(ny, nx, ndr);
}

vector<tuple<int,int,int> > path;

void trpath(int y, int x, int dr, bool cont=false) {
    if (y == -1) return;
    if (g[y][x] == '#') return;
    path.emplace_back(y,x,dr);
    if (g[y][x] == '-' && !cont) return;
    auto nk = clcnxt(y,x,dr,true);
    int ny, nx, ndr; tie(ny, nx, ndr) = nk;
    trpath(ny, nx, ndr);
}

int gvr(int y, int x, int dr) {
    if (dr % 2 == 0) {
        return (y*w+x)*4;
    } else {
        return (y*w+x)*4+2;
    }
}

bool vld[4*55*55];

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d %d", &h, &w);
        FO(y,0,h) scanf(" %s", g[y]);
        FO(y,0,h) FO(x,0,w) if (g[y][x] == '|') g[y][x] = '-';

        ts.init(4*h*w);
        memset(vld, 0, sizeof vld);

        FO(y,0,h) FO(x,0,w) if (g[y][x] == '-') {
            FO(i,0,2) {
                vector<tuple<int,int,int> > tmp;
                for (int j = i; j < 4; j += 2) {
                    path.clear();
                    trpath(y,x,j,true);
                    int ly, lx, ldr;
                    tie(ly,lx,ldr) = path.back();
                    if (sz(path) > 1 && g[ly][lx] == '-') goto novert;
                    for (auto u : path) tmp.push_back(u);
                }

                for (auto c : tmp) {
                    int cy, cx, cdr;
                    tie(cy,cx,cdr) = c;
                    int v0 = gvr(cy, cx, cdr);
                    vld[v0] = true;
                }
novert:;
            }
        }

        FO(y,0,h) FO(x,0,w) {
            if (g[y][x] == '-' || g[y][x] == '.') {
                FO(d,0,4) {
                    int v0 = gvr(y,x,d);
                    if (!vld[v0]) {
                        ts.aor(v0^1, v0^1);
                    }
                }
            }
            int v0 = gvr(y,x,0);
            int v1 = gvr(y,x,1);
            ts.aor(v0,v1);
            if (g[y][x] == '-') {
                ts.aor(v0^1,v1^1);
            }
        }
        
        FO(y,0,h) FO(x,0,w) if (g[y][x] == '-' || g[y][x] == '.') {
            tuple<int,int,int> nk[4];
            FO(i,0,4) nk[i] = clcnxt(y, x, i, true);
            FO(i,0,4) {
                int ny, nx, ndr;
                tie(ny,nx,ndr) = nk[i];
                if (ny != -1) {
                    int v0 = gvr(y,x,i);
                    int v1 = gvr(ny,nx,ndr);
                    ts.aor(v0^1, v1);
                }
            }
        }

        if (!ts.clc()) {
            printf("Case #%d: IMPOSSIBLE\n", Z);
        } else {
            printf("Case #%d: POSSIBLE\n", Z);
            FO(y,0,h) FO(x,0,w) if (g[y][x] == '-') {
                int v0 = gvr(y,x,0);
                if (ts.ass[v0] == v0) {
                    g[y][x] = '|';
                } else {
                    g[y][x] = '-';
                }
            }
            FO(y,0,h) printf("%s\n", g[y]);
        }
        fflush(stdout);
    }
}


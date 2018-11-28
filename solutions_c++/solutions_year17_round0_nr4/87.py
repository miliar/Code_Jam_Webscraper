#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#define MAXN 110

using namespace std;

int n,m;
char g[MAXN][MAXN];
bool rr[MAXN],cc[MAXN],d1[2*MAXN],d2[2*MAXN];
vector<int> e[2*MAXN];
int prv[2*MAXN],match[2*MAXN];
bool vis[2*MAXN];
char add[MAXN][MAXN];

bool dfs(int u) {
    if (vis[u]) return 0;
    vis[u] = 1;
    for (int v : e[u]) {
        if (prv[v] == 0) {
            prv[v] = u;
            match[u] = v;
            return 1;
        } else if (dfs(prv[v])) {
            prv[v] = u;
            match[u] = v;
            return 1;
        }
    }
    return 0;
}

int mm() {
    int res = 0;
    for (int i = 2; i <= n+n; i++) {
        memset(vis,0,sizeof(vis));
        if (dfs(i)) res++;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        memset(g,0,sizeof(g));
        memset(rr,0,sizeof(rr));
        memset(cc,0,sizeof(cc));
        memset(d1,0,sizeof(d1));
        memset(d2,0,sizeof(d2));
        memset(prv,0,sizeof(prv));
        memset(match,0,sizeof(match));
        for (int i = 0; i < 2*MAXN; i++) e[i].clear();
        memset(add,0,sizeof(add));

        cin >> n >> m;

        int score = 0;
        for (int i = 0; i < m; i++) {
            char ch;
            int r,c;
            cin >> ch >> r >> c;
            g[r][c] = ch;

            if (ch == 'x' || ch == 'o') {
                rr[r] = 1;
                cc[c] = 1;
                score++;
            }
            if (ch == '+' || ch == 'o') {
                d1[r+c] = 1;
                d2[r-c+MAXN] = 1;
                score++;
            }
        }

        vector<int> rs,cs;
        for (int r = 1; r <= n; r++) if (!rr[r]) rs.push_back(r);
        for (int c = 1; c <= n; c++) if (!cc[c]) cs.push_back(c);

        score += rs.size();
        vector<pair<char,pair<int,int> > > ans;
        for (int i = 0; i < rs.size(); i++) {
            int r = rs[i], c = cs[i];
            if (g[r][c]) add[r][c] = 'o';
            else add[r][c] = 'x';
        }

        for (int r = 1; r <= n; r++) {
            for (int c = 1; c <= n; c++) {
                int x = r+c, y = r-c+MAXN;
                if (d1[x] || d2[y]) continue;
                e[x].push_back(y);
            }
        }

        score += mm();
        for (int x = 2; x <= n+n; x++) {
            int y = match[x];
            if (y == 0) continue;
            int r = (x + y-MAXN) / 2;
            int c = x - r;
            if (g[r][c] || add[r][c]) add[r][c] = 'o';
            else add[r][c] = '+';
        }

        for (int r = 1; r <= n; r++) {
            for (int c = 1; c <= n; c++) {
                if (add[r][c]) ans.push_back(make_pair(add[r][c], make_pair(r,c)));
            }
        }

        cout << "Case #" << TC << ": ";
        cout << score << ' ' << ans.size() << '\n';
        for (auto &p : ans) {
            cout << p.first << ' ' << p.second.first << ' ' << p.second.second << '\n';
        }
    }
}

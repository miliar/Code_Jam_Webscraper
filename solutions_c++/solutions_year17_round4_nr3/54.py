#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>

 
using namespace std; 
 
typedef long long ll; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  
//const long double eps = 1e-5;
//const int INF = 50000;
//const int N = 1000 * 1000 * 1000 + 10;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
vector<string> a;
vector<vector<vector<int> > > forbid;
vector<vector<pii> > sat2;
int r, c;
vector<vector<int> > g, invg;
bool solveSat2(vector<int>& res);
bool isValid(int x, int y) {
    return (x >= 0) && (y >= 0) && (x < r) && (y < c);
}

void prop(int d, int x, int y) {
    if (!isValid(x, y))
        return;
    //cerr << d << " " << x << " " << y << "\n";

    int opd = (d + 2) % 4;
    if (forbid[x][y][opd])
        return;
    if (a[x][y] == '#')
        return;
    forbid[x][y][opd] = 1;
    if (a[x][y] == '.') {
        prop(d, x + dx[d], y + dy[d]);
        return;
    }
    if (a[x][y] == '\\') {
        int dd = d ^ 3;
        prop(dd, x + dx[dd], y + dy[dd]);
        return;
    }
    if (a[x][y] == '/') {
        int dd = d ^ 1;
        prop(dd, x + dx[dd], y + dy[dd]);
        return;
    }
    return;
}


void prop(int d, int x, int y, int id) {
    if (!isValid(x, y))
        return;
    if (a[x][y] == '#')
        return;
    if (a[x][y] == '.') {
        if (sat2[x][y].first == -1)
            sat2[x][y].first = id;
        else
            sat2[x][y].second = id;
        prop(d, x + dx[d], y + dy[d], id);
        return;
    }
    if (a[x][y] == '\\') {
        int dd = d ^ 3;
        prop(dd, x + dx[dd], y + dy[dd], id);
        return;
    }
    if (a[x][y] == '/') {
        int dd = d ^ 1;
        prop(dd, x + dx[dd], y + dy[dd], id);
        return;
    }
    return;
}

void solve() {
    cin >> r >> c;
    a.resize(r);
    for (int i = 0; i < r; ++i)
        cin >> a[i];
    forbid.assign(r, vector<vector<int> >(c, vector<int>(4, 0)));
    sat2.assign(r, vector<pii>(c, pii(-1, -1)));
    vector<pii> las;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if ((a[i][j] == '-') || (a[i][j] == '|')) {
                las.emplace_back(i, j);
            }
        }
    }
    for (int lasId = 0; lasId < las.size(); ++lasId) {
        for (int d = 0; d < 4; ++d) {
            prop(d, las[lasId].first + dx[d], las[lasId].second + dy[d]);
        }
    }
    bool pos = 1;
    vector<int> res(las.size(), -1);
    for (int i = 0; i < las.size(); ++i) {
        if (((forbid[las[i].first][las[i].second][0]) || (forbid[las[i].first][las[i].second][2]))
            && ((forbid[las[i].first][las[i].second][1]) || (forbid[las[i].first][las[i].second][3]))) {
            pos = 0;
            break;
        }
        if ((forbid[las[i].first][las[i].second][0]) || (forbid[las[i].first][las[i].second][2])) {
            a[las[i].first][las[i].second] = '-';
            res[i] = 0;
        }
        if ((forbid[las[i].first][las[i].second][1]) || (forbid[las[i].first][las[i].second][3])) {
            a[las[i].first][las[i].second] = '|';
            res[i] = 1;
        }
    }
    if (!pos) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    for (int lasId = 0; lasId < las.size(); ++lasId) {
        if (res[lasId] == 1) {
            prop(0, las[lasId].first + dx[0], las[lasId].second + dy[0], 2 * lasId + 1);
            prop(2, las[lasId].first + dx[2], las[lasId].second + dy[2], 2 * lasId + 1);
        }
        if (res[lasId] == 0) {
            prop(1, las[lasId].first + dx[1], las[lasId].second + dy[1], 2 * lasId);
            prop(3, las[lasId].first + dx[3], las[lasId].second + dy[3], 2 * lasId);
        }
        if (res[lasId] == -1) {
            prop(0, las[lasId].first + dx[0], las[lasId].second + dy[0], 2 * lasId + 1);
            prop(2, las[lasId].first + dx[2], las[lasId].second + dy[2], 2 * lasId + 1);
            prop(1, las[lasId].first + dx[1], las[lasId].second + dy[1], 2 * lasId);
            prop(3, las[lasId].first + dx[3], las[lasId].second + dy[3], 2 * lasId);
        }        
    }
    bool ok = solveSat2(res);

    if (!ok) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    else {
        cout << "POSSIBLE\n";
    }
    for (int i = 0; i < las.size(); ++i) {
        if (res[i])
            a[las[i].first][las[i].second] = '|';
        else
            a[las[i].first][las[i].second] = '-';
    }
    for (int i = 0; i < r; ++i) {
        cout << a[i] << endl;
    }
}

vector<bool> used;
vector<int> order, comp;

void dfs1(int v) {
    used[v] = true;
    for (int i = 0; i < g[v].size(); ++i) {
        int to = g[v][i];
        if (!used[to])
            dfs1(to);
    }
    order.push_back(v);
}

void dfs2(int v, int cl) {
    comp[v] = cl;
    for (int i = 0; i < invg[v].size(); ++i) {
        int to = invg[v][i];
        if (comp[to] == -1)
            dfs2(to, cl);
    }
}

bool solveSat2(vector<int>& res) {
    int n = 2 * res.size();
    g.clear();
    g.resize(n);
    invg.clear();
    invg.resize(n);
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (a[i][j] != '.')
                continue;
            if (sat2[i][j].first == -1)
                return 0;
            if (sat2[i][j].second == -1) {
                g[sat2[i][j].first ^ 1].push_back(sat2[i][j].first);
                invg[sat2[i][j].first].push_back(sat2[i][j].first ^ 1);
                continue;
            }
            g[sat2[i][j].first ^ 1].push_back(sat2[i][j].second);
            g[sat2[i][j].second ^ 1].push_back(sat2[i][j].first);
            invg[sat2[i][j].first].push_back(sat2[i][j].second ^ 1);
            invg[sat2[i][j].second].push_back(sat2[i][j].first ^ 1);
        }
    }
    order.clear();
    comp.assign(n, -1);
    used.assign(n, 0);
    
    for (int i = 0; i < n; ++i)
        if (!used[i])
            dfs1(i);

    for (int i = 0, j = 0; i < n; ++i) {
        int v = order[n - i - 1];
        if (comp[v] == -1)
            dfs2(v, j++);
    }

    for (int i = 0; i < n; ++i)
        if (comp[i] == comp[i ^ 1]) 
            return 0;
        
    for (int i = 0; i < n; ++i) {
        if (res[i / 2] == -1)
            res[i / 2] = (comp[i] < comp[i ^ 1]);
    }
    return 1;
    

}

int main() {
    //freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
		std::cerr << i << endl;
	}
	return 0;
}
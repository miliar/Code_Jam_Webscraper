#include <bits/stdc++.h>

using namespace std;

#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

typedef long long LL;

const int hi[] = {0,0,-1,1};
const int hj[] = {-1,1,0,0};

const int N = 105;
const int M = N*N;

int n, m, counter;
char s[N][N];
int sh[N][N], xx[M], yy[M], com[M];
bool mark[M];
vector<int> ke[M], nguoc[M];
stack<int> st;
vector<pair<int,int>> must[M];
bool res[M][2];

bool di_thu(int bd, bool hh) {
    queue<pair<pair<int,int>,int>> q;
    while (!q.empty()) q.pop();
    if (hh) {
        q.push({{xx[bd],yy[bd]},2});
        q.push({{xx[bd],yy[bd]},3});
    }
    else {
        q.push({{xx[bd],yy[bd]},0});
        q.push({{xx[bd],yy[bd]},1});
    }
    vector<int> vx;
    vx.clear();
    while (!q.empty()) {
        int i = q.front().first.first;
        int j = q.front().first.second;
        int hg = q.front().second;
        q.pop();
        
        //cout << i << ' ' << j << ' ' << hg << '\n';

        i += hi[hg];
        j += hj[hg];
        
        if (sh[i][j] < 0) continue;
        if (s[i][j] == '/') {
            hg = 3-hg;
        }
        else if (s[i][j] == '\\') {
            hg ^= 2;
        }
        else
        if (s[i][j] != '.') {
            return false;
        }
        else {
            vx.push_back(sh[i][j]);
        }
        //cout << "to " << i << ' ' << j << ' ' << hg << "\n";
        q.push({{i,j},hg});
    }
    for (auto &p : vx) must[p].push_back({bd,(hh?1:0)});
    return true;
}

void dfs1(int u) {
    mark[u] = true;
    for (auto &v : ke[u]) {
        if (!mark[v]) {
            dfs1(v);
        }
    }
    st.push(u);
}

void dfs2(int u) {
    mark[u] = true;
    for (auto &v : nguoc[u]) {
        if (!mark[v]) {
            dfs2(v);
        }
    }
    com[u] = counter;
}

bool getans() {
    while (!st.empty()) st.pop();

    scanf("%d%d", &n, &m);

    int dem_laser = 0, dem_trong = 0;
    for (int j = 1; j <= m; j++) {
        sh[0][j] = sh[n+1][j] = -1;
    }
    for (int i = 1; i <= n; i++) {
        scanf("%s", s[i]+1);
        for (int j = 1; j <= m; j++) {
            sh[i][j] = 0;
            if (s[i][j] == '.' || s[i][j] == '|' || s[i][j] == '-') {
                if (s[i][j] != '.') {
                    s[i][j] = '+';
                    sh[i][j] = ++dem_laser;
                    xx[dem_laser] = i; yy[dem_laser] = j;
                }
                else {
                    sh[i][j] = ++dem_trong;
                    must[dem_trong].clear();
                }
            }
            else if (s[i][j] == '#') sh[i][j] = -1;
        }
        sh[i][0] = sh[i][m+1] = -1;
    }

    int sz = dem_laser * 2;
    for (int i = 1; i <= sz; i++) {
        ke[i].clear();
        nguoc[i].clear();
    }

    for (int p = 1; p <= dem_laser; p++) {
        bool ok_false = di_thu(p,false);
        bool ok_true = di_thu(p,true);
        if (!ok_false && !ok_true) return false;
        res[p][0] = ok_false;
        res[p][1] = ok_true;
    }

    for (int i = 1; i <= dem_trong; i++) {
        if (must[i].empty()) return false;
        int a1 = 0, a2 = 0, b1 = 0, b2 = 0;
        for (auto &p : must[i]) {
            if (a1 == 0) a1 = p.first;
            else if (a1 != p.first) a2 = p.first;
            if (a1 == p.first) b1 |= (1<<p.second);
            if (a2 == p.first) b2 |= (1<<p.second); 
        }

        if (b1 >= 3 || b2 >= 3) {
            continue;
        }

        b1--; b2--;

        if (a2 == 0) {
            if (res[a1][b1] == false) {
                return false;
            }
            res[a1][1-b1] = false;
            continue;
        }

        if (res[a1][b1] == false && res[a2][b2] == false) return false;

        if (res[a1][b1] == false) {
            res[a2][1-b2] = false;
            continue;
        }
        if (res[a2][b2] == false) {
            res[a1][1-b1] = false;
            continue;
        }
        
        ke[a1*2+1-b1-1].push_back(a2*2+b2-1);
        ke[a2*2+1-b2-1].push_back(a1*2+b1-1);
    }

    for (int i = 1; i <= dem_laser; i++) {
        if (res[i][0] == false && res[i][1] == false) return false;
        if (res[i][0] == false) ke[i*2-1].push_back(i*2);
        else if (res[i][1] == false) ke[i*2].push_back(i*2-1);
    }

    for (int i = 1; i <= sz; i++) {
        for (auto &j : ke[i]) {
            nguoc[j].push_back(i);
        }
        mark[i] = false;
    }

    while (!st.empty()) st.pop();

    for (int i = 1; i <= sz; i++)
        if (!mark[i]) dfs1(i);

    counter = 0;

    for (int i = 1; i <= sz; i++) mark[i] = false;

    while (!st.empty()) {
        int v = st.top();
        st.pop();
        if (!mark[v]) {
            ++counter;
            dfs2(v);
        }
    }

    for (int i = 1; i <= dem_laser; i++) {
        if (com[i*2-1] == com[i*2]) return false;
        if (com[i*2-1] > com[i*2]) s[xx[i]][yy[i]] = '-';
        else s[xx[i]][yy[i]] = '|';
    }

    return true;
}

void solve(int nt) {
    bool ok = getans();
    printf("Case #%d: %s\n", nt, (ok?"POSSIBLE":"IMPOSSIBLE"));

    if (ok) {
        for (int i = 1; i <= n; i++) {
            printf("%s\n", s[i]+1);
        }
    }
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
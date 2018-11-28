#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>
#include <functional>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long long llong;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
        cerr << (*i) << " ";
    }
    cerr << "\n";
}
const int MX = 5000;

int n, m;
vector<int> go[MX];
vector<int> vv;
vector<int> vv2;
int was[MX * 2];
vector<int> eds[MX * 2];
vector<int> beds[MX * 2];
string s[60];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int en[MX * 2];

int ch(int x, int y, int d) {
    if (x < 0 || x >= n || y < 0 || y >= m)
        return 1;
    if (s[x][y] == '#')
        return 1;
    if (s[x][y] == '-' || s[x][y] == '|')
        return 0;
    if (s[x][y] == '/') {
        d ^= 1;
        return ch(x + dx[d], y + dy[d], d);
    }
    else if (s[x][y] == '\\') {
        d = 3 - d;
        return ch(x + dx[d], y + dy[d], d);
    }
    else {
        return ch(x + dx[d], y + dy[d], d);
    }
}

void gg(int x, int y, int d, int k) {
    if (x < 0 || x >= n || y < 0 || y >= m)
        return;
    if (s[x][y] == '#')
        return;
    if (s[x][y] == '-' || s[x][y] == '|')
        return;
    if (s[x][y] == '/') {
        d ^= 1;
        gg(x + dx[d], y + dy[d], d, k);
    }
    else if (s[x][y] == '\\') {
        d = 3 - d;
        gg(x + dx[d], y + dy[d], d, k);
    }
    else {
        go[x * m + y].push_back(k);
        gg(x + dx[d], y + dy[d], d, k);
    }

}

void dfs1(int v) {
    was[v] = 1;
    for (int u: eds[v])
        if (!was[u])
            dfs1(u);
    vv2.push_back(v);
}

void dfs2(int v) {
    was[v] = 1;
    vv.push_back(v);
    for (int u: beds[v])
        if (!was[u])
            dfs2(u);
}

int ng(int x) {
    if (x >= n * m)
        return x - n * m;
    else
        return x + n * m;
}

int enbl(int x) {
    en[x] = 1;
    was[x] = 1;
    en[ng(x)] = 0;
    was[ng(x)] = 1;
    for (int u: eds[x]) {
        if (was[u]) {
            if (!en[u])
                return 0;
        }
        else {
            if (!enbl(u))
                return 0;
        }
    }
    return 1;
}

int bl[MX * 2];
void print() {
    /*for (int i = 0; i < n; ++i)
        cerr << s[i] << "\n";
    cerr << "\n";*/
}

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> s[i];
    for (int i = 0; i < n * m; ++i)
        go[i].clear();
    for (int i = 0; i < 2 * n * m; ++i)
        bl[i] = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (s[i][j] == '|' || s[i][j] == '-') {
                if (ch(i - 1, j, 0) && ch(i + 1, j, 2)) {
                    gg(i - 1, j, 0, i * m + j);
                    gg(i + 1, j, 2, i * m + j);
                }
                else {
                    bl[i * m + j] = 1;
                }
                if (ch(i, j - 1, 3) && ch(i, j + 1, 1)) {
                    gg(i, j - 1, 3, i * m + j + n * m);
                    gg(i, j + 1, 1, i * m + j + n * m);
                }
                else {
                    bl[i * m + j + n * m] = 1;
                }
            }
        }
    for (int i = 0; i < n * m; ++i)
        if (bl[i] && bl[i + n * m]) {
            cout << "IMPOSSIBLE\n";
                print();
            return;
        }
    for (int i = 0; i < 2 * n * m; ++i)
        eds[i].clear();
    for (int i = 0; i < 2 * n * m; ++i)
        beds[i].clear();
    for (int i = 0; i < n * m; ++i)
        assert(go[i].size() <= 2);
    for (int i = 0; i < n * m; ++i) {
        if (bl[i]) {
            eds[i].push_back(ng(i));
            beds[ng(i)].push_back(i);
        }
        if (bl[i + n * m]) {
            eds[i + n * m].push_back(i);
            beds[i].push_back(ng(i));
        }
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (s[i][j] == '.' && go[i * m + j].empty()) {
                cout << "IMPOSSIBLE\n";
                print();
                return;
            }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (s[i][j] == '.') {
                if (go[i * m + j].size() == 1) {
                    int k = go[i * m + j][0];
                    eds[ng(k)].push_back(k);
                    beds[k].push_back(ng(k));
                }
                else {
                    int k = go[i * m + j][0];
                    int l = go[i * m + j][1];
                    eds[ng(k)].push_back(l);
                    eds[ng(l)].push_back(k);
                    beds[k].push_back(ng(l));
                    beds[l].push_back(ng(k));
                }
            }
    vv.clear();
    vv2.clear();
    memset(was, 0, sizeof(was));
    for (int i = 0; i < 2 * n * m; ++i)
        if (!was[i])
            dfs1(i);
    reverse(vv2.begin(), vv2.end());
    memset(was, 0, sizeof(was));
    for (int i: vv2)
        if (!was[i])
            dfs2(i);
    reverse(vv.begin(), vv.end());
    for (int i = 0; i < 2 * n * m; ++i)
        en[i] = 0, was[i] = 0;
    for (int i: vv) {
        if (!was[i]) {
            if (!enbl(i)) {
                cout << "IMPOSSIBLE\n";
                print();
                return;
            }
        }
    }
    cout << "POSSIBLE\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (s[i][j] != '-' && s[i][j] != '|')
                cout << s[i][j];
            else if (en[i * m + j])
                cout << "|";
            else
                cout << "-";
        }
        cout << "\n";
    }
}

int main() {
    int tt;
    cin >> tt;
    for (int i = 0; i < tt; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}



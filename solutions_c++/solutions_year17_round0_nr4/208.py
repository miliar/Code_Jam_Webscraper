// (text-heavy) epiphany code!  aka the measure of a man, part three
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
using namespace std;
#define rep(i,a,n) for (int i=a;i<(int)(n);i++)
#define per(i,a,n) for (int i=(n)-1;i>=(int)(a);i--)
template<typename T> ostream& operator<<(ostream& s, vector<T> t) {rep(i, 0, t.size()) s << (i ? " " : "") << t[i]; return s;}
template<typename T> istream& operator>>(istream& s, vector<T> &t) {rep(i, 0, t.size()) s >> t[i]; return s;}
template<typename T, typename U> ostream& operator<<(ostream& s, pair<T, U> t) {s << "(" << t.first << "," << t.second << ")"; return s;}
template<typename T, typename U> istream& operator>>(istream& s, pair<T, U> &t) {s >> t.first >> t.second; return s;}
typedef long long ll;

const int N = 111;

bool oR[N][N], oD[N][N], r[N][N], d[N][N], done[N][N];

int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};

void solve() {
    memset(oR, 0, sizeof(oR)), memset(oD, 0, sizeof(oD));
    memset(r, 0, sizeof(r)), memset(d, 0, sizeof(d));
    memset(done, 0, sizeof(done));
    int n, m;
    cin >> n >> m;
    rep(i, 0, m) {
        char type;
        int x, y;
        cin >> type >> x >> y;
        x--, y--;
        if (type != '+') {
            r[x][y] = true;
            oR[x][y] = true;
        }
        if (type != 'x') {
            d[x][y] = true;
            oD[x][y] = true;
        }
    }
    rep(i, 0, n) rep(j, 0, n) {
        bool can = true;
        rep(k, 0, n) if (r[i][k] || r[k][j]) can = false;
        if (can) r[i][j] = true;
    }
    
    auto inBounds = [n](int x) {
        return x >= 0 && x < n;
    };
    
    auto add = [&](int i, int j) {
        bool can = true;
        rep(k, -n, n) {
            if ((inBounds(i + k) && inBounds(j + k) && d[i + k][j + k]) ||
                    (inBounds(i + k) && inBounds(j - k) && d[i + k][j - k])) {
                can = false;
            }
        }
        if (can) d[i][j] = true;
    };
    auto canGo = [&](int i, int j) {
        return inBounds(i) && inBounds(j) && !done[i][j];
    };
    int ci = 0, cj = 0, cd = 0;
    rep(it, 0, n * n) {
        //cout << ci << " " << cj << endl;
        add(ci, cj);
        if (!canGo(ci + dx[cd], cj + dy[cd])) cd = (cd + 1) % 4;
        done[ci][cj] = true;
        ci += dx[cd];
        cj += dy[cd];
    }
    //rep(i, 0, n) {rep(j, 0, n) cout << r[i][j]; cout << endl;}
    
    vector<pair<char, pair<int, int>>> res;
    int val = 0;
    rep(i, 0, n) rep(j, 0, n) {
        val += r[i][j] + d[i][j];
        if (oR[i][j] != r[i][j] || oD[i][j] != d[i][j]) {
            char ch = '.';
            if (r[i][j] && d[i][j]) {
                ch = 'o';
            } else if (r[i][j]) {
                ch = 'x';
            } else if (d[i][j]) {
                ch = '+';
            }
            if (ch != '.') {
                res.push_back({ch, {i + 1, j + 1}});
            }
        }
    }
    cout << val << " " << res.size() << endl;
    for (auto x : res) {
        cout << x.first << " " << x.second.first << " " << x.second.second << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
    }
}

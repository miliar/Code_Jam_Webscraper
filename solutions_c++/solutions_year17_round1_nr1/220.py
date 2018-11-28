#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fi first
#define se second
#define pb push_back
#define MP make_pair

typedef pair<int,int> PII;
typedef vector<int> VI;

int m, n;
string a[33];
char c[33][33][33][33];
char d[33][33];
int F[33][33][33][33];

bool solve(int i, int j, int u, int v) {
    if (u < i || v < j) return true;
    int &res = F[i][j][u][v];
    if (res != -1) return res;
    For(x, i, u) For(y, j, v) if (c[x][y][u][v] != ' ') {
        if (solve(i, y, x - 1, v) && solve(i, j, u, y - 1)) res = 1;
        if (solve(i, j, x - 1, v) && solve(x, j, u, y - 1)) res = 1;
    }
    return res;
}

void trace(int i, int j, int u, int v) {
    if (u < i || v < j) return;
    For(x, i, u) For(y, j, v) if (c[x][y][u][v] != ' ') {
        if (solve(i, y, x - 1, v) && solve(i, j, u, y - 1)) {
            trace(i, y, x - 1, v);
            trace(i, j, u, y - 1);
            For(p, x, u) For(q, y, v) d[p][q] = c[x][y][u][v];
            return;
        }
        if (solve(i, j, x - 1, v) && solve(x, j, u, y - 1)) {
            trace(i, j, x - 1, v);
            trace(x, j, u, y - 1);
            For(p, x, u) For(q, y, v) d[p][q] = c[x][y][u][v];
            return;
        }
    }
}

int main() {
    int nt;
    cin >> nt;
    Rep(t, nt) {
        cin >> m >> n;
        Rep(i,m) cin >> a[i];
        Rep(i, m) Rep(j, n) Rep(u, m) Rep(v, n) c[i][j][u][v] = ' ';
        Rep(i, m) Rep(j, n) For(u, i, m-1) For(v, j, n-1) {
            char cc = ' ';
            int count = 0;
            For(x, i, u) For(y, j, v) if (a[x][y] != '?') {
                ++count;
                cc = a[x][y];
            }
            if (count == 1) c[i][j][u][v] = cc;
        }

        memset(F, 255, sizeof(F));
        bool b = solve(0, 0, m - 1, n - 1);
        if (!b) {
            cout << "WRONG WRONG WRONG" << endl;
        }
        trace(0, 0, m - 1, n - 1);

        cout << "Case #" << (t + 1) << ":" << endl;
        Rep(i, m) {
            Rep(j, n) cout << d[i][j];
            cout << endl;
        }
    }
    return 0;
}

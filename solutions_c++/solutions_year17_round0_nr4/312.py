#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

typedef long long int64 ;
typedef unsigned long long uint64 ;
typedef pair<int, int> pint ;
typedef pair<int64, int64> pint64 ;
typedef vector<int> vint ;

#define px first
#define py second

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define REPD(i, n) for (int i = (n) ; i >= 0 ; i --)
#define FOR(i, a, b) for (int i = (a) ; i < (b) ; i ++)
#define FORD(i, a, b) for (int i = (a) ; i >= (b) ; i --)

#define MUL64(x, y) (((int64) (x)) * ((int64) (y)))
#define MULMOD(x, y, modul) (MUL64(x, y) % modul)
#define MUL(x, y) MULMOD(x, y, modul)
#define ADD(reg, val) { reg += val ; if (reg >= modul) reg -= modul ; }

#define SET(v, val) memset(v, val, sizeof(v)) ;
#define SIZE(v) ((int) (v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) { sort(ALL(v)) ; }
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }

#define MAXN 555
#define DELTA 250

#define FIRST_DIAG(r, c) ((r) + (c))
#define SECOND_DIAG(r, c) (DELTA + (r) - (c))

#define IX 1
#define PLUS 2
#define OX 3

bool dfs(int n, int m, vector<vector<int> >& e, int match[MAXN], int prev[MAXN], bool vis[MAXN], int u) {
    vis[u] = true;
    REP(i, SIZE(e[u])) {
        int v = e[u][i];
        if (prev[v] == -1 || (!vis[prev[v]] && dfs(n, m, e, match, prev, vis, prev[v]))) {
            prev[v] = u;
            match[u] = v;
            return true;
        }
    }
    return false;
}

int maxMatching(int n, int m, vector<vector<int> >& e, int match[MAXN], int prev[MAXN]) {
    int ret = 0;
    REP(u, n) { if (match[u] != -1) e[u].clear(); ret++; }
    bool vis[MAXN];
    REP(u, n) {
        if (match[u] == -1) {
            REP(v, n) vis[v] = false;
            if (dfs(n, m, e, match, prev, vis, u)) {
                ret++;
            }
        }
    }
    return ret;
}

int main() {
    int numTests ;
    cin >> numTests ;

    int n, m;
    FOR(test, 1, numTests + 1) {
        cin >> n >> m;

        int matchRow[MAXN], prevRow[MAXN], matchDiag[MAXN], prevDiag[MAXN];
        vector<vector<int> > erow, ediag;
        char init[MAXN][MAXN] = {0};
        REP(u, MAXN) {
            matchRow[u] = -1; prevRow[u] = -1;
            matchDiag[u] = -1; prevDiag[u] = -1;
        }
        REP(u, n) {
            erow.push_back(vector<int>());
            REP(v, n) erow[u].push_back(v);
        }
        REP(u, 2*n-1) {
            ediag.push_back(vector<int>());
            FOR(v, -n+1, n) {
                int id = DELTA+v;
                int r = (u+v), c = (u-v);

                if ((r%2 == 0) && (c%2 ==0)) {
                    r /= 2; c /= 2;
                    if (r >= 0 && r < n && c >= 0 && c < n) {
                        ediag[u].push_back(id);
                    }
                }
            }
        }
        REP(i, m) {
            string s;
            int r, c;

            cin >> s >> r >> c;
            r--; c--;
            init[r][c] = s[0];
            if (s == "o" || s == "x") {
                matchRow[r] = c;
                prevRow[c] = r;
            }
            if (s == "o" || s == "+") {
                matchDiag[FIRST_DIAG(r, c)] = SECOND_DIAG(r, c);
                prevDiag[SECOND_DIAG(r, c)] = FIRST_DIAG(r, c);
            }
        }
        maxMatching(n, n, erow, matchRow, prevRow);
        maxMatching(2*n-1, 2*n-1, ediag, matchDiag, prevDiag);
        int board[MAXN][MAXN] = {0};
        int value = 0;
        int cnt = 0;
        REP(u, n) {
            if (matchRow[u] != -1) {
                board[u][matchRow[u]] = IX;
            }
        }
        REP(u, 2*n-1) {
            if (matchDiag[u] != -1) {
                int r = (u + matchDiag[u] - DELTA) / 2;
                int c = (u - (matchDiag[u] - DELTA)) / 2;
                if (board[r][c] == IX) {
                    board[r][c] = OX;
                }
                if (board[r][c] == 0) {
                    board[r][c] = PLUS;
                }
            }
        }
        REP(r, n) REP(c, n) if (board[r][c] != 0) {
            char ch;
            switch (board[r][c]) {
                case IX: ch = 'x'; value++; break;
                case OX: ch = 'o'; value += 2; break;
                case PLUS: ch = '+'; value++; break;
            }
            if (init[r][c] != ch) {
                cnt++;
            }
        }
        cout << "Case #" << test << ": " << value << " " << cnt << endl;

        REP(r, n) REP(c, n) if (board[r][c] != 0) {
            char ch;
            switch (board[r][c]) {
                case IX: ch = 'x'; break;
                case OX: ch = 'o'; break;
                case PLUS: ch = '+'; break;
                default: init [r][c] = ' ';
            }
            if (init[r][c] != ch) {
                cout << ch << " " << (r+1) << " " << (c+1) << endl;
            }
        }
    }

    return 0;
}

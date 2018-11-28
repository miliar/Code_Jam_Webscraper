#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <tuple>
#define SZ(x) ((int) (x).size())
using namespace std;

typedef long long i64;

const int NMAX = 105;

// Problem 1

int xmat1[NMAX][NMAX];
int mat1[NMAX][NMAX];
bool badRow[NMAX], badCol[NMAX];

int ans = 0;

void clearProblem1(int n) {
    memset(mat1, 0, sizeof mat1);
    memset(xmat1, 0, sizeof xmat1);
    memset(badRow, 0, sizeof badRow);
    memset(badCol, 0, sizeof badCol);
}

void doOp1(int n, int x, int y) {
    ans++;
    xmat1[x][y]++;
    badRow[x] = true;
    badCol[y] = true;
}

void solveProblem1(int n) {
    for (int i = 1, j = 1; i <= n; ++i) {
        if (!badRow[i]) {
            while (badCol[j]) {
                ++j;
            }
            mat1[i][j++]++;
            ans++;
        }
    }
}

// Problem 2
int xmat2[NMAX][NMAX];
int mat2[NMAX][NMAX];

vector<int> G[3 * NMAX];
bool badDiag1[3 * NMAX], badDiag2[3 * NMAX];
int L[3 * NMAX], R[3 * NMAX];
bool used[3 * NMAX];

void clearProblem2(int n) {
    memset(mat2, 0, sizeof mat2);
    memset(xmat2, 0, sizeof xmat2);
    memset(badDiag1, 0, sizeof badDiag1);
    memset(badDiag2, 0, sizeof badDiag2);
    memset(L, 0, sizeof L);
    memset(R, 0, sizeof R);
    for (int i = 1; i <= n + n; ++i) {
        G[i].clear();
    }
}

void doOp2(int n, int x, int y) {
    ans++;
    badDiag1[x + y - 1] = true;
    badDiag2[n + x - y] = true;
    xmat2[x][y]++;
}

bool pairUp(int node) {
    if (used[node]) {
        return false;
    }
    used[node] = true;
    for (int to: G[node]) {
        if (R[to] == 0) {
            L[node] = to;
            R[to] = node;
            return true;
        }
    }
    for (int to: G[node]) {
        if (pairUp(R[to])) {
            L[node] = to;
            R[to] = node;
            return true;
        }
    }
    return false;
}

void solveProblem2(int n) {
    int k = 2 * n - 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            int d1 = i + j - 1;
            int d2 = n + i - j;
            if (!badDiag1[d1] && !badDiag2[d2]) {
                G[d1].push_back(d2);
            }
        }
    }
    for (bool ok = true; ok; ) {
        ok = false;
        memset(used, false, sizeof used);
        for (int i = 1; i <= k; ++i) {
            if (!badDiag1[i] && L[i] == 0) {
                ok |= pairUp(i);
            }
        }
    }
    for (int i = 1; i <= k; ++i) {
        if (!badDiag1[i] && L[i] != 0) {
            ans++;
            int a = i + 1, b = L[i] - n;
            int r = (a + b) / 2;
            int c = (a - b) / 2;
            mat2[r][c]++;
        }
    }
}

struct Operation {
    char type;
    int r, c;
    Operation() = default;
    Operation(char _type, int _r, int _c):
        type(_type), r(_r), c(_c) {}
};

void solve() {
    int n, m;
    cin >> n >> m;

    ans = 0;
    clearProblem1(n);
    clearProblem2(n);

    while (m-- > 0) {
        char op;
        int x, y;
        cin >> op >> x >> y;
        if (op == 'x' || op == 'o') {
            doOp1(n, x, y);
        }
        if (op == '+' || op == 'o') {
            doOp2(n, x, y);
        }
    }
    solveProblem1(n);
    solveProblem2(n);
    vector<Operation> ops;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            int s1 = mat1[i][j] + xmat1[i][j];
            int s2 = mat2[i][j] + xmat2[i][j];
            if (mat1[i][j] || mat2[i][j]) {
                if (s1 && s2) {
                    ops.push_back(Operation('o', i, j));
                } else if (s1) {
                    ops.push_back(Operation('x', i, j));
                } else if (s2) {
                    ops.push_back(Operation('+', i, j));
                }
            }
        }
    }
    cout << ans << ' ' << SZ(ops) << '\n';
    for (const Operation& p: ops) {
        cout << p.type << ' ' << p.r << ' ' << p.c << '\n';
    }
}

int main() {
    #ifdef LOCAL_RUN
    freopen("task.in", "r", stdin);
    freopen("task.out", "w", stdout);
    //freopen("task.err", "w", stderr);
    #endif // ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}

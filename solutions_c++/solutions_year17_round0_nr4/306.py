#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
    if (argc == 1) freopen("input.txt", "r", stdin);
    int tc;
    cin >> tc;
    int l = 1, r = tc;
    if (argc > 1) {
        freopen(argv[2], "w", stdout);
        int n = atoi(argv[1]), i = atoi(argv[2]);
        l = tc / n * i + 1;
        r = i+1<n ? tc/n*(i+1) : tc;
    }
    for (int cs = 1; cs <= tc; cs++) {
        input();
        if (cs >= l && cs <= r) solve(cs);
    }
    return 0;
}

const int N = 512;
int n, m;
int a[N][N];
int b[N][N];

void input() {
    memset(a, 0, sizeof a);
    cin >> n >> m;
    REP(i, m) {
        char c;
        int x, y;
        cin >> c >> x >> y;
        if (c == 'x' || c == 'o') a[x][y] |= 1;
        if (c == '+' || c == 'o') a[x][y] |= 2;
    }
    REP(i, N) REP(j, N) b[i][j] = a[i][j];
}

bool row[N], col[N];

int addRooks() {
    memset(row, 0, sizeof row);
    memset(col, 0, sizeof col);

    int pnts = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) if (b[i][j]&1) {
            pnts++;
            row[i] = true;
            col[j] = true;
        }
    }
    for (int i = 1; i <= n; i++) if (!row[i]) {
        for (int j = 1; j <= n; j++) if (!col[j]) {
            pnts++;
            b[i][j] |= 1;
            row[i] = true;
            col[j] = true;
            break;
        }
    }
    return pnts;
}

int addBishops() {
    memset(row, 0, sizeof row);
    memset(col, 0, sizeof col);

    int pnts = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) if (b[i][j]&2) {
            pnts++;
            row[i+j] = true;
            col[i-j+n] = true;
        }
    }
    vector<int> dgns;
    for (int i = 2; i <= n; i++) {
        dgns.pb(i);
        dgns.pb(2*(n+1) - i);
    }
    dgns.pb(n+1);
    for (int x : dgns) if (!row[x]) {
        for (int y = -n+1; y <= n-1; y++) if (!col[y+n] && (x-y) % 2 == 0) {
            int i = (x+y)/2, j = (x-y)/2;
            if (i < 1 || i > n || j < 1 || j > n) continue;
            pnts++;
            b[i][j] |= 2;
            row[x] = true;
            col[y+n] = true;
            break;
        }
    }
    return pnts;
}

void solve(int cs) {
    cout << "Case #" << cs << ": ";
    int pnts = 0, changes = 0;

    pnts += addRooks();
    pnts += addBishops();
    
    REP(i, N) REP(j, N) if (a[i][j] != b[i][j]) changes++;

    cout << pnts << " " << changes << "\n";
    
    REP(i, N) REP(j, N) if (a[i][j] != b[i][j]) {
        if (b[i][j] == 3) cout << "o ";
        if (b[i][j] == 2) cout << "+ ";
        if (b[i][j] == 1) cout << "x ";
        cout << i << " " << j << "\n";
    }
}


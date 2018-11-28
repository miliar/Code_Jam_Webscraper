#include <bits/stdc++.h>
using namespace std;


const int MAXN = 410;
const int MAXM = 20010;
const int INF = 1e9;

vector<int> G[MAXN];
int cx[MAXN], cy[MAXN];
int dx[MAXN], dy[MAXN];
bool mark[MAXN];
int N;

int searchPath() {
    memset(dx, -1, sizeof(dx));
    memset(dy, -1, sizeof(dy));
    queue<int> Q;
    for (int i = 1; i <= N; i++) if (cx[i] == -1) {
        dx[i] = 0;
        Q.push(i);
    }
    int dist = INF;
    while (!Q.empty()) {
        int u = Q.front(); Q.pop();
        if (dx[u] > dist) break;
        for (int i = 0; i < (int)G[u].size(); i++) {
              int v = G[u][i];
              if (dy[v] == -1) {
                dy[v] = dx[u] + 1;
                if (cy[v] == -1) {
                    dist = dy[v];
                } else {
                    dx[cy[v]] = dy[v] + 1;
                    Q.push(cy[v]);
                }
            }
        }
    }
    return dist != INF;
}

int findPath(int u) {
    for (int i = 0; i < (int)G[u].size(); i++) {
        int v = G[u][i];
        if (!mark[v] && dy[v] == dx[u] + 1) {
            mark[v] = true;
            if (cy[v] == -1 || findPath(cy[v])) {
                cy[v] = u;
                cx[u] = v;
                return 1;
            }
        }
    }
    return 0;
}

int MaxMatch() {
    int res = 0;
    memset(cx, -1, sizeof(cx));
    memset(cy, -1, sizeof(cy));
    while (searchPath()) {
        memset(mark, false, sizeof(mark));
        for (int i = 1; i <= N; i++) {
            if (cx[i] == -1) {
                res += findPath(i);
            }
        }
    }
    return res;
}


// = =============== main function ===========================

char a[110][110], b[110][110];
bool hasxx[MAXN], hasxy[MAXN];
bool haspx[MAXN], haspy[MAXN];
int main(void) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; ++ i) for (int j = 1; j <= n; ++ j) {
            a[i][j] = b[i][j] = '.';
        }
        memset(hasxx, false, sizeof(hasxx));
        memset(hasxy, false, sizeof(hasxy));
        memset(haspx, false, sizeof(haspx));
        memset(haspy, false, sizeof(haspy));
        for (int i = 0; i < m; ++ i) {
            char ch; int x, y;
            cin >> ch >> x >> y;
            a[x][y] = b[x][y] = ch;
            if (ch == 'x') {
                hasxx[x] = hasxy[y] = true;
            } else if (ch == '+') {
                haspx[x - y + n] = haspy[x + y + n + n] = true;
            } else {
                hasxx[x] = hasxy[y] = true;
                haspx[x - y + n] = haspy[x + y + n + n] = true;
            }
        }

        N = n * 4;
        for (int i = 1; i <= N; ++ i) G[i].clear();
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= n; ++ j) if (b[i][j] == '.' or b[i][j] == '+') {
                if (hasxx[i] or hasxy[j]) continue;
                G[i].emplace_back(j + n);
                //G[j + n].emplace_back(i);
            }
        }

        int tmp1 = MaxMatch();
        //cerr << "tmp1: " << tmp1 << endl;
        for (int i = 1; i <= n; ++ i) if (cx[i] != -1) {
            int j = cx[i] - n;
            if (b[i][j] == '.')
                b[i][j] = 'x';
            else
                b[i][j] = 'o';
        }

        N = 4 * n;
        for (int i = 1; i <= N; ++ i) G[i].clear();
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= n; ++ j) if (b[i][j] == '.' or b[i][j] == 'x') {
                int x = i - j + n;
                int y = i + j + n + n;
                if (haspx[x] or haspy[y]) continue;
                G[x].emplace_back(y);
                //G[y].emplace_back(x);
            }
        }
        int tmp2 = MaxMatch();
        //cerr << "tmp2: " << tmp2 << endl;
        for (int k = 1; k <= n + n; ++ k) {
            if (cx[k] != -1) {
                int i = (k + cx[k] - n * 3) / 2;
                int j = (cx[k] - n - k) / 2;
                if (b[i][j] == '.') b[i][j] = '+';
                else if (b[i][j] == 'x') b[i][j] = 'o';
            }
        }

        int ans = 0, cnt = 0;
        for (int i = 1; i <= n; ++ i) for (int j = 1; j <= n; ++ j) {
            if (b[i][j] == 'o') ans += 2;
            else if (b[i][j] != '.') ans += 1;

            if (a[i][j] != b[i][j]) ++ cnt;
        }
        cout << "Case #" << t << ": " << ans << ' ' << cnt << endl;
        for (int i = 1; i <= n; ++ i) for (int j = 1; j <= n; ++ j) {
            if (a[i][j] != b[i][j]) {
                cout << b[i][j] << ' ' << i << ' ' << j << endl;
            }
        }
    }

    return 0;
}

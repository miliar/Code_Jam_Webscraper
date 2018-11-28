#include <bits/stdc++.h>
using namespace std;

template<typename T>
void sci(T& t) {
    cin >> t;
}

template<typename T, typename... Ts>
void sci(T& t, Ts&... ts) {
    sci(t);
    sci(ts...);
}

#define scid(vars...) int vars; sci(vars)
#define scidl(vars...) lint vars; sci(vars)
#define scidd(vars...) double vars; sci(vars)
#define scids(vars...) string vars; sci(vars)

template <typename T, typename Cmp=std::greater<T>>
using heap = priority_queue<T, std::vector<T>, Cmp>;

typedef long long lint;

int n, m;
string a[33];
string b[33];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void dfs(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m || a[nx][ny] != '?') {
            continue;
        }
        a[nx][ny] = a[x][y];
        dfs(nx, ny);
    }
}

void solve() {
    sci(n, m);
    for (int i = 0; i < n; i++) {
        sci(a[i]);
        b[i] = a[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '?') {
                b[i][j] = a[i][j];
                continue;
            }
            char c = 0;
            for (int y = j; y < m; y++) {
                for (int x = i; x >= 0; x--) {
                    if (a[x][y] != '?') {
                        c = c == 0 ? a[x][y] : c;
                        break;
                    }
                }
                for (int x = i + 1; x < n; x++) {
                    if (a[x][y] != '?') {
                        c = c == 0 ? a[x][y] : c;
                        break;
                    }
                }
            }
            for (int y = j - 1; y >= 0; y--) {
                for (int x = i; x >= 0; x--) {
                    if (a[x][y] != '?') {
                        c = c == 0 ? a[x][y] : c;
                        break;
                    }
                }
                for (int x = i + 1; x < n; x++) {
                    if (a[x][y] != '?') {
                        c = c == 0 ? a[x][y] : c;
                        break;
                    }
                }
            }
            if (c == 0) {
                cerr << ":(" << endl;
            }
            b[i][j] = c;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << b[i] << "\n";
    }

}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; ++it) {
//        cerr << it << endl;
        cout << "Case #" << it << ":\n";
        solve();
    }

    return 0;
}
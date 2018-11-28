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

const char* IMPOSSIBLE = "IMPOSSIBLE";

string a[55];
int id[55][55];
vector<int> bc[55][55];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

bool covers(int li, int lj, int ci, int cj) {
    return li == ci && a[li][lj] == '-' || lj == cj && a[li][lj] == '|';
}

void rot(int li, int lj) {
    assert(a[li][lj] == '-' || a[li][lj] == '|');
    a[li][lj] = a[li][lj] == '-' ? '|' : '-';
}

void solve() {
    scid(n, m);
    vector<int> inr(n);
    vector<int> inc(m);
    vector<pair<int, int>> wh;
    int ac = 0;
    for (int i = 0; i < n; i++) {
        sci(a[i]);
        for (int j = 0; j < m; j++) {
            char c = a[i][j];
            if (c == '-' || c == '|') {
                id[i][j] = ac;
                inr[i]++;
                inc[j]++;
                wh.push_back({i, j});
                ac++;
            }
            bc[i][j].clear();
        }
    }

    vector<bool> dm(ac);
    for (int i = 0; i < ac; i++) {
        vector<int> cc(2);
        for (int t = 0; t < 4; t++) {
            int x = wh[i].first;
            int y = wh[i].second;
            while (true) {
                int nx = x + dx[t];
                int ny = y + dy[t];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || a[nx][ny] == '#') {
                    break;
                }
                if (a[nx][ny] != '.') {
                    cc[t / 2]++;
                } else {
                    bc[nx][ny].push_back(i);
                }
                x = nx;
                y = ny;
            }
        }
        if (cc[0] > 0 && cc[1] > 0) {
            cout << IMPOSSIBLE << "\n";
            return;
        }
        if (cc[0] > 0) {
            a[wh[i].first][wh[i].second] = '-';
            dm[i] = true;
        }

        if (cc[1] > 0) {
            a[wh[i].first][wh[i].second] = '|';
            dm[i] = true;
        }
    }

    while (true) {
        int sz = 1e9;
        int ci = -1;
        int cj = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] == '.') {
                    bool uc = true;
                    int ud = 0;
                    for (auto id : bc[i][j]) {
                        if (dm[id] && covers(wh[id].first, wh[id].second, i, j)) {
                            uc = false;
                            break;
                        }
                        if (!dm[id]) {
                            ud++;
                        }
                    }
                    if (uc && ud < sz) {
                        sz = ud;
                        ci = i;
                        cj = j;
                    }
                }
            }
        }
        if (sz == 1e9) {
            break;
        }
        if (sz == 0) {
            cout << IMPOSSIBLE << "\n";
            return;
        }
        for (auto id : bc[ci][cj]) {
            if (!dm[id]) {
                if (!covers(wh[id].first, wh[id].second, ci, cj)) {
                    rot(wh[id].first, wh[id].second);
                }
                dm[id] = true;
                break;
            }
        }
    }
    cout << "POSSIBLE\n";
    for (int i = 0; i < n; i++) {
        cout << a[i] << "\n";
    }
}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; it++) {
        cerr << it << endl;
        cout << "Case #" << it << ": ";
        solve();
    }

    return 0;
}
#include <iostream>
#include <vector>

using namespace std;

int n, m;
string s[100];
bool f;

vector<pair<int,int>> v[10000][5];
int c[10000];

bool lol;

void add(int y1, int x1, int u1, int y2, int x2, int u2) {
    int t1 = y1*100+x1;
    int t2 = y2*100+x2;
    v[t1][3-u1].push_back({t2,u2});
    v[t2][3-u2].push_back({t1,u1});
}

void check(int y, int x) {
    int c1 = 0, c2 = 0;
    int y1, x1, y2, x2;
    for (int i = x-1; i >= 0; i--) {
        if (s[y][i] == '#') break;
        if (s[y][i] == '*') {
            c1++;
            y1 = y;
            x1 = i;
        }
    }
    for (int i = x+1; i < m; i++) {
        if (s[y][i] == '#') break;
        if (s[y][i] == '*') {
            c1++;
            y1 = y;
            x1 = i;
        }
    }
    for (int i = y-1; i >= 0; i--) {
        if (s[i][x] == '#') break;
        if (s[i][x] == '*') {
            c2++;
            y2 = i;
            x2 = x;
        }
    }
    for (int i = y+1; i < n; i++) {
        if (s[i][x] == '#') break;
        if (s[i][x] == '*') {
            c2++;
            y2 = i;
            x2 = x;
        }
    }
    if (c1 && c2) {
        add(y1, x1, 1, y2, x2, 2);
        return;
    }
    if (c1) {
        add(y1, x1, 1, y1, x1, 1);
        return;
    }
    if (c2) {
        add(y2, x2, 2, y2, x2, 2);
        return;
    }
    lol = true;
}

void scan1(int y1, int y2, int x) {
    if (s[y1][x] != '*') return;
    if (s[y2][x] != '*') return;
    for (int i = y1+1; i <= y2-1; i++) {
        if (s[i][x] == '#') return;
    }
    add(y1,x,1,y1,x,1);
    add(y2,x,1,y2,x,1);
}

void scan2(int y, int x1, int x2) {
    if (s[y][x1] != '*') return;
    if (s[y][x2] != '*') return;
    for (int i = x1+1; i <= x2-1; i++) {
        if (s[y][i] == '#') return;
    }
    add(y,x1,2,y,x1,2);
    add(y,x2,2,y,x2,2);
}

bool ok(int t, int u) {
    if (c[t] != 0 && c[t] != u) return false;
    for (auto g : v[t][u]) {
        int ut = g.first;
        int uu = g.second;
        if (c[ut] != 0 && c[ut] != uu) return false;
        if (t == ut && u != uu) return false;
    }
    return true;
}

void search(int y, int x) {
    if (f) return;
    if (y == n) {
        cout << "POSSIBLE\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i][j] == '*') {
                    int t = 100*i+j;
                    if (c[t] == 1) cout << "-";
                    else cout << "|";
                } else cout << s[i][j];
            }
            cout << "\n";
        }
        f = true;
        return;
    }
    if (x == m) {
        search(y+1,0);
        return;
    }
    int t = y*100+x;
    if (s[y][x] == '*') {
        if (ok(t,1)) {
            c[t] = 1;
            search(y,x+1);
        }
        if (ok(t,2)) {
            c[t] = 2;
            search(y,x+1);
        }
    } else {
        search(y,x+1);
    }
}

void solve(int t) {
    cin >> n >> m;
    f = false;
    lol = false;
    for (int i = 0; i < 10000; i++) {
        for (int j = 0; j < 5; j++) v[i][j].clear();
    }
    for (int i = 0; i < 10000; i++) c[i] = 0;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '-') s[i][j] = '*';
            if (s[i][j] == '|') s[i][j] = '*';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '.') check(i,j);
        }
    }
    for (int y1 = 0; y1 < n; y1++) {
        for (int y2 = y1+1; y2 < n; y2++) {
            for (int x = 0; x < m; x++) {
                scan1(y1,y2,x);
            }
        }
    }
    for (int x1 = 0; x1 < m; x1++) {
        for (int x2 = x1+1; x2 < m; x2++) {
            for (int y = 0; y < n; y++) {
                scan2(y,x1,x2);
            }
        }
    }
    cout << "Case #" << t << ": ";
    if (lol) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    search(0,0);
    if (!f) cout << "IMPOSSIBLE\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}

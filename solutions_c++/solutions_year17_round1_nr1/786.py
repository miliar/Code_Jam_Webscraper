#include <bits/stdc++.h>

using namespace std;

const int N = (int)50;

int cases;

int n, m;

char a[N][N];

void read_input() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> a[i][j];
}

bool fillj(int i) {
    char cur = '?';
    bool was = false;
    for (int j = 0; j < m; ++j) {
        if (a[i][j] != cur && a[i][j] != '?') {
            cur = a[i][j];
            was = true;
        }
        a[i][j] = cur;
    }
    cur = '?';
    for (int j = m - 1; j >= 0; --j) {
        if (a[i][j] != cur && a[i][j] != '?') {
            cur = a[i][j];
            was = true;
        }
        a[i][j] = cur;
    }
    return was;
}

void solve() {
    for (int i = 0; i < n; ++i) {
        bool ok = fillj(i);
        if (ok) continue;
        if (i != 0) {
            for (int j = 0; j < m; ++j)
                a[i][j] = a[i - 1][j];
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        bool ok = fillj(i);
        if (ok) continue;
        if (i != n - 1) {
            for (int j = 0; j < m; ++j)
                a[i][j] = a[i + 1][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        bool ok = fillj(i);
        if (ok) continue;
        if (i != 0) {
            for (int j = 0; j < m; ++j)
                a[i][j] = a[i - 1][j];
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        bool ok = fillj(i);
        if (ok) continue;
        if (i != n - 1) {
            for (int j = 0; j < m; ++j)
                a[i][j] = a[i + 1][j];
        }
    }
}

void write_output(int test) {
    cout << "Case #" << test << ": \n";
    for (int i = 0; i < n; ++i, cout << endl)
        for (int j = 0; j < m; ++j) cout << a[i][j];

}

void clear_data() {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            a[i][j] = '?';
    n = m = 0;
}

int main() {
    ios_base::sync_with_stdio(false);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> cases;
    for (int test = 1; test <= cases; ++test) {
        read_input();
        solve();
        write_output(test);
        clear_data();
    }
    return 0;
}

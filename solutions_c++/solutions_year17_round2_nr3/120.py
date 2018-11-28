#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n = 1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        solve(i);
    }
}

const int MAX_N = 105; // TODO

int n, q;
long long d[MAX_N][MAX_N];
int e[MAX_N], s[MAX_N];
int pq[MAX_N][2];

void read_input() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> d[i][j];
        }
    }
    for (int i = 0; i < q; i++) {
        cin >> pq[i][0] >> pq[i][1];
        pq[i][0]--;
        pq[i][1]--;
    }
}

void init() {
    // memset(a, -1, sizeof(a));
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
}

void solve(int test_number) {
    read_input();
    init();

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][k] < 0 || d[k][j] < 0) {
                    continue;
                }
                if (d[i][j] < 0) {
                    d[i][j] = d[i][k] + d[k][j];
                } else {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
    }

    output(test_number);
    for (int k = 0; k < q; k++) {
        int sr = pq[k][0], t = pq[k][1];
        double dist[MAX_N];
        for (int j = 0; j < n; j++) {
            dist[j] = -1;
        }
        dist[sr] = 0;
        bool vis[MAX_N] = {false};
        while (true) {
            int mn = -1;
            for (int i = 0; i < n; i++) {
                if (vis[i] || dist[i] < 0) {
                    continue;
                }
                if (mn < 0 || dist[i] < dist[mn]) {
                    mn = i;
                }
            }
            if (mn < 0) {
                break;
            }
            vis[mn] = true;
            for (int i = 0; i < n; i++) {
                if (vis[i] || d[mn][i] < 0 || d[mn][i] > e[mn]) {
                    continue;
                }
                double val = dist[mn] + (double)d[mn][i] / s[mn];
                if (dist[i] < 0) {
                    dist[i] = val;
                } else {
                    dist[i] = min(dist[i], val);
                }
            }
        }
        cout << dist[t] << " ";
    }

    cout << endl;
}

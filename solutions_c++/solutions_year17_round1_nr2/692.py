#include <bits/stdc++.h>

using namespace std;

const int N = 60;

typedef pair<int, int> pi;

int n, p;
int r[N];
multiset <pi> q[N];

int getLow(int u, int v) {
    return (v * 10 - 1) / (u * 11) + 1;
}

int getHigh(int u, int v) {
    return (10 * v) / (u * 9);
}

int solver() {
    scanf("%d %d", &n, &p);
    for (int i = 1; i <= n; i++) {
        scanf("%d", r + i);
        q[i].clear();
    }
    for (int i = 1; i <= n; i++) {
//        if (flag)
//        cerr << i << ": " << endl;
        for (int j = 1; j <= p; j++) {
            int u;
            scanf("%d", &u);
            int low = getLow(r[i], u);
            int high = getHigh(r[i], u);
            if (low <= high) {
                q[i].insert(make_pair(low, high));
            }
        }
//    if (flag)
//        for (pi u : q[i]) {
//            cerr << u.first << " " << u.second << endl;
//        }
    }
    int res = 0;
    for (int num = 1; num <= 1e6 + 10; num++) {
        while (1) {
            int f = 0;
            for (int i = 1; i <= n; i++) {
                while (!q[i].empty() && q[i].begin()->second < num) {
                    q[i].erase(q[i].begin());
                }
                if (q[i].empty()) {
                    return res;
                }
                if (q[i].begin()->first > num) {
                    f = 1;
                    break;
                }
            }
            if (f) {
                break;
            }
            res++;
            for (int i = 1; i <= n; i++) {
                q[i].erase(q[i].begin());
            }
        }
    }
    return res;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int test = 1; test <= tc; test++) {
        printf("Case #%d: %d\n", test, solver());
    }
    return 0;
}

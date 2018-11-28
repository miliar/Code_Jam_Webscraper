#include <bits/stdc++.h>

using namespace std;

int test, n, k, u, p;
char s[20];

int read() {
    scanf("%s", s);
    int t1, t2;
    sscanf(s, "%d.%d", &t1, &t2);
    return t1 * 10000 + t2;
}

int main() {
    scanf("%d", &test);

    for (int tt = 1; tt <= test; ++tt) {
        scanf("%d %d", &n, &k);
        u = read();
        priority_queue<int, vector<int>, greater<int> > heap;

        for (int i = 1; i <= n; ++i) {
            p = read();
            heap.push(p);
        }

        while (u --> 0) {
            p = heap.top();
            heap.pop();
            heap.push(p + 1);
        }

        double res = 1;
        while (!heap.empty()) {
            p = heap.top();
            heap.pop();
            double t = 1.0 * p / 10000.0;
            res = res * t;
        }

        printf("Case #%d: %.6lf\n", tt, res);
    }
    return 0;
}

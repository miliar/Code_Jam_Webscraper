#define DBG 1

#include <cstring>
#include <map>
#include <unordered_map>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> pii;

int gi() {
    int a;
    scanf("%d", &a);
    return a;
}

ll gli() {
    ll a;
    scanf("%lld", &a);
    return a;
}

char a[30][30];

void wrk(int x1, int x2, int y1, int y2) {
    int c = 0;
    int x[2], y[2];
    for (int i = x1; i < x2 && c < 2; i++)
        for (int j = y1; j < y2 && c < 2; j++)
            if (a[i][j] != '?') {
                x[c] = i;
                y[c] = j;
                c++;
            }
    if (c == 1) {
        char v = a[x[0]][y[0]];
        for (int i = x1; i < x2; i++)
            for (int j = y1; j < y2; j++)
                a[i][j] = v;
        return;
    }
    if (x[0] != x[1]) {
        wrk(x1, x[1], y1, y2);
        wrk(x[1], x2, y1, y2);
    } else {
        wrk(x1, x2, y1, y[1]);
        wrk(x1, x2, y[1], y2);
    }
}

#define SINGLELINE 0
void solve() {
    int n = gi();
    int m = gi();

    for (int i = 0; i < n; i++)
        scanf("%s", a[i]);

    wrk(0, n, 0, m);

    for (int i = 0; i < n; i++)
        printf("%s\n", a[i]);
}

int main() {
    int t = gi();

    for (int i = 1; i <= t; i++) {
        printf("Case #%d:%c", i, (SINGLELINE ? ' ' : '\n'));
        solve();
        fprintf (stderr, "Case %d / %d. Elapsed %.2f. Estimated %.2f\n", i, t, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * t) / CLOCKS_PER_SEC);
    }

    return 0;
}

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

int r[54][54];
int rec[54];
int pn[54];
int n, p;

#define RT printf("%d\n", res); return

#define SINGLELINE 1
void solve() {
    n = gi();
    p = gi();

    for (int i = 0; i < n; i++)
        rec[i] = gi();

    int f = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++)
            r[i][j] = gi();
        sort(r[i], r[i] + p);
        pn[i] = 0;
    }

    int res = 0;
    for (int c = 1; ; ) {
        for (int i = 0; i < n; i++) {
            int m9 = rec[i] * c * 9;
            if (m9 % 10 == 0)
                m9 /= 10;
            else
                m9 = m9/10 + 1;
            while (pn[i] < p && r[i][pn[i]] < m9)
                pn[i]++;
            if (pn[i] >= p) {
                RT;
            }
        }
        int y = 1;
        for (int i = 0; i < n; i++) {
            int m11 = rec[i] * c * 11 / 10;
            if (r[i][pn[i]] > m11) {
                y = 0;
                break;
            }
        }
        if (y) {
            for (int i = 0; i < n; i++)
                pn[i]++;
            res++;
        } else {
            c++;
        }
    }
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

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

#define SINGLELINE 1
void solve() {
    int n = gi();
    int p = gi();

    int a[4];
    for (int i = 0; i < p; i++)
        a[i] = 0;
    for (int i = 0; i < n; i++) {
        int x = gi() % p;
        a[x]++;
    }

    int res = a[0];
    if (p == 2) {
        res += (a[1]+1)/2;
    } else if (p == 3) {
        int m = MIN(a[1], a[2]);
        a[1] -= m;
        a[2] -= m;
        res += m;
        if (a[1]) {
            res += a[1]/3;
            a[1] -= (a[1]/3) * 3;
            if (a[1])
                res++;
        }
        if (a[2]) {
            res += a[2]/3;
            a[2] -= (a[2]/3) * 3;
            if (a[2])
                res++;
        }
    } else {
    }
    printf("%d\n", res);
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

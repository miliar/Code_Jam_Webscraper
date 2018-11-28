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

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define ld long double

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int maxn = 1005;

int pos[maxn];
int v[maxn];

int main() {
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        int d, n;
        scanf("%d%d", &d, &n);
        forn(j, n)
            scanf("%d%d", &pos[j], &v[j]);
        ld T;
        for (int j = n - 1; j >= 0; j--) {
            ld newt = (ld)(d - pos[j]) / v[j];
            if (j == n - 1)
                T = newt;
            else T = max(newt, T);
        }
        ld ans = d / T;
        printf("Case #%d: %.10lf\n", test + 1, (double)ans);
    }
}

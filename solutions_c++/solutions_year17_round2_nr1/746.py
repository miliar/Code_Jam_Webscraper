// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;
typedef pair < double, double > pd;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-12;

const int MAX_N = (int)1e6 + 123;

int d, n;
pi a[MAX_N];

double T(pd a, pd b) {
    if (a.s < b.s || fabs(a.s - b.s) < eps)
        return 1.0 * d;
    return 1.0 * (b.f - a.f) / (a.s - b.s);
}

double solve() {
    scanf("%d%d", &d, &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d%d", &a[i].f, &a[i].s);
    }
    sort(a + 1, a + n + 1);
    double v = 1e18;
    for (int i = n; i > 0; i--) {
        double t = (1.0 * d - a[i].f) / (1.0 * a[i].s);
        v = min(v, 1.0 * d / t);
    }
    return v;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int numberOfTests;
    scanf("%d", &numberOfTests);
    for (int i = 1; i <= numberOfTests; i++) {
        printf("Case #%d: %.6f\n", i, solve());
    }
    return 0;
}


#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

typedef long long ll;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

using namespace std;

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    double d;
    int n;
    cin >> d >> n;
    double ans = 1e20;
    forn(i, n) {
        double k, s;
        cin >> k >> s;
        ans = min(ans, d * s / (d - k));
    }
    cout.precision(12);
    cout << fixed << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <list>
#include <cstdlib>
#include <bitset>
#include <ctime>

#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;

void solve() {
    int n, k;
    scanf("%d %d", &n, &k);

    map<int, int, greater<int> > s;
    s[n] = 1;

    for (int i = 0; i < k; ++i) {
        pair<int, int> p = *(s.begin());
        if (p.second > 1) {
            s[p.first] = s[p.first] - 1;
        } else {
            s.erase(p.first);
        }
        int f1, f2;
        if (p.first % 2 == 0) {
            f1 = p.first / 2;
            f2 = p.first / 2 - 1;
        } else {
            f1 = f2 = p.first / 2;
        }
        if (i == k - 1) {
            printf("%d %d", f1, f2);
        }
        if (s.count(f1)) {
            s[f1] = s[f1] + 1;
        } else {
            s[f1] = 1;
        }
        if (s.count(f2)) {
            s[f2] = s[f2] + 1;
        } else {
            s[f2] = 1;
        }
    }
}

int main() {

    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/c.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/c.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    
    return 0;
}
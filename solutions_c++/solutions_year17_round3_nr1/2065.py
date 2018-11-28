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
const ld pi = 3.14159265358979323846;

int n, k;
pair<pair<ld,ld>, int> panks[1000];

inline ld area(int pank) {
    return pi*panks[pank].first.first*panks[pank].first.first;
}

inline ld sideArea(int pank) {
    return pi*2*panks[pank].first.first*panks[pank].first.second;
}

ld rec(int lev, int curPal, ld curRes) {
    if (lev == k) {
        return curRes;
    }
    ld res = curRes;
    for (int i = curPal+1; i < n; ++i) {
        res = max(res, rec(lev+1, i, curRes + sideArea(i)));
    }
    return res;
}

void solve() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%Lf %Lf", &panks[i].first.first, &panks[i].first.second);
        panks[i].second = i;
    }
    sort(panks, panks+n, std::greater<pair<pair<ld, ld>, int> >());
    ld res = 0;
    for (int i = 0; i < n; ++i) {
        res = max(res, rec(1, i, area(i)+sideArea(i)));
    }
    printf("%.9Lf", res);
}

int main() {
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/a.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/a.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    
    return 0;
}
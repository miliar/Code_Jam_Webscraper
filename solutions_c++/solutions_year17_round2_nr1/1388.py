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


ld d, k[1000], s[1000];
int n;
void solve() {
    ld times[1000];
    scanf("%Lf %d", &d, &n);
    ld slowest = 0;
    int slowestIdx = -1;
    for (int i = 0; i < n; ++i) {
        scanf("%Lf %Lf", &k[i], &s[i]);
        times[i] = (d-k[i])/s[i];
        if (slowest < times[i]) {
            slowest = times[i];
            slowestIdx = i;
        }
    }
    ld res = d/slowest;
    printf("%Lf", res);
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
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
    char buf[1024];
    int k;
    scanf("%s %d\n", buf, &k);
    int res = 0;
    size_t len = strlen(buf);
    for (int i = 0; i < len - k + 1; ++i) {
        if (buf[i] == '-') {
            res++;
            for (int j = 0; j < k; ++j) {
                buf[j+i] = buf[j+i] == '-' ? '+' : '-';
            }
        }
    }
    for (int j = 0; j < k; ++j) {
        if (buf[len-1-j] == '-') {
            printf("IMPOSSIBLE");
            return;
        }
    }
    printf("%d", res);
    return;
}

int main() {

    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/a.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/a.out", "w", stdout);

    int tests;
    scanf("%d", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }

    return 0;
}
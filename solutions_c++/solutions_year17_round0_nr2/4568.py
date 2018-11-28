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
    char n[20];
    scanf("%s\n", n);
    size_t 	len = strlen(n);
again:
    for (int i = 1; i < len; i++) {
        if (n[i] < n[i-1]) {
            n[i-1]--;
            for (int j = i; j < len; ++j) {
                n[j] = '9';
            }
            goto again;
        }
    }
    printf("%s", n[0] == '0' ? &n[1] : n);
}

int main() {

    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/b.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/b.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    
    return 0;
}
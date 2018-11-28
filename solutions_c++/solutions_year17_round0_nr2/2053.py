#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

const int MAXL = 20;
char minafter[MAXL];

int T; LL n;

bool check(LL x) {
    LL curr = 10;

    while (x) {
        if (x % 10 > curr) {
            return false;
        }
        else {
            curr = min(curr, x % 10);
            x /= 10;
        }
    }

    return true;
}

void solve() {
    if (check(n)) { printf("%lld\n", n); return; }

    LL prefix = n / 10; LL pow = 10; LL suffix = 9;

    while (prefix) {
        LL curr = (prefix - 1) * pow + suffix;

        if (check(curr)) { printf("%lld\n", curr); return; }

        prefix /= 10; pow *= 10; suffix = 10 * suffix + 9;
    }

    assert(false);
}

int main() {
    GI(T);

    FOR1(t, T) {
        printf("Case #%d: ", t);

        GLL(n);
        solve();
    }

    return 0;
}

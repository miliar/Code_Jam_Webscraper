#include <iostream>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;

long long best(long long n, long long cur, long long ld, int lv) {
    if (ld == 0)
        return cur;
    for (int v = 9; v >= lv; v--) {
        if (cur + ld * v <= n) {
            long long c_best = best(n, cur + ld * v, ld / 10, v);
            if (c_best >= 0)
                return c_best;
        }
    }
    return -1;
}

void solve() {
    long long n;
    cin >> n;
    long long d = 1;
    while (n / 10 >= d)
        d *= 10;
    cout << best(n, 0, d, 0) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    
    
    return 0;
}

#include <cstdint>
#include <iostream>
#include <map>
#include <sstream>
#include <stdio.h>
using namespace std;

void solve()
{
    int64_t n, k;
    cin >> n >> k;
    map<int64_t, int64_t> mm;
    mm[n] = 1;

    while (k > 0) {
        int64_t v = mm.rbegin()->first;
        int64_t c = mm.rbegin()->second;
        mm.erase(mm.rbegin()->first);

        int64_t mi = (v - 1) / 2;
        int64_t ma = (v - 1) - mi;

        if (c >= k) {
            printf("%ld %ld\n", ma, mi);
            return;
        }

        k -= c;
        mm[mi] += c;
        mm[ma] += c;
    }

    abort();
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

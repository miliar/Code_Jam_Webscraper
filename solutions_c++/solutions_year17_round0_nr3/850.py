#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define LL long long
LL n, k;

map<LL, LL> ms;

int main() {
    int test;
    cin >> test;
    for (int cas = 1; cas <= test; cas++) {
        cin >> n >> k;
        LL tt = 0;
        ms.clear();
        ms[n] = 1;
        LL na, nb;
        while (tt < k) {
            auto x = ms.rbegin();
            LL m = x->first;
            LL val = x->second;
            if (m == 1) {
                na = 0;
                nb = 0;
            }
            else if (m == 2) {
                na = 1;
                nb = 0;
                ms[1] += val;
            }
            else {
                if (m & 1) {
                    na = m >> 1;
                    nb = m >> 1;
                }
                else {
                    na = m >> 1;
                    nb = (m - 1) >> 1;
                }
               // cou << na << ' ' << nb << endl;
               ms[na] += val;
               ms[nb] += val;
            }
            ms.erase(x->first);
            tt += val;
            //cout << tt << ' ' << k << endl;
        }

        printf("Case #%d: %lld %lld\n", cas, na, nb);
    }
    return 0;
}


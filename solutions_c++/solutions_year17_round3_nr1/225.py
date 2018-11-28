#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>
#include <cmath>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

template <typename T>
int numbits(T n) {
    return n ? 1 + numbits(n & (n - 1)) : 0;
}

class timer {
public:
    timer() : t_(clock()) {}
    void restart() { t_ = clock(); }
    float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
    clock_t t_;
};

void run();

int main() {
#ifdef LOCAL_HOST
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    timer t;
#endif
    run();
#ifdef LOCAL_HOST
    // printf("\nElapsed time: %.9f\n", t.elapsed());
#endif
    return 0;
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n, k;
        cin >> n >> k;
        vector<pair<ll, ll> > vp(n);
        for (int i = 0; i < vp.size(); ++i) {
            ll r, h; cin >> r >> h;
            vp[i].first = r * r;
            vp[i].second = 2 * r * h;
        }
        sort(all(vp));
        reverse(all(vp));
        ll res = 0.0;
        for (int i = 0; i < vp.size(); ++i) {
            vector<ll> rest;
            for (int j = i + 1; j < vp.size(); ++j) {
                rest.push_back(vp[j].second);
            }
            sort(all(rest));
            reverse(all(rest));
            ll subres = vp[i].first + vp[i].second;
            for (int j = 0; j < min(k-1, int(rest.size())); ++j) {
                subres += rest[j];
            }
            res = max(res, subres);
        }
        printf("Case #%d: %.9f\n", cs + 1, Pi * res);
    }
}


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
        int n, k; cin >> n >> k;
        double units; cin >> units;
        vector<double> probs(n);
        for (int i = 0; i < probs.size(); ++i) {
            cin >> probs[i];
        }
        sort(all(probs));
        while (units > 1E-9 && probs[0] < 1.0 - 1e-9) {
            int cnt = count(all(probs), probs[0]);
            double nval = min(probs[0] + units / cnt, (cnt == probs.size()) ? 1.0 : probs[cnt]);
            units -= (nval - probs[0]) * cnt;
            for (int j = 0; j < cnt; ++j) {
                probs[j] = nval;
            }
        }
        double res = 1.0;
        for (int i = 0; i < probs.size(); ++i) {
            res *= probs[i];
        }
        printf("Case #%d: %.9f\n", cs + 1, res);
    }
}


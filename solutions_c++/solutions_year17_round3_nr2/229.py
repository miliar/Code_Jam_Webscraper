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

int times[1440];
int dp[1440][2][1440];

void update(int& dest, int val) {
    if (dest == -1 || dest > val) {
        dest = val;
    }
}

int get(int& dest) {
    if (dest == -1) {
        return 2e9;
    } else {
        return dest;
    }
}

int solve(int who) {
    memset(dp, -1, sizeof(dp));
    if (times[0] == -1 || times[0] == 0) {
        if (who == 0) {
            dp[0][0][1] = 0;
        } else {
            dp[0][0][1] = 1;
        }
    }
    if (times[0] == -1 || times[0] == 1) {
        if (who == 0) {
            dp[0][1][0] = 1;
        } else {
            dp[0][1][0] = 0;
        }
    }
    for (int turn = 0; turn < 1439; ++turn) {
        for (int player = 0; player < 2; ++player) {
            for (int first = 0; first <= 720; ++first) {
                int exch = dp[turn][player][first];
                if (exch == -1) {
                    continue;
                }
                if (times[turn + 1] == -1 || times[turn + 1] == 0) {
                    if (player == 0) {
                        update(dp[turn + 1][0][first + 1], exch);
                    } else {
                        update(dp[turn + 1][0][first + 1], exch + 1);
                    }
                }
                if (times[turn + 1] == -1 || times[turn + 1] == 1) {
                    if (player == 0) {
                        update(dp[turn + 1][1][first], exch + 1);
                    } else {
                        update(dp[turn + 1][1][first], exch);
                    }
                }
            }
        }
    }
    return min(get(dp[1439][0][720]) + who, get(dp[1439][1][720]) + (who ^ 1));
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        memset(times, -1, sizeof(times));
        int ac; int aj;
        cin >> ac >> aj;
        for (int i = 0; i < ac; ++i) {
            int a, b; cin >> a >> b;
            for (int j = a; j < b; ++j) {
                times[j] = 0;
            }
        }
        for (int i = 0; i < aj; ++i) {
            int a, b; cin >> a >> b;
            for (int j = a; j < b; ++j) {
                times[j] = 1;
            }
        }
        int res0 = solve(0);
        int res1 = solve(1);
        int res = min(res0, res1);
        cout << "Case #" << cs + 1 << ": " << res << endl;
    }
}


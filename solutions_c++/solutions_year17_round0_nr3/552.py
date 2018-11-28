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

struct State {
    int cells;
    int idx;

    State(int c, int i) {
        cells = c;
        idx = i;
    }

    bool operator<(const State& that) const {
        if (cells != that.cells) {
            return cells < that.cells;
        }
        return idx < that.idx;
    }
};

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        ll n, k; cin >> n >> k;
        ll intervals = 1;
        ll power = 1;
        for (;;) {
            if (power * 2 > k) {
                break;
            }
            intervals += power;
            power *= 2;
        }
        k -= (power - 1);
        ll avg_div = (n - (power - 1)) / power;
        ll avg_mod = (n - (power - 1)) % power;
        if (avg_mod >= k) {
            avg_div++;
        }
        cout << "Case #" << cs + 1 << ": " << avg_div / 2 << " " << (avg_div-1) / 2 << endl;
    }
}

// void run() {
//     int T; cin >> T;
//     for (int cs = 0; cs < T; ++cs) {
//         ll n, k; cin >> n >> k;
//         priority_queue<State> pq;
//         pq.push(State(n, 1));
//         for (int i = 0; i < k - 1; ++i) {
//             State s = pq.top();
//             pq.pop();
//             int cells1 = (s.cells - 1) / 2;
//             int cells2 = s.cells / 2;
//             pq.push(State(cells1, s.idx));
//             pq.push(State(cells2, s.idx + cells1 + 1));
//         }
//         State s = pq.top();
//         cout << "Case #" << cs + 1 << ": " << s.cells / 2 << " " << (s.cells-1) / 2 << endl;
//     }
// }

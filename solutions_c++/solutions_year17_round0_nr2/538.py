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
        string str; cin >> str;
        string res = "";
        for (int i = 0; i < str.size(); ++i) {
            if (i && str[i] < str[i - 1]) {
                break;
            }
            if (i && (str[i] - 1 < str[i - 1]) && (i != str.size() - 1)) {
                continue;
            }
            res = str.substr(0, i + 1) + string(str.size() - i - 1, '9');
            if (i != str.size() - 1) {
                res[i]--;
            }
        }
        while(res[0] == '0') {
            res = res.substr(1);
        }
        cout << "Case #" << cs + 1 << ": " << res << endl;
    }
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

const int64_t NINES = 999999999999999999LL;

bool check(int64_t ans) {
    bool ok = true;
    int64_t prev_last = 9;
    while (ok && ans != 0) {
        int64_t last = ans % 10;
        ok &= (last <= prev_last);
        ans /= 10;
        prev_last = last;
    }
    return ok;
}

int64_t solve(int64_t number) {
    int64_t ans = number;
    int64_t base = 1;
    while (!check(ans)) {
        int64_t next = (ans / base - 1) * base + NINES % base;
        ans = next;
        base *= 10LL;
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    int64_t number;
    for (int t = 1; t <= T; ++t) {
        cin >> number;
        cout << "Case #" << t << ": " << solve(number) << endl;
    }
    return 0;
}

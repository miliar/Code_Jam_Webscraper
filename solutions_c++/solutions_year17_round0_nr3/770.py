#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

pair<int64_t, int64_t> solve_brute(int64_t n, int64_t k) {
    priority_queue<int64_t> q;

    q.push(n);
    for (int i = 0; i < k - 1; ++i) {
        int64_t cur = q.top();
        q.pop();
        --cur;
        q.push(cur / 2);
        q.push(cur / 2 + cur % 2);
    }
    int64_t cur = q.top() - 1;
    return make_pair(cur / 2 + cur % 2, cur / 2);
}

pair<int64_t, int64_t> solve(int64_t n, int64_t k) {
    int64_t mnv = n;
    int64_t mnc = 1;
    int64_t mxv = n;
    int64_t mxc = 0;

    int l = 0;
    int64_t seen = 0;
    while (seen + (1LL << l) < k) {
        int64_t new_mnv = (mnv - 1) / 2;
        int64_t new_mnc = mnc;
        int64_t new_mxv = (mxv - 1) / 2 + (mxv - 1) % 2;
        int64_t new_mxc = mxc;

        if ((mnv - 1) % 2 != 0) {
            new_mxc *= 2;
            new_mxc += mnc;
        } else {
            new_mnc *= 2;
            new_mnc += mxc;
        }

        mnv = new_mnv;
        mnc = new_mnc;
        mxv = new_mxv;
        mxc = new_mxc;

        seen += 1LL << l;
        ++l;
    }

    if (k - seen <= mxc) {
        return make_pair((mxv - 1) / 2 + (mxv - 1) % 2, (mxv - 1) / 2);
    }
    return make_pair((mnv - 1) / 2 + (mnv - 1) % 2, (mnv - 1) / 2);
}

int main() {
    cin.sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int64_t n, k;
        cin >> n >> k;
//        pair<int64_t, int64_t> res = solve_brute(n, k);
        pair<int64_t, int64_t> res1 = solve(n, k);

//        cout << "Case #" << t << ": " << res.first << " " << res.second << endl;
        cout << "Case #" << t << ": " << res1.first << " " << res1.second << endl;

    }

    return 0;
}

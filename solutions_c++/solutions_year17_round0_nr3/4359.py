#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>
#include <cmath>

using i64 = long long;

using namespace std;

i64 ilog2(i64 n) {
    i64 p = 0;
    i64 num = 1;
    while (num <= n) {
        p++;
        num *= 2;
    }

    return p - 1;
}

pair<i64, i64> get_ans(i64 l, i64 r, i64 k) {
    i64 n = r - l - 1;
    i64 h = ilog2(k);
    i64 level_count = (1 << h);
    i64 level_index = k - (1 << h);

    i64 count_before = (1 << h) - 1;

    i64 fl = (n - count_before) / (count_before + 1);
    i64 cl = (n) / (count_before + 1);

    i64 count_big = (n - count_before) % (count_before + 1);
    i64 count_small = (count_before + 1) - count_big;

    if (level_index < count_big) {
        return make_pair((cl) / 2, (cl - 1) / 2);
    } else {
        return make_pair((fl) / 2, (fl - 1) / 2);
    }
}

int main() {
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        // cerr << "Case #" << test << ": ";

        i64 n, k;
        cin >> n >> k;

        auto ans = get_ans(0, n + 1, k);
        cout << ans.first << " " << ans.second << endl;
    }
}
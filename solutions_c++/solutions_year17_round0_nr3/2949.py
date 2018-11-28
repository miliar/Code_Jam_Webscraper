#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <unordered_set>
#include <deque>
#include <set>

using namespace std;

std::pair<uint64_t, uint64_t> solve(uint64_t n, uint64_t k) {
    int p = 0;
    uint64_t base = 1;

    while (base <= k) {
        base <<= 1;
        p++;
    }

    p--;
    base >>= 1;
    uint64_t rhs = n - (base - 1);

    uint64_t a = n / base;
    uint64_t b = (n - 1) / base;
    cout << "base = " << base << " a = " << a << " b = " << b << endl;
    if (a == b) {
        uint64_t res = rhs / a;
        uint64_t r = a / 2;
        uint64_t l = a - r - 1;

        return {l, r};
    }

    // a - b = 1
    uint64_t k1 = rhs - base * b;
    uint64_t k2 = base - k1;

    cout << "rhs = " << rhs << " k1 = " << k1 << endl;
    k -= base;
    if (k <= k1) {
        uint64_t r = a / 2;
        uint64_t l = a - r - 1;
        return {l, r};
    }

    uint64_t r = b / 2;
    uint64_t l = b - r - 1;
    return {l, r};
}

std::pair<uint64_t, uint64_t> solve_fast(uint64_t n, uint64_t k) {
    std::map<uint64_t, uint64_t, std::greater<uint64_t>> gap_size_amount;

    gap_size_amount[n] = 1;
    uint64_t gaps_num = 1;
    while (gaps_num < k) {
        k -= gaps_num;
        gaps_num = 0;
        std::map<uint64_t, uint64_t, std::greater<uint64_t>> new_gaps;
        for (auto &g : gap_size_amount) {
            uint64_t r = g.first / 2;
            uint64_t l = (r > 0 ? g.first - r - 1 : 0);
            new_gaps[l] += g.second;
            new_gaps[r] += g.second;
            if (g.first)
                gaps_num += 2 * g.second;
        }

        gap_size_amount = new_gaps;
    }
    for (auto &g : gap_size_amount) {
        if (k > g.second)
            k -= g.second;
        else {
            uint64_t r = g.first / 2;
            uint64_t l = (r > 0 ? g.first - r - 1 : 0);
            return {l, r};
        }
    }
};

std::pair<uint64_t, uint64_t> solve_naive(uint64_t n, uint64_t k) {
    std::multiset<uint64_t, std::greater<uint64_t >> gaps;
    gaps.insert(n);

    uint64_t l, r;
    for (int i = 0; i < k; i++) {
        uint64_t g = *gaps.begin();
 //       cout << g << endl;
        gaps.erase(gaps.begin());

        l = (g - 1) / 2;
        r = g / 2;
        gaps.insert(l);
        gaps.insert(r);

       // cout << gaps.size() << endl;
        if (g == 0) throw std::logic_error("shit");

//        for (int j = 0; j < gaps.size() - 1; j++) {
//            if (gaps[j + 1] > gaps[j]) throw std::logic_error("shit");
//        }
    }

    return {l, r};
};

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        uint64_t n, k;
        cin >> n >> k;
        auto lr = solve_fast(n, k);
 /*       auto lr_naive = solve_naive(n, k);
        if (lr != lr_naive) {
            cout << "error on case #" << i + 1 << endl;
            cout << " with n = " << n << " and k = " << k <<  endl;
            cout << "expected " << " l = " << lr_naive.first << " r = " << lr_naive.second << endl;
            cout << "actually " << " l = " << lr.first << " r = " << lr.second << endl;
            return 0;
        }*/

        cout << "Case #" << i + 1 << ": " << lr.second << " " << lr.first << endl;
    }

    return 0;
}

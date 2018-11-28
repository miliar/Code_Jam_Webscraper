#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string.h>
#include <utility>
#include <vector>

using namespace std;

using vi = vector<int>;
using vc = vector<char>;
using vd = vector<double>;
using vl = vector<long long>;
using vvi = vector<vector<int>>;
using vvc = vector<vector<char>>;
using vvd = vector<vector<double>>;
using vvl = vector<vector<long long>>;

template <typename T>
auto read()
{
    T i;
    cin >> i;
    return i;
}
auto rc() { return read<char>(); };
auto ri() { return read<int>(); };
auto rd() { return read<double>(); };
auto rl() { return read<long long>(); };
auto rs() { return read<string>(); };

void test_case(int case_num)
{
    auto N = ri();
    auto P = ri();

    vi R(N);
    generate_n(R.begin(), N, ri);

    vvi ingredients(N);
    for (auto i = 0; i < N; ++i) {
        for (auto j = 0; j < P; ++j) {
            ingredients[i].push_back(ri());
        }
        sort(ingredients[i].begin(), ingredients[i].end());
    }

    auto answer = 0;
    auto servings = 1;
    auto done = false;
    while (!done) {
        auto packetsForServing = INT_MAX;
        auto allLow = true;
        for (auto i = 0; i < N; ++i) {
            auto required = servings * R[i];
            auto tmplo = required * 9;
            auto lo = (tmplo / 10) + (tmplo % 10 ? 1 : 0);
            auto hi = required * 11 / 10;
            auto& packets = ingredients[i];

            if (count_if(packets.begin(), packets.end(), [&](auto p) { return p >= lo; }) != 0) {
                allLow = false;
            }

            int possibles = count_if(packets.begin(), packets.end(), [&](auto p) { return p >= lo && p <= hi; });
            packetsForServing = std::min(possibles, packetsForServing);
        }

        answer += packetsForServing;
        if (allLow) {
            break;
        }

        for (auto i = 0; i < N; ++i) {
            auto required = servings * R[i];
            auto tmplo = required * 9;
            auto lo = (tmplo / 10) + (tmplo % 10 ? 1 : 0);
            auto hi = required * 11 / 10;
            auto& packets = ingredients[i];

            for (auto j = 0; j < packetsForServing; ++j) {
                packets.erase(find_if(packets.begin(), packets.end(), [&](auto p) { return p >= lo && p <= hi; }));
            }
        }

        ++servings;
    }

    cout << answer;
}

void run()
{
    auto num_cases = ri();
    cout << fixed << setprecision(7);
    for (auto i = 0; i < num_cases; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        test_case(i);
        cout << endl;
    }
}

// int main() { run(); }

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
auto rul() { return read<unsigned long long>(); };
auto rs() { return read<string>(); };

void test_case(int case_num)
{
    /*
    auto N = ri();
    auto K = ri();

    list<int> gaps = {N};

    for (auto i = 0; i < K; ++i) {
        auto maxGapElement = max_element(gaps.begin(), gaps.end());
        auto& maxGap = *maxGapElement;
        maxGap -= 1;
        auto odd = maxGap % 2;
        maxGap /= 2;
        gaps.insert(maxGapElement, maxGap);
        maxGap += odd;
        for (auto& g: gaps) {
            cout << g << ' ';
        }
        cout << endl;
    }


    auto maxGap = *max_element(gaps.begin(), gaps.end());
    cout << maxGap / 2 << ' ' << (maxGap - 1) / 2;
     */

    auto N = rul();
    auto K = rul();
    auto shift = sizeof(unsigned long long) * 8 - 1;

    while (!((1ull << shift) & K)) {
        --shift;
    }

    map<unsigned long long, unsigned long long> gaps = {{N, 1}};
    for (auto i = 0; i < shift; ++i) {
        map<unsigned long long, unsigned long long> newGaps;
        for (auto& kv : gaps) {
            auto g = kv.first - 1ull;
            auto odd = g % 2ull;
            g /= 2ull;
            if (odd) {
                auto ng = newGaps.find(g);
                if (ng == newGaps.end()) {
                    newGaps[g] = kv.second;
                } else {
                    newGaps[g] += kv.second;
                }
                auto oddg = newGaps.find(g + 1ull);
                if (oddg == newGaps.end()) {
                    newGaps[g + 1ull] = kv.second;
                } else {
                    newGaps[g + 1ull] += kv.second;
                }
            } else {
                auto ng = newGaps.find(g);
                if (ng == newGaps.end()) {
                    newGaps[g] = kv.second * 2ull;
                } else {
                    newGaps[g] += kv.second * 2ull;
                }
            }
        }
        gaps = move(newGaps);
    }

    auto left = ((1ull << shift) ^ K) + 1;
    auto lastGap = gaps.rbegin()->first;

    if (gaps.size() > 1 && left > gaps.rbegin()->second) {
        lastGap = gaps.begin()->first;
    }
    cout << lastGap / 2ull << ' ' << (lastGap - 1) / 2ull;
//    while (shift > 1) {
//        N -= 1;
//        auto odd = N % 2ull;
//        N /= 2ull;
//
//        if ((1ull << shift) & K) {
//            N += odd;
//        }
//
//        --shift;
//    }

//    auto odd = N % 2ull ? 0 : 1;

    //cout << lastGap;
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

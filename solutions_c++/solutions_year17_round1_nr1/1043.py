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
using vs = vector<string>;
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
    auto R = ri();
    auto C = ri();

    vs grid;
    for (auto i = 0; i < R; ++i) {
        grid.push_back(rs());
    }

    auto allqs = ""s;
    for (auto i = 0; i < C; ++i) {
        allqs += "?";
    }

    string lastRow;
    for (auto i = 0; i < R; ++i) {
        if (grid[i] != allqs) {
            lastRow = grid[i];
            break;
        }
    }


    for (auto i = 0; i < R; ++i) {
        if (grid[i] != allqs) {
            lastRow = grid[i];
        } else {
            grid[i] = lastRow;
        }
    }

    for (auto i = grid.begin(); i != grid.end(); ++i) {
        char last = '?';
        for (auto j = 0; j < C; ++j) {
            if ((*i)[j] != '?') {
                last = (*i)[j];
                break;
            }
        }
        for (auto j = 0; j < C; ++j) {
            auto cur = (*i)[j];
            if (cur == '?') {
                (*i)[j] = last;
            } else {
                last = cur;
            }
        }
    }

    for (auto i = 0; i < R; ++i) {
        cout << endl << grid[i];
    }

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

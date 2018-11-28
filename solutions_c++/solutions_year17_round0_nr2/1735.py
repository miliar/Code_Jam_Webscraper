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
    auto nstr = rs();
    vi digits;

    for (auto i = nstr.begin(); i != nstr.end(); i++) {
        digits.push_back(*i - '0');
    }

    auto lasti = 0;
    auto last = 0;
    auto nines = false;
    for (auto i = 0; i < digits.size(); ++i) {
        if (nines) {
            digits[i] = 9;
        }
        else if (digits[i] < last) {
            digits[lasti] -= 1;
            for (auto j = lasti + 1; j < i + 1; ++j) {
                digits[j] = 9;
            }
            nines = true;
        } else if (digits[i] > last) {
            lasti = i;
            last = digits[i];
        }
    }

    auto bzero = true;
    for (auto&& d : digits) {
        if (bzero && d == 0) {
            continue;
        }
        cout << d;
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

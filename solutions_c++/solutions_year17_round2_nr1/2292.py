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

#define For(i,b,e) for(auto i=b; i<e; ++i)

using vi = vector<int>;
using vc = vector<char>;
using vd = vector<double>;
using vl = vector<long long>;
using vs = vector<string>;
using vvi = vector<vector<int>>;
using vvc = vector<vector<char>>;
using vvd = vector<vector<double>>;
using vvl = vector<vector<long long>>;
using vvs = vector<vector<string>>;

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
    auto d = ri();
    auto n = ri();

    //vector<pair<int, int>> horses;
    auto last = 0.0;
    For(i,0,n) {
        auto k = ri();
        auto s = ri();
        last = max(last, static_cast<double>(d - k) / s);
        //horses.push_back(make_pair(ri(), ri()));
    }

    cout << static_cast<double>(d) / last;

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

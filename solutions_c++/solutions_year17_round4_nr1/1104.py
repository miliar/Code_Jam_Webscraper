// Copyright (C) 2017 Sayutin Dmitry.
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License as
// published by the Free Software Foundation; version 3

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program; If not, see <http://www.gnu.org/licenses/>.

#include <iostream>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <set>
#include <map>
#include <array>
#include <queue>
#include <stack>
#include <functional>
#include <utility>
#include <string>
#include <assert.h>
#include <iterator>
#include <cstdint>
#include <cinttypes>
#include <string.h>
#include <random>
#include <numeric>


using std::cin;
using std::cout;
using std::cerr;

using std::vector;
using std::map;
using std::array;
using std::set;
using std::string;

using std::pair;
using std::make_pair;

using std::min;
using std::abs;
using std::max;

using std::unique;
using std::sort;
using std::generate;
using std::reverse;
using std::min_element;
using std::max_element;

#ifdef LOCAL
#define LASSERT(X) assert(X)
#else
#define LASSERT(X) {}
#endif

template <typename T>
T input() {
    T res;
    cin >> res;
    LASSERT(cin);
    return res;
}

template <typename IT>
void input_seq(IT b, IT e) {
    std::generate(b, e, input<typename std::remove_reference<decltype(*b)>::type>);
}

#define SZ(vec)         int((vec).size())
#define ALL(data)       data.begin(),data.end()
#define RALL(data)      data.rbegin(),data.rend()
#define TYPEMAX(type)   std::numeric_limits<type>::max()
#define TYPEMIN(type)   std::numeric_limits<type>::min()

// t1, t2, t3.
int dp[200][200][200];

int solve(vector<int>& people, int p) {
    int num[4] = {0, 0, 0, 0};

    for (int elem: people)
        num[elem % p] += 1;

    auto good = [p](int a, int b, int c) {
        return (1 * a + 2 * b + 3 * c) % p == 0;
    };
    
    for (int i = 0; i <= num[1]; ++i)
        for (int j = 0; j <= num[2]; ++j)
            for (int k = 0; k <= num[3]; ++k) {
                dp[i][j][k] = 0;
                if (i + j + k != 0) {
                    if (i != 0)
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + good(i - 1, j, k));
                    if (j != 0)
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + good(i, j - 1, k));
                    if (k != 0)
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1] + good(i, j, k - 1));
                }
            }
    
    
    return num[0] + dp[num[1]][num[2]][num[3]];
}

int main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    // code here.
    int T = input<int>();
    for (int tc = 1; tc <= T; ++tc) {
        int n = input<int>();
        int p = input<int>();
        vector<int> visit(n);

        input_seq(ALL(visit));

        cout << "Case #" << tc << ": " << solve(visit, p) << "\n";
    }
    
    return 0;
}

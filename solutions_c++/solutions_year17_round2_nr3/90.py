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

#define int int64_t

signed main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cout << std::fixed;
    cout.precision(10);
    
    // code here.
    int T = input<int>();
    for (int tc = 1; tc <= T; ++tc) {
        int N, Q;
        cin >> N >> Q;

        // dist, speed
        vector<pair<int64_t, int64_t>> percity(N);
        for (int i = 0; i != N; ++i)
            cin >> percity[i].first >> percity[i].second;

        vector<vector<int64_t>> dist0(N, vector<int64_t>(N));
        for (int i = 0; i != N; ++i)
            for (int j = 0; j != N; ++j)
                dist0[i][j] = input<int64_t>();

        const double inf = 1e100;
        vector<vector<double>> dist1(N, vector<double>(N, inf));
        // run dijkstra N times

        for (int S = 0; S != N; ++S) {
            vector<int64_t> distS(N, TYPEMAX(int64_t));
            vector<char>    used(N, false);
            distS[S] = 0;
            
            for (int z = 0; z != N; ++z) {
                int pmin = -1;
                for (int pp = 0; pp != N; ++pp)
                    if (not used[pp] and (pmin == -1 or distS[pmin] > distS[pp]))
                        pmin = pp;

                if (distS[pmin] == TYPEMAX(int64_t))
                    break;

                used[pmin] = true;
                for (int go = 0; go != N; ++go)
                    if (dist0[pmin][go] != -1)
                        distS[go] = min(distS[go], distS[pmin] + dist0[pmin][go]);
            }

            for (int z = 0; z != N; ++z)
                if (distS[z] <= percity[S].first)
                    dist1[S][z] = double(distS[z]) / percity[S].second;
        }

        // run mr floyd
        for (int k = 0; k != N; ++k)
            for (int i = 0; i != N; ++i)
                for (int j = 0; j != N; ++j)
                    dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j]);

        cout << "Case #" << tc << ": ";
        for (int i = 0; i != Q; ++i) {
            int s = input<int>() - 1;
            int t = input<int>() - 1;
            cout << dist1[s][t] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}

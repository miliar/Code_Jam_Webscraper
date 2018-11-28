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

vector<char> solve_RYB(int R, int Y, int B) {
    int S = R + Y + B;
    
    if (2 * max(R, max(Y, B)) > S)
        return vector<char>();

    vector<char> ans(S, 0);
    int i = 0;

    auto put_label = [&i, &ans, S](int cnt, char ch) {
        for (int k = 0; k != cnt; ++k) {
            ans[i] = ch;
            i = (i + 2) % S;
            
            if (ans[i] != 0)
                i = (i + 1) % S;
        }
    };
    
    vector<pair<int, char>> list = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
    std::sort(list.begin(), list.end());

    for (int t = 2; t >= 0; --t)
        put_label(list[t].first, list[t].second);
    return ans;
}

string from_vec(vector<char>& v) {
    if (v.empty())
        return "IMPOSSIBLE";
    v.push_back(0);
    return string(v.data());
}

string from_vec2(vector<char> v) {
    if (v.empty())
        return "IMPOSSIBLE";
    v.push_back(0);
    return string(v.data());
}


vector<char> solve_coldwar(int A, char AC, int B, char BC) {
    if (A != B)
        return vector<char>();
    else {
        vector<char> ans(A + B);
        for (int i = 0; i != A; ++i) {
            ans[2 * i]     = AC;
            ans[1 + 2 * i] = BC;
        }
        return ans;
    }
}

map<char, uint32_t> MASKS = {{'R', 1},
                             {'Y', 2},
                             {'B', 4},
                             {'O', 1 + 2},
                             {'G', 2 + 4},
                             {'V', 1 + 4}};

bool validate(const string& a, int N) {
    if (a == "IMPOSSIBLE")
        return true;
    
    if (SZ(a) != N)
        return false;

    for (int i = 0; i != N; ++i) {
        int j = (i + 1) % N;
        
        if (MASKS.count(a[i]) == 0 or MASKS.count(a[j]) == 0)
            return false;
        if (MASKS.find(a[i])->second & MASKS.find(a[j])->second)
            return false;
    }
    return true;
}

vector<char> solve(int N, int R, int O, int Y, int G, int B, int V) {
    if (R + G == N)
        return solve_coldwar(R, 'R', G, 'G');
    if (Y + V == N)
        return solve_coldwar(Y, 'Y', V, 'V');
    if (B + O == N)
        return solve_coldwar(B, 'B', O, 'O');

    if ((G != 0 and G >= R) or (V != 0 and V >= Y) or (O != 0 and O >= B))
        return vector<char>();

    auto RYB = solve_RYB(R - G, Y - V, B - O);
    if (RYB.empty())
        return vector<char>();
    
    vector<char> ans;
    for (char ch: RYB) {
        ans.push_back(ch);

        if (ch == 'R')
            while (G != 0) {
                ans.push_back('G');
                ans.push_back('R');
                G -= 1;
            }
        
        if (ch == 'Y')
            while (V != 0) {
                ans.push_back('V');
                ans.push_back('Y');
                V -= 1;
            }
        
        if (ch == 'B')
            while (O != 0) {
                ans.push_back('O');
                ans.push_back('B');
                O -= 1;
            }
    }
    return ans;
}

vector<char> brute(int R, int O, int Y, int G, int B, int V, vector<char>& cur) {
    if (R != 0) {
        cur.push_back('R');
        auto ans = brute(R - 1, O, Y, G, B, V, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (O != 0) {
        cur.push_back('O');
        auto ans = brute(R, O - 1, Y, G, B, V, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (Y != 0) {
        cur.push_back('Y');
        auto ans = brute(R, O, Y - 1, G, B, V, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (G != 0) {
        cur.push_back('G');
        auto ans = brute(R, O, Y, G - 1, B, V, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (B != 0) {
        cur.push_back('B');
        auto ans = brute(R, O, Y, G, B - 1, V, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (V != 0) {
        cur.push_back('B');
        auto ans = brute(R, O, Y, G, B, V - 1, cur);
        cur.pop_back();
        
        if (not ans.empty())
            return ans;
    }

    if (R + O + Y + G + B + V == 0) {
        cur.push_back(0);
        bool b = validate(string(cur.data()), SZ(cur) - 1);
        cur.pop_back();
        
        if (b)
            return cur;
    }

    return vector<char>();
}

vector<char> solve_stupid(int N, int R, int O, int Y, int G, int B, int V) {
    vector<char> cur;
    return brute(R, O, Y, G, B, V, cur);
}

int main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    for (int i = 0; i != 0; ++i) {
        std::mt19937 rnd;
        int R = rnd() % 6;
        int O = rnd() % 6;
        int Y = rnd() % 6;
        int G = rnd() % 6;
        int B = rnd() % 6;
        int V = rnd() % 6;

        if (R + O + Y + G + B + V == 0)
            continue;

        auto ans1 = from_vec2(solve_stupid(R + O + Y + G + B + V, R, O, Y, G, B, V));
        auto ans2 = from_vec2(solve(R + O + Y + G + B + V, R, O, Y, G, B, V));

        assert(validate(ans1, R + O + Y + G + B + V));
        assert(validate(ans2, R + O + Y + G + B + V));
        assert((ans1 == "IMPOSSIBLE") == (ans2 == "IMPOSSIBLE"));
        cerr << "TESTS PASSED\n";
    }
    
    int tests = input<int>();
    for (int t = 1; t <= tests; ++t) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        assert(N == R + O + Y + G + B + V);
        auto tmp = solve(N, R, O, Y, G, B, V);
        string ans = from_vec(tmp);
        if (not validate(ans, N)) {
            solve(N, R, O, Y, G, B, V);
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    
    return 0;
}

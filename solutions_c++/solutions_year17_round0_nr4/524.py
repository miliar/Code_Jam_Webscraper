
#include <iostream>
#include <iomanip>
#include <fstream>

#include <string>
#include <sstream>

#include <vector>
#include <queue>
#include <set>
#include <map>

#include <algorithm>
#include <limits>

#include <cctype>
#include <cassert>


#include <utility>
#include <numeric>
#include <tuple>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <map>

#include <queue>

template<typename T>
using Vector2D = std::vector<std::vector<T>>;

template<typename T>
using Vector3D = std::vector<Vector2D<T>>;

using PairInt = std::pair<int, int>;
using PairInt64 = std::pair<int64_t, int64_t>;

using MapInt = std::map<int, int>;
using MMapInt = std::multimap<int, int>;
using MapInt64 = std::map<int64_t, int64_t>;
using MMapInt64 = std::multimap<int64_t, int64_t>;
using UMapIntString = std::unordered_map<int, std::string>;
using SetInt = std::set<int>;
using SetPairInt64 = std::set<PairInt64>;

using VectorInt = std::vector<int>;
using VectorInt2D = Vector2D<int>;
using VectorInt64 = std::vector<int64_t>;
using VectorUInt64 = std::vector<uint64_t>;
using VectorInt642D = Vector2D<int64_t>;

using VectorChar = std::vector<char>;
using VectorChar2D = Vector2D<char>;
using VectorString = std::vector<std::string>;

using QueuePairInt = std::queue<PairInt>;
using QueueInt = std::queue<int>;

using VectorPairInt = std::vector<PairInt>;
using VectorPairInt64 = std::vector<PairInt64>;
using VectorPairInt2D = Vector2D<PairInt>;
using SetInt = std::set<int>;
using MSetInt = std::multiset<int>;
using UMapChar = std::map<char, int>;

using ListInt = std::list<int>;
using VectorListInt = std::vector<ListInt>;
using VectorDouble = std::vector<double>;
using VectorDouble2D = Vector2D<double>;

void init() {

}

void fill_t(VectorString& grid_t, bool up) {
    int sz = grid_t.size();
    int r_start = up ? (sz - 1) : 1;
    int r_dir = up ? -1 : 1;
    int r_finish = up ? -1 : sz;
    for (int i = 1; i < sz; ++i) {
        bool has_t = false;
        int c = i;
        int r = r_start;
        for (; !has_t && r != r_finish && c < sz; r += r_dir, ++c) {
            has_t = grid_t[r][c] != '.';
        }
        c = i;
        r = r_start;
        for (; !has_t && r != r_finish && c >= 0; r += r_dir, --c) {
            has_t = grid_t[r][c] != '.';
        }
        if (!has_t) {
            grid_t[r_start][i] = '+';
        }
    }
}

void fill_x(VectorString& grid_x) {
    VectorString busy = grid_x;
    int sz = grid_x.size();
    for (int r = 1; r < sz; ++r) {
        auto p = grid_x[r].find('x');
        if (p != std::string::npos) {
            busy[r] = std::string(sz, 'x');
            for (int i = 0; i < sz; ++i) {
                busy[i][p] = 'x';
            }
        }
    }

    for (int r = 1; r < sz; ++r) {
        for (int c = 1; c < sz; ++c) {
            if (busy[r][c] != 'x') {
                busy[r] = std::string(sz, 'x');
                for (int i = 0; i < sz; ++i) {
                    busy[i][c] = 'x';
                }
                grid_x[r][c] = 'x';
                break;
            }
        }
    }
}


void task(int ti) {
    int n;
    int m;
    std::cin >> n >> m;
    VectorString grid(n + 1, std::string(n + 1, '.'));
    VectorString grid_x(n + 1, std::string(n + 1, '.'));
    VectorString grid_t(n + 1, std::string(n + 1, '.'));

    for (int i = 0; i < m; ++i) {
        char t;
        int r;
        int c;
        std::cin >> t >> r >> c;
        switch (t) {
        case 'x':
            grid[r][c] = grid_x[r][c] = 'x';
            break;
        case '+':
            grid[r][c] = grid_t[r][c] = '+';
            break;
        case 'o':
            grid_x[r][c] = 'x';
            grid_t[r][c] = '+';
            grid[r][c] = 'o';
            break;
        }
    }

    fill_t(grid_t, false);
    fill_t(grid_t, true);
    fill_x(grid_x);

    VectorString grid_m(n + 1, std::string(n + 1, '.'));
    int score = 0;
    int update = 0;
    std::string ans;
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= n; ++c) {
            if (grid_t[r][c] == '+' && grid_x[r][c] == 'x') {
                grid_m[r][c] = 'o';
                score += 2;
            }
            else if (grid_t[r][c] == '+') {
                grid_m[r][c] = '+';
                ++score;
            }
            else if (grid_x[r][c] == 'x') {
                grid_m[r][c] = 'x';
                ++score;
            }

            if (grid[r][c] != grid_m[r][c]) {
                ans += grid_m[r][c];
                ans += " " + std::to_string(r) + " " + std::to_string(c) + "\n";
                ++update;
            }
        }
    }

    ans = std::to_string(score) + " " + std::to_string(update) + "\n" + ans;
#if 0
    for (int r = 1; r <= n; ++r) {
        std::cout << "\n" << grid_m[r].substr(1);
    }
    std::cout << "\n\n";
#endif
    std::cout << "Case #" << ti << ": " << ans;
}

int main() {
    std::ios::sync_with_stdio(false);

    std::ifstream in(IN_TXT_ABSPATH);
    std::cin.rdbuf(in.rdbuf());
#if 1
    std::ofstream out(OUT_TXT_ABSPATH);
    std::cout.rdbuf(out.rdbuf());
#endif

    init();

    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        task(i + 1);
    }

    return 0;
}


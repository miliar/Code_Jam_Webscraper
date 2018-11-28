
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


void task(int ti) {
    int n;
    int r;
    int o;
    int y;
    int g;
    int b;
    int v;
    std::cin >> n >> r >> o >> y >> g >> b >> v;
    VectorString s = {
        std::string(r, 'R'),
        std::string(y, 'Y'),
        std::string(b, 'B')
    };
    std::sort(s.begin(), s.end(), [](const std::string& s1, const std::string& s2) {
        return s1.length() > s2.length();
    });
    std::string s2 = s[0] + s[1] + s[2];

    int len = s.front().length();
    std::string ans(len * 3, '0');
    size_t k = 0;
    for (int j = 0; j < 3; ++j) {
        for (int i = 0; i < len; ++i) {
            if (k >= s2.length()) {
                break;
            }
            ans[i * 3 + j] = s2[k++];
        }
        if (k >= s2.length()) {
            break;
        }
    }
    ans.erase(std::remove(ans.begin(), ans.end(), '0'), ans.end());
    bool is_imp = false;
    for (size_t i = 1; i < ans.length(); ++i) {
        if (ans[i - 1] == ans[i]) {
            is_imp = true;
            break;
        }
    }
    is_imp = is_imp || ans.front() == ans.back();

    std::cout << "Case #" << ti << ": ";
    if (is_imp) {
        std::cout << "IMPOSSIBLE\n";
    }
    else {
        std::cout << ans << "\n";
    }
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


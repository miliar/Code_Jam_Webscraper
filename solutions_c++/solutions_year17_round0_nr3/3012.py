#define NDEBUG
NDEBUG


#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <memory>
#include <queue>
#include <random>


#define forn(t, i, n) for (t i = 0; i < (n); ++i)


using namespace std;

/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);


// Section with adoption of array and vector algorithms.


// 32 bit ints (sum LSB + MSB == 32)


// TODO: Section with some container algorithms


namespace template_util {
    

    constexpr int bytecount(uint64_t x) {
        return x ? 1 + bytecount(x >> 8) : 0;
    }

    /// caide keep
    template<int N>
    struct bytetype {
        
    };

    /// caide keep
    template<>
    struct bytetype<4> {
        
    };

    /// caide keep
    template<>
    struct bytetype<3> {
        
    };

    /// caide keep
    template<>
    struct bytetype<2> {
        
    };

    /// caide keep
    template<>
    struct bytetype<1> {
        
    };

    /// caide keep
    template<>
    struct bytetype<0> {
        
    };

    /// caide keep
    template<uint64_t N>
    struct minimal_uint : bytetype<bytecount(N)> {
    };
}


template<class T>
T next(istream& in) {
    T ret;
    in >> ret;
    return ret;
}


namespace hash_util_detail {
    template<class T>
    inline void hash_combine(size_t &seed, T const &v) {
        static std::hash<T> h;
        seed ^= h(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
    }

    
}

namespace std {
    

    template<class U, class V>
    struct hash<pair<U, V>> {
        std::size_t operator()(pair<U, V> const& p) const {
            size_t seed = 0;
            hash_util_detail::hash_combine(seed, p.first);
            hash_util_detail::hash_combine(seed, p.second);
            return seed;
        }
    };

    
}

unordered_map<pair<int64_t, int64_t>, int64_t> cache;

int64_t cnt(int64_t n, int64_t min) {
    if (cache.count({n, min})) {
        return cache[{n, min}];
    }
    assert(n == 0 || n == 1 + n / 2 + (n - 1) / 2);
    int64_t ret = (n < min ? 0 : 1 + cnt(n / 2, min) + cnt((n - 1) / 2, min));
    return cache[{n, min}] = ret;
}

void solveTest(istream& in, ostream& out) {
    int64_t n = next<int64_t>(in);
    int64_t k = next<int64_t>(in);
    int64_t l = 0, r = n + 1;
    while (l + 1 < r) {
        int64_t mid = (l + r) / 2;
        if (cnt(n, mid) < k) {
            r = mid;
        } else {
            l = mid;
        }
    }
    out << l / 2 << " " << (l - 1) / 2 << endl;
}

void solve(istream& in, ostream& out) {
    int test = next<int>(in);
    forn (int, t, test) {
        out << "Case #" << (t + 1) << ": ";
        solveTest(in, out);
    }
}


int main(int argc, char* argv[]) {
    solve(cin, cout);
    return 0;
}


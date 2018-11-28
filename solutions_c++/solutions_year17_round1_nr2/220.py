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


#define all(c) c.begin(), c.end()


using namespace std;

/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);

template<class T>
inline T mn(T arg) {
    return arg;
}


template<class T>
inline T mx(T arg) {
    return arg;
}


template<class T, class... Args>
inline bool rmn(T &to, Args... args) {
    auto v = mn(args...);
    if (to > v) {
        to = v;
        return true;
    }
    return false;
}

template<class T, class... Args>
inline bool rmx(T &to, Args... args) {
    auto v = mx(args...);
    if (to < v) {
        to = v;
        return true;
    }
    return false;
}


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

template<class T>
vector<T> next_vector(istream& in, size_t n) {
    vector<T> ret(n);
    for (size_t i = 0; i < n; ++i) {
        ret[i] = next<T>(in);
    }
    return ret;
}


#define dbg(...) ;


void solveTest(istream& in, ostream& out) {
    int n = next<int>(in);
    int p = next<int>(in);
    auto rs = next_vector<int>(in, n);
    vector<vector<pair<int, int>>> ranges(n);
    dbg("here");
    forn (int, i, n) {
        forn (int, j, p) {
            int x = next<int>(in);
            // 11 * l * rs[i] >= 10 * x
            int l = (10 * x + 11 * rs[i] - 1) / (11 * rs[i]);
            // 9 * r * rs[i] > 10 * x
            int r = (10 * x) / (9 * rs[i]) + 1;
            if (l < r) {
                ranges[i].emplace_back(l, r);
            }
        }
        sort(all(ranges[i]));
    }
    int ans = 0;
    vector<int> its(n);
    while (true) {
//        dbg(ranges, its);
        int maxl = 1, minr = 1000000000, minlAt = 0;
        forn (int, i, n) {
            if (its[i] >= ranges[i].size()) {
                goto next;
            }
            rmx(maxl, ranges[i][its[i]].first);
            rmn(minr, ranges[i][its[i]].second);
            if (ranges[i][its[i]].first < ranges[minlAt][its[minlAt]].first) {
                minlAt = i;
            }
        }
        if (maxl < minr) {
            ans++;
            forn (int, i, n) {
                its[i]++;
            }
        } else {
            its[minlAt]++;
        }
    }
    next:;
    out << ans << "\n";
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


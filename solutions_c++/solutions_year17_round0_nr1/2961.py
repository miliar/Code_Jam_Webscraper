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


void solveTest(istream& in, ostream& out) {
    string s = next<string>(in);
    int k = next<int>(in);
    int ans = 0;
    forn (int, i, s.length() - k + 1) {
        if (s[i] == '-') {
            ans++;
            forn (int, j, k) {
                s[i + j] = '-' + '+' - s[i + j];
            }
        }
    }
    forn (int, i, s.length()) {
        if (s[i] != '+') {
            out << "IMPOSSIBLE\n";
            return;
        }
    }
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


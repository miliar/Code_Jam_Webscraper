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
#define foran(t, i, a, n) for (t i = (a); i < (n); ++i)


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

template<class T>
vector<T> next_vector(istream& in, size_t n) {
    vector<T> ret(n);
    for (size_t i = 0; i < n; ++i) {
        ret[i] = next<T>(in);
    }
    return ret;
}


void solveTest(istream& in, ostream& out) {
    int n = next<int>(in);
    int m = next<int>(in);
    vector<string> f = next_vector<string>(in, n);
    std::function<void(int, int, int, int)> fill = [&](int i0, int i1, int j0, int j1) {
        int x0 = -1, y0 = -1, x1 = -1, y1 = -1;
        foran (int, i, i0, i1) {
            foran (int, j, j0, j1) {
                if (f[i][j] != '?') {
                    if (x0 == -1) {
                        x0 = i;
                        y0 = j;
                    }
                    x1 = i;
                    y1 = j;
                }
            }
        }
        if (x0 == x1 && y0 == y1) {
            foran (int, i, i0, i1) {
                foran (int, j, j0, j1) {
                    f[i][j] = f[x0][y0];
                }
            }
        } else if (x0 != x1) {
            fill(i0, (x0 + x1) / 2 + 1, j0, j1);
            fill((x0 + x1) / 2 + 1, i1, j0, j1);
        } else {
            fill(i0, i1, j0, (y0 + y1) / 2 + 1);
            fill(i0, i1, (y0 + y1) / 2 + 1, j1);
        }
    };
    fill(0, n, 0, m);
    out << "\n";
    for (auto& s : f) {
        out << s << "\n";
    }
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


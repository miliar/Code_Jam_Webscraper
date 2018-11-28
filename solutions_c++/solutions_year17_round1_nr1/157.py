#define NDEBUG
NDEBUG


#include <algorithm>
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
#include <random>

#define FOR(i, n) for (int i = 0; i < (n); ++i)


using namespace std;

// TC_REMOVE_BEGIN
/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);
// TC_REMOVE_END


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


int n, m;
char f[55][55];

void solveTest(istream& in, ostream& out) {
    FOR(i, n) {
        FOR(j, m) if (j) {
            if (f[i][j] == '?' && f[i][j-1] != '?') {
                f[i][j] = f[i][j-1];
            }
        }
        for (int j = m-2; j >= 0; --j) {
            if (f[i][j] == '?' && f[i][j+1] != '?') {
                f[i][j] = f[i][j+1];
            }
        }
    }
    vector<int> has_letter(n, 0);
    FOR(i, n) {
        FOR(j, m) {
            if (f[i][j] != '?') {
                has_letter[i] = 1;
                break;
            }
        }
    }
    FOR(i, n) {
        if (has_letter[i]) {
            for (int j = i-1; j >= 0; --j) {
                if (has_letter[j]) break;
                FOR(c, m) {
                    f[j][c] = f[i][c];
                }
                has_letter[j] = 1;
            }
            for (int j = i+1; j < n; ++j) {
                if (has_letter[j]) break;
                FOR(c, m) {
                    f[j][c] = f[i][c];
                }
                has_letter[j] = 1;
            }
        }
    }
    out << endl;
    FOR(i, n) {
        FOR(j, m) {
            out << f[i][j];
        }
        out << endl;
    }
}

void inputData(istream& in) {
    n = next<int>(in);
    m = next<int>(in);
    FOR(i, n) {
        string t = next<string>(in);
        FOR(j, m) {
            f[i][j] = t[j];
        }
    }
}

void solve(istream& in, ostream& out, const int test_id = -1) {
    int test = next<int>(in);
    FOR(t, test) {
        inputData(in);
        if (t == test_id || test_id == -1) {
            out << "Case #" << t + 1 << ": ";
            solveTest(in, out);
        }
    }
}
#include <fstream>


int main(int argc, char* argv[]) {
    if (argc == 0) {
        solve(cin, cout);
    } else {
        ifstream in("in.txt");
        int test_id = stoi(argv[1]);
        solve(in, cout, test_id);
    }
    return 0;
}


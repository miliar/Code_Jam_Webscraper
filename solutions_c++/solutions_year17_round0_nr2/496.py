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


typedef int64_t int64;


using namespace std;

// TC_REMOVE_BEGIN
/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);
// TC_REMOVE_END


int64 parseInt64(const string& s) {
    return stoll(s);
}


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


int64 n;
string ns;

int64 build(string prefix, int last_digit, int rest_len) {
    FOR(i, rest_len) {
        prefix.push_back((char)('0' + last_digit));
    }
    return parseInt64(prefix);
}

void solveIt(int len, ostream& out) {
    string result;
    int lst = 1;
    while (len--) {
        for (int d = lst; d <= 9; ++d) {
            int64 x = build(result, d, len + 1);
            if (x <= n) {
                lst = d;
            } else {
                break;
            }
        }
        result.push_back((char)('0' + lst));
    }
    out << result << endl;
}

void solveTest(istream& in, ostream& out) {
    ns = to_string(n);
    if (build("", 1, ns.length()) <= n) {
        solveIt(ns.length(), out);
    } else {
        solveIt(ns.length() - 1, out);
    }
}

void inputData(istream& in) {
    n = next<int64>(in);
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


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


#define all(c) c.begin(), c.end()


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


string s;
int k;

int try1(string s) {
    int res = 0;
    for (int begin = 0, end = k; end <= s.length(); ++begin, ++end) {
        if (s[begin] == '-') {
            for (int j = begin; j < end; ++j) {
                s[j] = s[j] == '+' ? '-' : '+';
            }
            ++res;
        }
    }
    FOR(i, s.length()) {
        if (s[i] == '-') {
            return 1000000;
        }
    }
    return res;
}

void solveTest(istream& in, ostream& out) {
    int res1 = try1(s);
    reverse(all(s));
    int res2 = try1(s);
    res1 = min(res1, res2);
    if (res1 >= 1000000) {
        out << "IMPOSSIBLE\n";
    } else {
        out << res1 << endl;
    }
}

void inputData(istream& in) {
    s = next<string>(in);
    k = next<int>(in);
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


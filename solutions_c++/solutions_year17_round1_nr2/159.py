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

template<class T>
vector<T> next_vector(istream& in, size_t n) {
    vector<T> ret(n);
    for (size_t i = 0; i < n; ++i) {
        ret[i] = next<T>(in);
    }
    return ret;
}


int n, n_packs;
vector<int> grams_need;
vector<vector<int>> grams_have;

void solveTest(istream& in, ostream& out) {
    FOR(i, n) {
        sort(all(grams_have[i]));
    }
    int res = 0;
    vector<int> need(n);
    FOR(j, n) {
        need[j] += grams_need[j];
    }
    while (true) {
        bool done = false;
        bool can_not = false;

        FOR(j, n) {
            while (!grams_have[j].empty()) {
                int gh = grams_have[j][0];
                //   0.9 * need[j] <= gh <= 1.1 * need[j]
                // 10gh < 9 * need
                if (10 * gh < 9 * need[j]) {
                    grams_have[j].erase(grams_have[j].begin());
                } else if (10 * gh > 11 * need[j]) {
                    can_not = true;
                    break;
                } else {
                    break;
                }
            }
            if (grams_have[j].empty()) {
                done = true;
                break;
            }
            if (can_not) {
                break;
            }

        }
        if (can_not) {
            FOR(j, n) {
                need[j] += grams_need[j];
            }
            continue;
        }
        if (done) break;
        ++res;
        FOR(j, n) grams_have[j].erase(grams_have[j].begin());
    }
    out << res << endl;
}

void inputData(istream& in) {
    n = next<int>(in);
    n_packs = next<int>(in);
    grams_need.clear();
    grams_have.clear();
    grams_need = next_vector<int>(in, n);
    grams_have.resize(n);
    FOR(i, n) {
        grams_have[i] = next_vector<int>(in, n_packs);
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


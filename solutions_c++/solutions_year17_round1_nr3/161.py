#include <deque>


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


const int INF = 1000000000;
int hd, ad, hk, ak, b, d;

int dst[101][101][101][101];
deque<pair<pair<int, int>, pair<int, int>>> q;

void solveTest(istream& in, ostream& out) {
    q.clear();
    FOR(i, 101) FOR(j, 101) FOR(k, 101) FOR(p, 101) {
        dst[i][j][k][p] = INF;
    }
    dst[hd][ad][hk][ak] = 0;
    q.push_back({{hd, ad}, {hk, ak}});
    int best = INF;
    while (!q.empty()) {
        pair<pair<int, int>, pair<int, int>> st = q.front();
        q.pop_front();
        int chd = st.first.first;
        int cad = st.first.second;
        int chk = st.second.first;
        int cak = st.second.second;
        int cur = dst[chd][cad][chk][cak];
        if (chd == 0) continue;
        if (chk == 0) {
            best = min(best, cur);
            continue;
        }
        // we attack
        int nhd = chd;
        int nad = cad;
        int nhk = max(0, chk - cad);
        int nak = cak;
        if (nhk > 0) {
            nhd -= nak;
        }
        if (nhd > 0) {
            if (dst[nhd][nad][nhk][nak] > cur + 1) {
                dst[nhd][nad][nhk][nak] = cur + 1;
                q.push_back({{nhd, nad}, {nhk, nak}});
            }
        }

        // we buff
        nhd = chd;
        nad = min(cad + b, 100);
        nhk = chk;
        nak = cak;
        if (nhk > 0) {
            nhd -= nak;
        }
        if (nhd > 0) {
            if (dst[nhd][nad][nhk][nak] > cur + 1) {
                dst[nhd][nad][nhk][nak] = cur + 1;
                q.push_back({{nhd, nad}, {nhk, nak}});
            }
        }

        // we cure
        nhd = hd;
        nad = cad;
        nhk = chk;
        nak = cak;
        if (nhk > 0) {
            nhd -= nak;
        }
        if (nhd > 0) {
            if (dst[nhd][nad][nhk][nak] > cur + 1) {
                dst[nhd][nad][nhk][nak] = cur + 1;
                q.push_back({{nhd, nad}, {nhk, nak}});
            }
        }

        // we debuff
        nhd = chd;
        nad = cad;
        nhk = chk;
        nak = max(0, cak - d);
        if (nhk > 0) {
            nhd -= nak;
        }
        if (nhd > 0) {
            if (dst[nhd][nad][nhk][nak] > cur + 1) {
                dst[nhd][nad][nhk][nak] = cur + 1;
                q.push_back({{nhd, nad}, {nhk, nak}});
            }
        }
    }

    if (best >= INF) {
        out << "IMPOSSIBLE\n";
        return;
    }
    out << best << endl;
}

void inputData(istream& in) {
    hd = next<int>(in);
    ad = next<int>(in);
    hk = next<int>(in);
    ak = next<int>(in);
    b = next<int>(in);
    d = next<int>(in);
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


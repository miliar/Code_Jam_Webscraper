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

template<class T>
inline T mn(T arg) {
    return arg;
}


template<class T>
inline T mx(T arg) {
    return arg;
}

template<class T, class... Ts>
inline typename common_type<T, Ts...>::type mx(T arg, Ts... args) {
    auto arg1 = mx(args...);
    return arg > arg1 ? arg : arg1;
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


#define dbg(...) ;


void solveTest(istream& in, ostream& out) {
    int64_t hd = next<int64_t>(in);
    int64_t ad = next<int64_t>(in);
    int64_t hk = next<int64_t>(in);
    int64_t ak = next<int64_t>(in);
    int64_t b = next<int64_t>(in);
    int64_t d = next<int64_t>(in);
    int64_t ca = (hk + ad - 1) / ad;
    forn (int64_t, bs, 100000) {
        int64_t ad1 = ad + b * bs;
        rmn(ca, bs + (hk + ad1 - 1) / ad1);
    }
    vector<int64_t> dsCandidates = {0}; // (hd - 1) >= (cur + 1) * (ak - d * ds)
    while (d > 0 && d * dsCandidates.back() < ak) {
        int64_t cur = (hd - 1) / (ak - d * dsCandidates.back());
        int64_t l = dsCandidates.back(), r = 2000000000LL;
        while (l + 1 < r) {
            int64_t mid = (l + r) / 2;
            int64_t midCur = ak - d * mid <= 0 ? 1000000000000000000LL : (hd - 1) / (ak - d * mid);
            if (midCur == cur) {
                l = mid;
            } else {
                r = mid;
            }
        }
        dsCandidates.push_back(r);
    }
    dbg(dsCandidates, ca);
    int64_t ans = 1000000000000000000LL;
//    int64_t processedDs = 0, processedOverhead = 0;
//    int64_t curak = ak, curh = hd;
    for (auto ds : dsCandidates) {
//        bool inf = false;
//        if (ak <= d * ds) {
//            inf = true;
//            ds--;
//        }
//        while (true) {
//            int64_t curr = f(curh, curak, d, ds - processedDs);
//            if (curr >= ds) {
//                break;
//            }
//            int64_t l = 0, r = curh == hd ? 2 : (ds - processedDs) / curr + 1;
//            while (l + 1 < r) {
//                int64_t mid = (l + r) / 2;
//                if (f(curh, curak - (mid - 1) * curr * d, d, curr) > curr) {
//                    r = mid;
//                } else {
//                    l = mid;
//                }
//            }
//            processedDs += curr * l;
//            processedOverhead += l;
//            curak -= d * curr;
//            if (curh == hd) {
//                curh = hd - curak;
//            }
//        }
//        int64_t l = -1, r = 2000000000LL;
//        while (l + 1 < r) {
//            int64_t mid = (l + r) / 2;
//
//        }
//        if (r < 2000000000LL) {
//            rmn(ans, ca + ds + l);
//        }
        int64_t curAns = 0, curCa = ca, curh = hd, cura = ak;
        bool healed = false;
        while (curCa > 0) {
            curAns++;
            if (ds > 0 && curh > mx(0, cura - d)) {
                healed = false;
                cura = mx(0, cura - d);
                curh -= cura;
                ds--;
            } else if (curh > cura || curCa == 1) {
                healed = false;
                curCa--;
                curh -= cura;
            } else {
                if (healed) {
                    break;
                }
                curh = hd - cura;
                healed = true;
            }
        }
        if (!healed) {
            rmn(ans, curAns);
        }
    }
    if (ans == 1000000000000000000LL) {
        out << "IMPOSSIBLE\n";
        return;
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


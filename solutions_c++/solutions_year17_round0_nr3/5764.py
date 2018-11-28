#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

template<typename T>
using mat = vector<vector<T>>;

template<typename T>
using lim = numeric_limits<T>;

#define mod 1000000007
#define fst first
#define snd second
#define ALL(x) (x).begin(), (x).end()
#define RFOR(i, a, n) for (int64_t i = (a - 1); i >= (n); --i)
#define FOR(i, a, n) for (int64_t i = (a); i < (n); ++i)
#define pb push_back
#define nx_perm next_permutation
#define sz size
#define PI 3.14159265358979323846264
/****************************************/

pair<uint64_t, uint16_t> solve(long n, long k)
{
    set<uint64_t> ary;
    pair<uint64_t, uint64_t> ret{0, 0};
    ary.insert(0);
    ary.insert(n + 1);
    auto b = ary.begin();
    auto e = ary.end();
    --e;
    FOR(i, 1, k) {
        uint64_t d = 0;
        uint64_t mid = 0;
        for (auto i = b; i != e; ++i) {
            auto nx = i;
            ++nx;
            ///uint64_t mx = lim<long>::min();
            uint64_t c = *nx - *i;
            //uint64_t mid = *i + (*nx - *i) / 2;
            if (c > d) {
                d = c;
                mid = *i + (*nx - *i) / 2;
            }

            //if (l > ret.fst && r > ret.fst)

                //    }

        }
        ary.insert(mid);
    }
    uint64_t d = 0;
    uint64_t mid;
    for (auto i = b; i != e; ++i) {
        auto nx = i;
        ++nx;
        //uint64_t mx = lim<long>::min();
        uint64_t c = *nx - *i;
        //uint64_t mid = *i + (*nx - *i) / 2;
        d = max(d, c);
        /*
          if (l > ret.fst && r > ret.fst)

          }
        */
    }
#ifdef DEBUG
    for_each(ALL(ary), [](auto n) { cout << n << ' '; });
    cout << endl;
#endif
    mid = d / 2;
    ret.fst = d - mid - 1;
    ret.snd = mid - 1;
    return ret;
}

int main()
{
    int t;
    cin >> t;
    FOR(i, 0, t) {
        long n, k;
        cin >> n >> k;
        pair<uint16_t, uint16_t> lr = solve(n, k);

        cout << "Case #" << i + 1 << ": " << lr.fst << ' ' << lr.snd << endl;
    }
}

#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdint.h>
#include <string.h>

#include <unordered_set>

//#define _USE_MATH_DEFINES
//#include <math.h>

#define M_PI 3.14159265358979323846


#include <vector>
#include <list>

#include <set>
#include <map>

#include <unordered_map>

#include <queue>

#include <string>

#include <vector>

#define sqr(x) (x) * (x)

#include <algorithm>
#include <functional>

#include <bitset>

#include <functional>

typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int64_t i64;

typedef uint16_t u16;
typedef int16_t i16;

typedef uint8_t u8;
typedef int8_t i8;


using namespace std;

struct less_key
{
    bool operator() (pair<i64, i64> p1, pair<i64, i64> p2)
    {
        return (p1.first > p2.first) || ((p1.first == p2.first) && (p1.second < p2.second));
    }
};

struct pair_hash
{
    std::size_t operator()(const pair<i64, i64>& k) const
    {
        return static_cast<size_t>(k.first ^ k.second);
    }
};

const i64 mod = 100000000007ll;
const i64 inf = 10000000000000007ll;

i64 T;

i64 r[52];
i64 q[52][52];


bool check(i64 r, i64 q, i64 x) {
    return 10 * q >= 9 * r * x;
}

bool check2(i64 r, i64 q, i64 x) {
    return 10 * q <= 11 * r * x;
}

i64 solve(i64 r, i64 q) {
    i64 x = (10 * q) / (9 * r);
    for (i64 t = x + 1; t >= x - 1; t--) {
        if (check(r, q, t)) {
            return max(t, 0ll);
        }
    }
    return 0;
}

i64 solve2(i64 r, i64 q) {
    i64 x = (10 * q) / (11 * r);
    for (i64 t = x - 1; t <= x + 1; t++) {
        if (check2(r, q, t)) {
            return max(t, 0ll);
        }
    }
}




int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        vector<pair<i64, i64> > a[52];

        map<i64, set<i64>> o[52];
        map<i64, set<i64>> c[52];

        i64 n, p;
        cin >> n >> p;

        for (i64 i = 1; i <= n; i++) {
            cin >> r[i];
        }

        for (i64 i = 1; i <= n; i++) {
            for (i64 j = 1; j <= p; j++) {
                cin >> q[i][j];
            }
        }

        for (i64 i = 1; i <= n; i++) {
            for (i64 j = 1; j <= p; j++) {
                i64 tmin = solve2(r[i], q[i][j]);
                i64 tmax = solve(r[i], q[i][j]);
                if (tmin > tmax) {
                    continue;
                }
                a[i].push_back(make_pair(tmin, tmax));
            }
        }

        for (i64 i = 1; i <= n; i++) {
            sort(a[i].begin(), a[i].end());
            for (i64 j = 0; j < a[i].size(); j++) {
                o[i][a[i][j].first].insert(j);
                c[i][a[i][j].second].insert(j);
            }
        }

        i64 R = 0;
        for (i64 k = 0; k < a[1].size(); k++) {
            vector<i64> tr;
            for (i64 i = 1; i <= n; i++) {
                tr.push_back(-1);
            }
            for (i64 i = 2; i <= n; i++) {
                auto cid = c[i].lower_bound(a[1][k].first);
                if (cid == c[i].end()) {
                    continue;
                }
                auto oid = o[i].upper_bound(a[1][k].second);
                if (oid == o[i].begin()) {
                    continue;
                }
                --oid;
                if (*cid->second.begin() <= *oid->second.rbegin()) {
                    tr[i - 1] = *cid->second.begin();
                }
            }
            bool f = true;
            for (i64 i = 1; i < n; i++) {
                if (tr[i] == -1) {
                    f = false;
                    break;
                }
            }

            if (f) {
                R++;
                for (i64 i = 1; i < n; i++) {
                    o[i + 1][(a[i + 1][tr[i]].first)].erase(tr[i]);
                    if (!o[i + 1][(a[i + 1][tr[i]].first)].size()) {
                        o[i + 1].erase(a[i + 1][tr[i]].first);
                    }
                    c[i + 1][a[i + 1][tr[i]].second].erase(tr[i]);
                    if (!c[i + 1][a[i + 1][tr[i]].second].size()) {
                        c[i + 1].erase(a[i + 1][tr[i]].second);
                    }
                }
            }
        }

        cout << "Case #" << tt << ": " << R << endl;
    }

    return 0;
}
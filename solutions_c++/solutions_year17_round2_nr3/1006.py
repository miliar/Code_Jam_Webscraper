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

const i64 N = 1004;

i64 e[N];
i64 s[N];

i64 d[N][N];

double r[N];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        i64 n, q;

        cin >> n >> q;

        for (i64 i = 1; i <= n; i++) {
            r[i] = -1.0;
        }

        for (i64 i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }

        for (i64 i = 1; i <= n; i++) {
            for (i64 j = 1; j <= n; j++) {
                cin >> d[i][j];
            }
        }

        vector<pair<i64, i64> > w;
        for (i64 i = 1; i <= q; i++) {
            pair<i64, i64> z;
            cin >> z.first >> z.second;
            w.push_back(z);
        }


        r[n] = 0.0;
        for (i64 i = n - 1; i > 0; i--) {
            r[i] = -1.0;
            i64 cd = 0;
            for (i64 j = i + 1; i <= n; j++) {
                cd += d[j - 1][j];
                if (cd > e[i]) {
                    break;
                }
                if (r[j] < 0) {
                    continue;
                }
                double tr = r[j] + (double)cd / s[i];
                if (r[i] < 0 || tr < r[i]) {
                    r[i] = tr;
                }
            }
        }

        cout << "Case #" << tt << ": " << setprecision(9) << fixed << r[1] << endl;
    }

    return 0;
}
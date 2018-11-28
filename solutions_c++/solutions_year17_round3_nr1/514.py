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
    bool operator() (pair<double, i64> p1, pair<double, i64> p2)
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

const double eps = 0.00000001;

i64 T;

i64 mm = 10005;

i64 r[10005];
i64 h[10005];


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        i64 n, k;

        cin >> n >> k;

        for (i64 i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
        }

        set<pair<double, i64>, less_key> a;

        for (i64 i = 0; i < n; i++) {
            a.insert(make_pair(2 * M_PI * r[i] * h[i], i));
        }

        double R = 0;
        for (i64 i = 0; i < n; i++) {
            double cr = M_PI * r[i] * r[i] + 2 * M_PI * r[i] * h[i];

            i64 ck = 0;
            for (auto j: a) {
                if (ck == k - 1) {
                    break;
                }
                if (i == j.second) {
                    continue;
                }
                if (r[j.second] - r[i] > eps) {
                    continue;
                }
                ck++;
                cr += 2 * M_PI * r[j.second] * h[j.second];
            }

            if (ck == k - 1) {
                R = max(R, cr);
            }
        }


        cout << "Case #" << tt << ": " << setprecision(9) << fixed << R << endl;
    }


    return 0;

}
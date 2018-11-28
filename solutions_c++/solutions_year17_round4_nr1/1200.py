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

#include <random>

const i64 mod = 100000000007ll;
const i64 inf = 10000000000000007ll;

const double eps = 0.00000001;

i64 T;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        i64 n, p;
        i64 a[102];

        cin >> n >> p;

        for (i64 i = 0; i < n; i++) {
            cin >> a[i];
        }

        i64 r = 0;
        if (p == 2) {
            i64 h = 0;
            for (i64 i = 0; i < n; i++) {
                if (a[i] % 2) {
                    h++;
                }
                else {
                    r++;
                }
            }
            if (h > 0) {
                r++;
                r += (h - 1) / 2;
            }
        }
        else if (p == 3) {
            i64 h1 = 0;
            i64 h2 = 0;
            for (i64 i = 0; i < n; i++) {
                if (a[i] % 3 == 1) {
                    h1++;
                }
                else if (a[i] % 3 == 2) {
                    h2++;
                }
                else {
                    r++;
                }
            }
            i64 t = min(h1, h2);
            r += t;
            h1 -= t;
            h2 -= t;
            i64 h = max(h1, h2);
            if (h > 0) {
                r++;
                r += (h - 1) / 3;
            }
        }
        else {
            i64 h1 = 0;
            i64 h2 = 0;
            i64 h3 = 0;
            for (i64 i = 0; i < n; i++) {
                if (a[i] % 4 == 1) {
                    h1++;
                }
                else if (a[i] % 4 == 2) {
                    h2++;
                }
                else if (a[i] % 4 == 3) {
                    h3++;
                }
                else {
                    r++;
                }
            }
            r += h2 / 2;
            h2 %= 2;
            i64 t = min(h1, h3);
            r += t;
            h1 -= t;
            h3 -= t;
            i64 h = max(h1, h3);
            if (h2 && !h) {
                r++;
            }
            if (h2 && h >= 2) {
                r += 1;
                h -= 2;
            }
            if (h > 0) {
                r++;
                r += (h - 1) / 4;
            }
        }

        cout << "Case #" << tt << ": " << r << endl;
    }


    return 0;

}
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

char a[30][30];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        i64 r, c;
        cin >> r >> c;

        for (i64 i = 0; i < r; i++) {
            for (i64 j = 0; j < c; j++) {
                cin >> a[i][j];
            }
        }

        for (i64 i = 0; i < r; i++) {
            char q = '?';
            for (i64 j = 0; j < c; j++) {
                if (a[i][j] != '?') {
                    q = a[i][j];
                }
                else if (q != '?') {
                    a[i][j] = q;
                }
            }
            q = '?';
            for (i64 j = c - 1; j >= 0; j--) {
                if (a[i][j] != '?') {
                    q = a[i][j];
                }
                else if (q != '?') {
                    a[i][j] = q;
                }
            }
        }

        for (i64 j = 0; j < c; j++) {
            char q = '?';
            for (i64 i = 0; i < r; i++) {
                if (a[i][j] != '?') {
                    q = a[i][j];
                }
                else if (q != '?') {
                    a[i][j] = q;
                }
            }
            q = '?';
            for (i64 i = r - 1; i >= 0; i--) {
                if (a[i][j] != '?') {
                    q = a[i][j];
                }
                else if (q != '?') {
                    a[i][j] = q;
                }
            }
        }

        cout << "Case #" << tt << ":" << endl;
        for (i64 i = 0; i < r; i++) {
            for (i64 j = 0; j < c; j++) {
                cout << a[i][j];
            }
            cout << endl;
        }
    }

    return 0;
}
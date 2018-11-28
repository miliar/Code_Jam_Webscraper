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

bool check(string& R) {
    if (R.size() == 1) {
        return 1;
    }

    if (R[0] != R[R.size() - 1]) {
        return 1;
    }

    for (i64 i = R.size() - 1; i > 0; i--) {
        swap(R[i], R[i - 1]);
        if (R[i] == R[i - 1]) {
            return 0;
        }
        if (i > 1 && R[i - 1] != R[i - 2]) {
            return 1;
        }
    }

    if (R[0] != R[R.size() - 1]) {
        return 1;
    }

    return 0;
}

bool check2(string& R) {
    bool r = R.size() == 1 || R[0] != R[R.size() - 1];

    for (i64 i = 0; i < R.size() - 1; i++) {
        r = r && (R[i] != R[i + 1]);
    }

    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        i64 n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;

        string R;

        set<pair<i64, char>> a;
        a.insert(make_pair(r, 'R'));
        a.insert(make_pair(y, 'Y'));
        a.insert(make_pair(b, 'B'));


        bool f = 1;
        for (;;) {
            auto it = a.rbegin();
            if (!it->first) {
                break;
            }
            if (R.size() == 0) {
                R.push_back(it->second);
                a.insert(make_pair(it->first - 1, it->second));
                a.erase(*it);
            }

            if (it->second == R[R.size() - 1]) {
                ++it;
            }
            if (it->first == 0) {
                f = false;
                break;
            }
            R.push_back(it->second);
            a.insert(make_pair(it->first - 1, it->second));
            a.erase(*it);
        }

        f = f && check(R);

        if (f) {
            f = check2(R);
        }

        cout << "Case #" << tt << ": " << (f ? R : "IMPOSSIBLE") << endl;
    }

    return 0;
}
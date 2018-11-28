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

bool check(i64 q, i64 e) {
    if (!q) {
        return true;
    }

    if (e < q % 10) {
        return false;
    }

    return check(q / 10, q % 10);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        string s;

        cin >> s;

        for (i64 i = 1; i < s.size(); i++) {
            if (s[i - 1] > s[i]) {
                i64 j;
                for (j = i - 1; j >= 0; j--) {
                    --s[j];
                    if ((j > 0 && s[j] >= s[j - 1]) || !j) {
                            break;
                    }
                }
                for (i64 k = j + 1; k < s.size(); k++) {
                    s[k] = '9';
                }
                break;
             }
        }

        if (s[0] == '0') {
            s = s.substr(1);
        }

        cout << "Case #" << tt << ": " << s << endl;
    }

    return 0;
}
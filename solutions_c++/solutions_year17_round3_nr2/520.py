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

struct tqi;

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

i64 n[2];
pair<i64, i64> a[2][10005];

struct tqi {
    i64 t;
    i64 q;
    i64 i;
};

struct less_key
{
    bool operator() (tqi p1, tqi p2)
    {
        return (p1.t < p2.t) || ((p1.t == p2.t) && (p1.q > p2.q)) || ((p1.t == p2.t) && (p1.q == p2.q) && (p1.i < p2.i));
    }

    bool operator() (pair<i64, i64> p1, pair<i64, i64> p2)
    {
        return (p1.first < p2.first) || (p1.first == p2.first && p1.second < p2.second);
    }

};

set<tqi, less_key> q;



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        q.clear();

        cin >> n[0] >> n[1];

        for (i64 j = 0; j < 2; j++) {
            for (i64 i = 0; i < n[j]; i++) {
                cin >> a[j][i].first >> a[j][i].second;
            }
        }

        i64 s[2] = {0, 0};

        for (i64 j = 0; j < 2; j++) {
            for (i64 i = 0; i < n[j]; i++) {
                s[j] += a[j][i].second - a[j][i].first;

                q.insert({ a[j][i].first, 0, j });
                q.insert({ a[j][i].second, 1, j });
            }
        }

        set<pair<i64, i64>, less_key> e[2]; // len, start

        for (auto cit = q.begin(); cit != q.end(); cit++) {
            auto nit = cit;
            nit++;
            if (nit == q.end()) {
                break;
            }
            if (cit->i == nit->i && cit->q == 1 && nit->q == 0) {
                e[cit->i].insert(make_pair(nit->t - cit->t, cit->t));
            }
        }

        if (q.size() > 0) {
            auto fit = q.begin();
            auto eit = q.rbegin();
            if (fit->i == eit->i) {
                e[fit->i].insert(make_pair(24 * 60 - eit->t + fit->t, eit->t));
            }
        }

        for (i64 j = 0; j < 2; j++) {
            for (auto i: e[j]) {
                if (s[j] + i.first <= 720) {
                    s[j] += i.first;
                    q.insert({ i.second, 0, j });
                    if (i.second + i.first <= 24 * 60) {
                        q.insert({ i.second + i.first, 1, j });
                    }
                    else {
                        q.insert({ 24 * 60, 1, j });
                        q.insert({ 0, 0, j });
                        q.insert({ i.first - (24 * 60 - i.second), 1, j });
                    }
                }
            }
        }

        i64 R = 0;
        for (auto cit = q.begin(); cit != q.end(); cit++) {
            auto nit = cit;
            nit++;
            if (nit == q.end()) {
                break;
            }

            if (cit->i == nit->i && cit->q == 0 && nit->q == 1) {
                continue;
            }

            if (cit->i == nit->i && cit->t == nit->t) {
                continue;
            }
            if (cit->i == nit->i && cit->t != nit->t) {
                R += 2;
                continue;
            }
            if (cit->i != nit->i) {
                R += 1;
            }
        }

        if (1) {
            auto fit = q.begin();
            auto eit = q.rbegin();
            if (fit->i == eit->i && !(eit->t == 24 * 60 && fit->t == 0)) {
                R += 2;
            }
            else if (fit->i != eit->i) {
                R += 1;
            }
        }


        cout << "Case #" << tt << ": " << R << endl;
    }


    return 0;

}
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

i64 n, k;
double p[105];
double u;

double f(double a, double b, double ta, double tb) {
    if (a + ta > 1.0) {
        ta = 1.0 - a;
    }
    if (b + tb > 1.0) {
        tb = 1.0 - b;
    }
    return ta * b + tb * a + ta * tb;
}

double solve(double a, double b, double l, double r, double u) {
    while (r - l > eps) {
        double m1 = l + (r - l) / 3;
        double m2 = r - (r - l) / 3;
        if (f(a, b, m1, u - m1) < f(a, b, m2, u - m2)) {
            l = m1;
        }
        else {
            r = m2;
        }
    }

    double m = (r + l) / 2;
    cout << a + m << " " << b + u - m << endl;
    return f(a, b, m, u - m);
}

double solve(i64 i, i64 j, double u) {
    return solve(p[i], p[j], 0, u, u);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    //n = 2;
    //u = 0.4;
    //p[0] = 0.3;
    //p[1] = 0;

    //cout << setprecision(9) << fixed << solve(0, 1, u) << endl;

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        cin >> n >> k;
        cin >> u;

        for (i64 i = 0; i < n; i++) {
            cin >> p[i];
        }

        map<double, i64> q;
        for (i64 i = 0; i < n; i++) {
            q[p[i]]++;
        }

        for (;;) {
            if (q.size() == 1) {
                auto t = *q.begin();
                q.clear();
                q.insert({ t.first + u / t.second, t.second });
                break;
            }

            auto cit = *q.begin();
            auto it = q.begin();
            it++;
            auto eit = *it;

            double d = eit.first - cit.first;
            if (d * cit.second - u < eps) {
                q.erase(q.begin());
                q.begin()->second += cit.second;
                u -= d * cit.second;
            }
            else {
                double t = u / cit.second;
                q.erase(q.begin());
                q.insert({ cit.first + t, cit.second });
                break;
            }
        }

        double R = 1.0;
        for (auto a : q) {
            for (i64 i = 0; i < a.second; i++) {
                R *= min(1.0, a.first);
            }
        }

        cout << "Case #" << tt << ": " << setprecision(9) << fixed << R << endl;
    }


    return 0;

}
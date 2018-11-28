#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <cmath>

using namespace std;

#ifndef PI
#define PI 3.14159265358979323846
#endif

class T { public:
    int r, h;
    double w;
    T() {}
    bool operator <(const T &x) const {
        if (w != x.w) return w < x.w;
        return make_pair(h, r) < make_pair(x.h, x.r);
    }
    bool operator >(const T &x) const {
        if (w != x.w) return w > x.w;
        return make_pair(h, r) > make_pair(x.h, x.r);
    }
};

int n, k;
vector<T> v;

double solve() {
    cin >> n >> k;
    v.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i].r >> v[i].h;
        v[i].w = 2 * PI * v[i].r * v[i].h;
    }

    sort(v.begin(), v.end(), greater<T>());

    int r = 0;
    double result = 0;
    for (int i = 0; i < k-1; i++) {
        result += v[i].w;
        r = max(r, v[i].r);
    }

    r = max(r, v[k-1].r);
    double ww = PI * r * r;
    double best = v[k-1].w + ww;

    for (int i = k; i < n; i++) {
        double temp = v[i].w +    PI * v[i].r * v[i].r;
        if (best < temp) {
            best = temp;
        }
    }

    return result + best;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: %0.9f\n", i, solve());
    }
}


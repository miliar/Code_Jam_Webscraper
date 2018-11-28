#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

class T { public :
    int k, s;
    bool operator <(const T& x) const {
        return make_pair(k, s) < make_pair(x.k, x.s);
    }
};

int d, n;
vector<T> in;

double solve() {
    cin >> d >> n;
    in.resize(n);
    for (int i = 0; i < n; i++) cin >> in[i].k >> in[i].s;

    double r = 0;
    for (int i = 0; i < n; i++) {
        double cand = ((double)d - in[i].k) / in[i].s;
        r = max(r, cand);
    }
    return d / r;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: %0.6f\n", i, solve());
    }
}


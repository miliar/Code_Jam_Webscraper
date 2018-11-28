#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#ifdef __APPLE__
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

const int N = (int)1e6 + 123;
const int MOD = (int)1e9 + 7;
const int inf = (int)5e8;
const long long infll = (long long)1e17;

struct Horse {
    double pos;
    double speed;
    Horse() {}
    void scan() {
        scanf("%lf %lf", &pos, &speed);
    }
};

bool double_equal(double a, double b) {
    return fabs(a - b) < 1e-9;
}

bool double_less(double a, double b) {
    return a < b && !double_equal(a, b);
}

bool double_less_or_equal(double a, double b) {
    return a < b || double_equal(a, b);
}

void solve() {
    double d;
    int n;
    scanf("%lf %d", &d, &n);
    vector<Horse> horses(n);
    double max_time = 0;
    for (auto& horse : horses) {
        horse.scan();
        max_time = max(max_time, (d - horse.pos) / horse.speed);
    }
    printf("%.6lf\n", d / max_time);

}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

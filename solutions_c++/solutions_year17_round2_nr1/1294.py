#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define MOD (1000000000000007LL)
#define LL long long


#define sqr(x) ((x) * (x))
#define Nmax 200333

inline void test_out() {
    static int test_id = 0;
    test_id ++;
    cout << "Case #" << test_id << ": ";
}

pair<int,int> a[2222];
int D, n;
double maxSpeed(int from) {
    if (from > n) {
        return MOD;
    }
    double result = MOD;
    for (int i = from; i <= n; i ++) {
        double temp = (D - a[i].first) * 1.0 / a[i].second;
        result = min(result, D * 1. / temp);
    }
    return result;
}
int main() {
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("answer.txt", "w", stdout);

    int test_number;
    cin >> test_number;
    while (test_number --> 0) {
        cin >> D >> n;
        for (int i= 1; i <= n; i ++) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a + 1, a + n + 1);
        double answer = maxSpeed(1);
        double minspeed = MOD;
        for (int i = 1; i <= n; i ++) {
            minspeed = min(minspeed, 1.*a[i].second);
            answer = max(answer, min(minspeed, maxSpeed(i + 1)));
        }
        test_out();
        cout.precision(8);
        cout << fixed << answer << endl;
    }
    return 0;
}

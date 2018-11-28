#include <bits/stdc++.h>
using namespace std;
typedef std::pair<int, int> ii;
const long double pi = acos((long double) -1);

void preprocess() {
}

struct X {
    bool operator()(long double a, long double b) {
        if (fabs(a-b) < 1e-6) {
            return false;
        }
        return a < b;
    }
};

void process_testcase(const int testcase, const int should_run) {
    int n, k;
    cin>>n>>k;
    long double u;
    cin>>u;
    long double p[n];
    for (int i = 0; i < n; ++i)
        cin>>p[i];

    if (should_run) {
        long double ans = -1;
        for (int i = 1; i <= 1000000 && u > 1e-6; ++i) {
            map<long double, vector<int>, X> m;
            for (int i= 0; i < n; ++i)
                m[p[i]].push_back(i);
            if (m.size() == 1) {
                long double delta = u / n;
                for (int i = 0; i < n; ++i)
                    p[i] += delta;
                u = 0;
            } else {
                auto min1 = *m.begin();
                auto min2 = *(++m.begin());
                long double delta = min(min2.first - min1.first, u / min1.second.size());
                for (int i : min1.second) {
                    p[i] += delta;
                }
                u -= delta*min1.second.size();
            }
        }
        ans = 1;
        for (int i = 0; i < n; ++i)
            ans *= p[i];

        printf("Case #%d: %.12lf\n", testcase, (double) ans);
    }
}

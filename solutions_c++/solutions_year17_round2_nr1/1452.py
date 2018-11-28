#include <bits/stdc++.h>
using namespace std;
typedef std::pair<int, int> ii;

void preprocess() {
}

void process_testcase(const int testcase, const int should_run) {
    long long d, n;
    cin>>d>>n;
    long double k[n+1], s[n+1];
    k[0] = 0;
    s[0] = 1e15;
    for (int i = 1; i <= n; ++i)
        cin>>k[i]>>s[i];
    if (should_run) {
        for (int i = n-1; i >= 0; --i) {
            long double time2 = (d - k[i+1]) / s[i+1];
            long double speed = (d - k[i]) / time2;
            if (speed < s[i])
                s[i] = speed;
        }

        printf("Case #%d: %.9lf\n", testcase, (double) s[0]);
    }
}
